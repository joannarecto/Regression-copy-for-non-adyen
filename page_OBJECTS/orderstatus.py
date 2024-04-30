from selenium.webdriver.common.by import By
from time import sleep

class OrderStatus:

    def __init__(self, driver):
        self.driver = driver

    shopfront_btn = (By.XPATH, "//*[contains(@class,'btn-secondary')]")

    def click_shopfrontbtn(self):
        self.driver.find_element(*OrderStatus.shopfront_btn).click()
        sleep(5)

    #-------------------------------------------------------------------------------------------------------------------

    receipt = (By.XPATH, "//*[contains(text(),'receipt')]")

    def view_receipt(self):
        self.driver.find_element(*OrderStatus.receipt).click()
        sleep(5)

    #-------------------------------------------------------------------------------------------------------------------

    orderid = (By.XPATH, "//*[contains(text(),'Order number')]")

    def get_orderid(self):
        return self.driver.find_element(*OrderStatus.orderid).text
        sleep(5)

    #-------------------------------------------------------------------------------------------------------------------

    receipt_subtotal = (By.XPATH, "(//*[contains(@class, 'price-wrapper')])[1]")
    receipt_ordertotal = (By.XPATH, "(//*[contains(@class, 'm-0')]/strong)[1]")

    def check_receipt_subtotal(self):
        currency_text = self.driver.find_element(*OrderStatus.receipt_subtotal).text
        print(currency_text)
        currency_str = currency_text.replace("\n", "")
        return print(currency_str)

    def check_receipt_totalcurrency(self):
        currency_text = self.driver.find_element(*OrderStatus.receipt_ordertotal).text
        print(currency_text)
        currency_str = currency_text.replace("\n", "")
        return print(currency_str)


    #-------------------------------------------------------------------------------------------------------------------

    itemprice1 = (By.XPATH, "//*[contains(@class,'receipt-description')]/div/div/div[2]")

    def get_itemprice1_with_whitespace(self):
        return self.driver.find_element(*OrderStatus.itemprice1).text.replace(" \n", " ")

    def get_itemprice1_without_whitespace(self):
        return self.driver.find_element(*OrderStatus.itemprice1).text.strip()

    def get_aud_itemprice1(self):
        return self.get_itemprice1_with_whitespace()

    def get_cad_itemprice1(self):
        return self.get_itemprice1_with_whitespace()

    def get_eur_itemprice1(self):
        return self.get_itemprice1_without_whitespace()

    def get_eur_c_itemprice1(self):
        return self.get_itemprice1_without_whitespace()

    def get_eur_i_itemprice1(self):
        return self.get_itemprice1_without_whitespace()

    def get_gbp_itemprice1(self):
        return self.get_itemprice1_without_whitespace()

    def get_nzd_itemprice1(self):
        return self.get_itemprice1_with_whitespace()

    def get_usd_itemprice1(self):
        return self.get_itemprice1_with_whitespace()

    def get_usd_e_itemprice1(self):
        return self.get_itemprice1_with_whitespace()

    def get_usd_n_itemprice1(self):
        return self.get_itemprice1_with_whitespace()

    #-------------------------------------------------------------------------------------------------------------------

    ordertotal = (By.XPATH, "//*[contains(@class,'receipt-description')]/div[2]/p[2]")

    def get_ordertotal_with_whitespace(self):
        return self.driver.find_element(*OrderStatus.ordertotal).text.replace(" \n", " ")

    def get_ordertotal_without_whitespace(self):
        return self.driver.find_element(*OrderStatus.ordertotal).text.strip()

    def get_aud_ordertotal(self):
        return self.get_ordertotal_with_whitespace()

    def get_cad_ordertotal(self):
        return self.get_ordertotal_with_whitespace()

    def get_eur_ordertotal(self):
        return self.get_ordertotal_without_whitespace()

    def get_eur_c_ordertotal(self):
        return self.get_itemprice1_without_whitespace()

    def get_eur_i_ordertotal(self):
        return self.get_itemprice1_without_whitespace()

    def get_gbp_ordertotal(self):
        return self.get_itemprice1_without_whitespace()

    def get_nzd_ordertotal(self):
        return self.get_ordertotal_with_whitespace()

    def get_usd_ordertotal(self):
        return self.get_ordertotal_with_whitespace()

    def get_usd_e_ordertotal(self):
        return self.get_ordertotal_with_whitespace()

    def get_usd_n_ordertotal(self):
        return self.get_ordertotal_with_whitespace()

    #-------------------------------------------------------------------------------------------------------------------

    cartoval = (By.XPATH, "//*[@class='oval']")

    def cartoval_displayed(self):
        return self.driver.find_element(*OrderStatus.cartoval).is_displayed()

    #-------------------------------------------------------------------------------------------------------------------

    backtoshopping = (By.XPATH, "//*[text()=' Back to shopping ']")

    def click_backtoshopping(self):
        self.driver.find_element(*OrderStatus.backtoshopping).click()
        sleep(25)
