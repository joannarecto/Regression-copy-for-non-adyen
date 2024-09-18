from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox
from time import sleep
import pytest

driver = None

#-----------------------------------------------------------------------------------------------------------------------
# browser invocation

@pytest.fixture(scope="class")
def setup(request):

    global driver

    profile_path = "C:\\Users\\jgabriel\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\y76yonvq.automationprofile"

    options = Options()
    options.set_preference('profile', profile_path)
    options.headless = True

    # service = Service("C:\\Users\\jgabriel\\geckodriver.exe")

    # driver = Firefox(service=service, options=options)

    driver = webdriver.Remote(command_executor="http://192.168.1.4:4444/wd/hub", options=options)
    # desired_capabilities={"node": "node-1"},
    # options=options)

    driver.get("https://qa-shopfront.cambridgedev.org/")

    # driver.get("https://release-shopfront.cambridgedev.org/")

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
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

#-----------------------------------------------------------------------------------------------------------------------
