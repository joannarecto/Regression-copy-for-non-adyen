from selenium.webdriver.common.by import By
from time import sleep

class Basket:

    def __init__(self, driver):
        self.driver = driver

    gotocheckout = (By.XPATH, "//*[contains(@class,'flex-column')]/button")

    def click_gotocheckout(self):
        self.driver.find_element(*Basket.gotocheckout).click()
        sleep(5)

# ---------------------------------------------------------------------------------------------------------------------
    basket_price1 = (By.XPATH, "(//*[contains(@class, 'price-wrapper')])[1]")
    basket_total = (By.XPATH, "(//*[contains(@class, 'm-0')]/strong)[1]")

    def check_basket_itemcurrency(self):
        currency_text = self.driver.find_element(*Basket.basket_price1).text
        currency_str = currency_text.replace("\n", "")
        return currency_str

    def check_basket_totalcurrency(self):
        currency_text = self.driver.find_element(*Basket.basket_price1).text
        currency_str = currency_text.replace("\n", "")
        return currency_str

    #-------------------------------------------------------------------------------------------------------------------

    itemprice1 = (By.XPATH, "//*[contains(@class,'price')]")

    def get_itemprice1_with_whitespace(self):
        return self.driver.find_element(*Basket.itemprice1).text.replace(" \n", " ")

    def get_itemprice1_without_whitespace(self):
        return self.driver.find_element(*Basket.itemprice1).text.strip()

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

    ordertotal = (By.XPATH, "(//*[contains(@class,'basket-description')]/p[2])[1]")

    def get_ordertotal_with_whitespace(self):
        return self.driver.find_element(*Basket.ordertotal).text.replace(" \n", " ")

    def get_ordertotal_without_whitespace(self):
        return self.driver.find_element(*Basket.ordertotal).text.strip()

    def get_aud_ordertotal(self):
        return self.get_ordertotal_with_whitespace()

    def get_cad_ordertotal(self):
        return self.get_ordertotal_with_whitespace()

    def get_eur_ordertotal(self):
        return self.get_ordertotal_without_whitespace()

    def get_eur_c_ordertotal(self):
        return self.get_ordertotal_without_whitespace()

    def get_eur_i_ordertotal(self):
        return self.get_ordertotal_without_whitespace()

    def get_gbp_ordertotal(self):
        return self.get_ordertotal_without_whitespace()

    def get_nzd_ordertotal(self):
        return self.get_ordertotal_with_whitespace()

    def get_usd_ordertotal(self):
        return self.get_ordertotal_with_whitespace()

    def get_usd_e_ordertotal(self):
        return self.get_ordertotal_with_whitespace()

    def get_usd_n_ordertotal(self):
        return self.get_ordertotal_with_whitespace()
