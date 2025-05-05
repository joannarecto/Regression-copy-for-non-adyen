from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

# def wait_for_element(driver, by, value, timeout=50):
#     return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

def wait_for_elements(driver, by, value, timeout=50):
    wait = WebDriverWait(driver, timeout)

    try:
        # 2. Wait for the element to be present in the DOM
        element = wait.until(EC.presence_of_all_elements_located((by, value)))
        return element
    except TimeoutException:
        print("trying 2nd option")

    try:
        # 1. Wait for the element to be visible
        element = wait.until(EC.visibility_of_all_elements_located((by, value)))
        return element
    except TimeoutException:
        print("trying 3rd option")

    try:
        # 3. Wait for the element to be clickable
        element = wait.until(EC.element_to_be_clickable((by, value)))
        return element
    except TimeoutException:
        print("sadt")

def wait_for_element(driver, by, value, timeout=50):
    wait = WebDriverWait(driver, timeout)

    try:
        # 2. Wait for the element to be present in the DOM
        element = wait.until(EC.presence_of_element_located((by, value)))
        return element
    except TimeoutException:
        print("trying 2nd option")

    try:
        # 1. Wait for the element to be visible
        element = wait.until(EC.visibility_of_element_located((by, value)))
        return element
    except TimeoutException:
        print("trying 3rd option")

    try:
        # 3. Wait for the element to be clickable
        element = wait.until(EC.element_to_be_clickable((by, value)))
        return element
    except TimeoutException:
        print("sadt")
