from time import sleep

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = None

#-----------------------------------------------------------------------------------------------------------------------
# browser invocation

@pytest.fixture(scope="class")
def setup(request):

    global driver

    # profile_path = "C:\\Users\\mrecto\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
    options = Options()
    # options.add_argument(f"user-data-dir={profile_path}")
    options.add_argument("--window-size=360,800")
    options.add_argument("--start-maximized")
    options.add_argument("--headless")  # Use headless mode for running in the background
    options.add_argument("--disable-gpu")
    service = Service("C:\\Drivers\\chromedriver\\chromedriver.exe")
    driver = Chrome(service=service, options=options)

    # driver.get("https://qa-shopfront.cambridgedev.org/")

    driver.get("https://release-shopfront.cambridgedev.org/")

    sleep(25)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

#-----------------------------------------------------------------------------------------------------------------------
# code, which screenshots where the error occurred

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed a screenshot in the HTML report whenever a test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when in ('call', 'setup'):
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_full_screen_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_full_screen_screenshot(name):
    # Use JavaScript to get the full width and height of the webpage
    height = driver.execute_script('return document.documentElement.scrollHeight')
    width = driver.execute_script('return document.documentElement.scrollWidth')

    # Set the window size to match the entire webpage
    driver.set_window_size(width, height)

    # Find the full page element (usually 'body') and capture the screenshot
    full_page = driver.find_element(By.TAG_NAME, "body")
    full_page.screenshot(name)

#-----------------------------------------------------------------------------------------------------------------------
