from selenium.webdriver.common.by import By
from time import sleep

class Basket:

    def __init__(self, driver):
        self.driver = driver

    gotocheckout = (By.XPATH, "//*[contains(@class,'flex-column')]/button")

    def click_gotocheckout(self):
        self.driver.find_element(*Basket.gotocheckout).click()
        sleep(5)
