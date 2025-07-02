from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from page_OBJECTS.data import Data
from selenium.webdriver.support.ui import WebDriverWait

class PayPal:

    def __init__(self, driver):
        self.driver = driver

    paypalemailaddress = (By.XPATH, "//*[@id='email']")

    next               = (By.XPATH, "//*[@id='btnNext']")

    paypalpassword     = (By.XPATH, "//*[@id='password']")

    login              = (By.XPATH, "//*[@id='btnLogin']")

    completepurchase   = (By.XPATH, "//button[@data-id='payment-submit-btn']")

    paypalcookies      = (By.XPATH, "//*[contains(@id,'Cookie')]")

    accept             = (By.XPATH, "//*[contains(@id,'accept')]")

    tryagain           = (By.XPATH, "//a[@class='btn full' and text()='Please try again']")

    def input_paypal_emailaddress(self):

        i = Data (self.driver)

        return self.driver.find_element(*PayPal.paypalemailaddress).send_keys(i.paypal_emailaddress)
        sleep(5)

    def click_next(self):
        self.driver.find_element(*PayPal.next).click()
        sleep(5)

    def input_paypal_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*PayPal.paypalpassword).send_keys(i.paypal_password)
        sleep(5)

    def click_login(self):
        self.driver.find_element(*PayPal.login).click()
        sleep(5)

    def click_completepurchase(self):
        self.driver.find_element(*PayPal.completepurchase).click()
        sleep(5)

    def verify_if_paypal_cookies_is_displayed(self):
        self.driver.find_element(*PayPal.paypalcookies).is_displayed()
        sleep(5)

    def click_accept(self):
        self.driver.find_element(*PayPal.accept).click()
        sleep(5)

    def handle_try_again_modal(self, timeout=3):
        try:
            try_again_button = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(PayPal.tryagain)
            )
            try_again_button.click()
            sleep(5)
        except TimeoutException:
            pass


    def login_and_pay(self):
        main_window = self.driver.window_handles[0]
        paypal_window = self.driver.window_handles[1]
        self.driver.switch_to.window(paypal_window)
        sleep(1)
        self.handle_try_again_modal()
        self.input_paypal_emailaddress()
        self.handle_try_again_modal()
        self.click_next()
        self.handle_try_again_modal()
        self.input_paypal_password()
        self.handle_try_again_modal()
        self.click_login()
        self.handle_try_again_modal()
        self.click_completepurchase()
        self.handle_try_again_modal()
        sleep(5)
        self.driver.switch_to.window(main_window)
        sleep(10)
