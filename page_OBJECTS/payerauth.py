from selenium.webdriver.common.by import By
from time import sleep

class PayerAuth:

    def __init__(self, driver):
        self.driver = driver

    code   = (By.XPATH, "//*[contains(@placeholder,'Code')]")

    submit = (By.XPATH, "//*[@value='SUBMIT']")

    def payerauth_frame(self):
        return self.driver.find_elements(by=By.TAG_NAME, value="iframe")[0]

    def input_code(self):
        return self.driver.find_element(*PayerAuth.code).send_keys("1234")
        sleep(5)

    def click_submit(self):
        self.driver.find_element(*PayerAuth.submit).click()
        sleep(25)

    def authenticate_payment(self):
        self.driver.switch_to.frame(self.payerauth_frame())
        self.input_code()
        self.click_submit()
        self.driver.switch_to.default_content()
