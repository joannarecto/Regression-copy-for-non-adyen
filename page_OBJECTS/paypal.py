from selenium.webdriver.common.by import By
from time import sleep

from page_OBJECTS.data import Data

class PayPal:

    def __init__(self, driver):
        self.driver = driver

    paypalemailaddress = (By.XPATH, "//*[@id='email']")

    next               = (By.XPATH, "//*[@id='btnNext']")

    paypalpassword     = (By.XPATH, "//*[@id='password']")

    login              = (By.XPATH, "//*[@id='btnLogin']")

    completepurchase   = (By.XPATH, "//*[@id='payment-submit-btn']")

    paypalcookies      = (By.XPATH, "//*[contains(@id,'Cookie')]")

    accept             = (By.XPATH, "//*[contains(@id,'accept')]")

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

    def login_and_pay(self):
        main_window = self.driver.window_handles[0]
        paypal_window = self.driver.window_handles[1]
        self.driver.switch_to.window(paypal_window)
        self.input_paypal_emailaddress()
        self.click_next()
        self.input_paypal_password()
        self.click_login()
        if self.paypalcookies == True:
            self.click_accept()
            sleep(5)
            self.click_completepurchase()
            sleep(25)
        else:
            self.click_completepurchase()
            sleep(25)
        self.driver.switch_to.window(main_window)
