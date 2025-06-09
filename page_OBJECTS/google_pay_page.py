from page_OBJECTS.data import Data

from selenium.webdriver.common.by import By
from utilities.wait import wait_for_element
from time import sleep

class GooglePay:

    def __init__(self, driver):
        self.driver = driver

    #-------------------------------------------------------------------------------------------------------------------

    google_pay_email_address = (By.XPATH, "//*[@id='identifierId']")

    def INPUT_GOOGLE_PAY_EMAIL_ADDRESS(self):

        i = Data

        a = wait_for_element(self.driver, *self.google_pay_email_address)
        return a.send_keys(i.google_pay_email_address)

    #-------------------------------------------------------------------------------------------------------------------

    next = (By.XPATH, "//*[text()='Next']")

    def CLICK_NEXT(self):
        a = wait_for_element(self.driver, *self.next)
        a.click()
        sleep(15)

    #-------------------------------------------------------------------------------------------------------------------

    google_pay_password = (By.XPATH, "//*[@id='password']/div/div/div/input")

    def INPUT_GOOGLE_PAY_PASSWORD(self):

        i = Data

        a = wait_for_element(self.driver, *self.google_pay_password)
        return a.send_keys(i.google_pay_password)

    #-------------------------------------------------------------------------------------------------------------------

    # continue_purchase = (By.XPATH, "//span[@jsname='V67aGc' and @class='VfPpkd-vQzf8d' and text()='Continue']")
    #
    # def CLICK_CONTINUE(self):
    #     a = wait_for_element(self.driver, *self.continue_purchase)
    #     if a:
    #         self.driver.execute_script("arguments[0].click();", a)
    #         sleep(30)
    #     else:
    #         raise Exception("Continue purchase button not found")



    # next = (By.XPATH, "//*[text()='Next']")
    continuebtn = (By.XPATH, "//*[text()='Pay']")

    def CLICK_CONTINUE(self):
        a = wait_for_element(self.driver, *self.continuebtn)
        a.click()
        sleep(15)


    #-------------------------------------------------------------------------------------------------------------------

    google_pay_frame = (By.XPATH, "//div[@class='bootstrapperIframeContainerElement']//iframe")

    def GOOGLE_PAY_FRAME(self):
        a = wait_for_element(self.driver, *self.google_pay_frame)
        return a

    #-------------------------------------------------------------------------------------------------------------------

    def LOGIN_AND_PAY(self):
        main_window = self.driver.window_handles[0]
        google_pay_window = self.driver.window_handles[1]
        self.driver.switch_to.window(google_pay_window)
        self.INPUT_GOOGLE_PAY_EMAIL_ADDRESS()
        self.CLICK_NEXT()
        self.INPUT_GOOGLE_PAY_PASSWORD()
        self.CLICK_NEXT()
        sleep(25)
        self.driver.switch_to.frame(self.GOOGLE_PAY_FRAME())
        self.CLICK_CONTINUE()
        self.driver.switch_to.default_content()
        sleep(5)
        self.driver.switch_to.window(main_window)
        sleep(5)

    #-------------------------------------------------------------------------------------------------------------------
