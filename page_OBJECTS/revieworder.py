from selenium.webdriver.common.by import By
from time import sleep

class ReviewOrder:

    def __init__(self, driver):
        self.driver = driver

    card         = (By.XPATH, "(//div[@class='card-header'])[1]")

    cardnumber   = (By.XPATH, "//*[@id='number']")

    expirydate   = (By.XPATH, "//*[@id='expiry-date']")

    securitycode = (By.XPATH, "//*[@id='securityCode']")

    paynow       = (By.XPATH, "//*[contains(@class,'payment-btn')]")

    def click_card(self):
        self.driver.find_element(*ReviewOrder.card).click()
        sleep(5)

    def cardnumber_frame(self):
        return self.driver.find_elements(by=By.TAG_NAME, value="iframe")[0]

    def input_cardnumber(self):
        return self.driver.find_element(*ReviewOrder.cardnumber).send_keys("4456 5300 0000 1096")
        sleep(5)

    # def input_expirydate(self):
    #     return self.driver.find_element(*ReviewOrder.expirydate).send_keys(" 1224 ")
    #     sleep(5)

    def input_expirymonth(self):
        return self.driver.find_element(*ReviewOrder.expirydate).send_keys("12")
        sleep(5)

    def input_expiryyear(self):
        return self.driver.find_element(*ReviewOrder.expirydate).send_keys("24")
        sleep(5)

    def securitycode_frame(self):
        return self.driver.find_elements(by=By.TAG_NAME, value="iframe")[1]

    def input_securitycode(self):
        return self.driver.find_element(*ReviewOrder.securitycode).send_keys("123")
        sleep(5)

    def click_paynow(self):
        self.driver.find_element(*ReviewOrder.paynow).click()
        sleep(25)

    def pay_via_card(self):
        self.click_card()
        self.driver.switch_to.frame(self.cardnumber_frame())
        self.input_cardnumber()
        self.driver.switch_to.default_content()
        self.input_expirymonth()
        self.input_expiryyear()
        self.driver.switch_to.frame(self.securitycode_frame())
        self.input_securitycode()
        self.driver.switch_to.default_content()
        self.click_paynow()

    #-------------------------------------------------------------------------------------------------------------------

    paypal       = (By.XPATH, "(//div[@class='card-header'])[2]")

    paypalbutton = (By.XPATH, "//*[contains(@id,'button-container')]")

    def click_paypal(self):
        self.driver.find_element(*ReviewOrder.paypal).click()
        sleep(5)

    def open_paypal(self):
        self.driver.find_element(*ReviewOrder.paypalbutton).click()
        sleep(25)

    def pay_via_paypal(self):
        self.click_paypal()
        self.open_paypal()
