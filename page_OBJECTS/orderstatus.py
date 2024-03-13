from selenium.webdriver.common.by import By
from time import sleep

class OrderStatus:

    def __init__(self, driver):
        self.driver = driver

    receipt = (By.XPATH, "//*[contains(text(),'receipt')]")

    def view_receipt(self):
        self.driver.find_element(*OrderStatus.receipt).click()
        sleep(5)

    #-------------------------------------------------------------------------------------------------------------------

    orderid = (By.XPATH, "//*[contains(text(),'Order number')]")

    def get_orderid(self):
        return self.driver.find_element(*OrderStatus.orderid).text
        sleep(5)
