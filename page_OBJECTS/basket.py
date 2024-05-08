from selenium.webdriver.common.by import By
from time import sleep

class Basket:

    def __init__(self, driver):
        self.driver = driver

    basket_products = (By.XPATH, "(//*[contains(@class,'product')])[2]")

    def basketproducts_displayed(self):
        self.driver.find_element(*Basket.basket_products).is_displayed()

    #-------------------------------------------------------------------------------------------------------------------

    basket_products = (By.XPATH, "//div[@class='product']")

    def basketproducts_displayed(self):
        return self.driver.find_element(*Basket.basket_products).is_displayed()

    #-------------------------------------------------------------------------------------------------------------------

    empty_basket = (By.XPATH, "//p[@class='mb-5 mb-md-0']")

    def empty_basket_label(self):
        return self.driver.find_element(*Basket.empty_basket).text

    #-------------------------------------------------------------------------------------------------------------------

    gotocheckout = (By.XPATH, "//*[contains(@class,'flex-column')]/button")

    def click_gotocheckout(self):
        self.driver.find_element(*Basket.gotocheckout).click()
        sleep(5)

# ---------------------------------------------------------------------------------------------------------------------
#     basket_price1 = (By.XPATH, "(//*[contains(@class, 'price-wrapper')])[1]")
#     basket_total = (By.XPATH, "(//*[contains(@class, 'm-0')]/strong)[1]")
#
#     def check_basket_itemcurrency(self):
#         currency_text = self.driver.find_element(*Basket.basket_price1).text
#         currency_str = currency_text.replace("\n", "")
#         return currency_str
#
#     def check_basket_totalcurrency(self):
#         currency_text = self.driver.find_element(*Basket.basket_price1).text
#         currency_str = currency_text.replace("\n", "")
#         return currency_str

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

    #-------------------------------------------------------------------------------------------------------------------

    def go_back(self):
        self.driver.back()
        sleep(25)

    #-------------------------------------------------------------------------------------------------------------------

    backtoshopping = (By.XPATH, "//*[text()=' Back to shopping ']")

    def click_backtoshopping(self):
        self.driver.find_element(*Basket.backtoshopping).click()
        sleep(25)

    def backtoshopping_enabled(self):
        return self.driver.find_element(*Basket.backtoshopping).is_enabled()

    #-------------------------------------------------------------------------------------------------------------------

    continueshopping = (By.XPATH, "//*[text()=' Continue shopping ']")

    def click_continueshopping(self):
        self.driver.find_element(*Basket.continueshopping).click()
        sleep(25)

    def continueshopping_enabled(self):
        return self.driver.find_element(*Basket.continueshopping).is_enabled()

    #-------------------------------------------------------------------------------------------------------------------

    chevron = (By.XPATH, "//*[contains(@class,'chevron')]")

    def click_chevron(self):
        self.driver.find_element(*Basket.chevron).click()
        sleep(25)

    def chevron_enabled(self):
        return self.driver.find_element(*Basket.chevron).is_enabled()

    #-------------------------------------------------------------------------------------------------------------------

    deleteitem1 = (By.XPATH, "(//*[contains(@class,'basket-delete')])[1]")

    deleteitem2 = (By.XPATH, "(//*[contains(@class,'basket-delete')])[2]")

    def delete_item1(self):
        self.driver.find_element(*Basket.deleteitem1).click()
        sleep(8)

    def delete_item2(self):
        self.driver.find_element(*Basket.deleteitem2).click()
        sleep(8)

    #-------------------------------------------------------------------------------------------------------------------

    undoitem1 = (By.XPATH, "(//*[text()=' Undo '])[1]")

    undoitem2 = (By.XPATH, "(//*[text()=' Undo '])[2]")

    def undo_item1(self):
        self.driver.find_element(*Basket.undoitem1).click()
        sleep(8)

    def undo_item2(self):
        self.driver.find_element(*Basket.undoitem2).click()
        sleep(8)

    #-------------------------------------------------------------------------------------------------------------------

    saveforlateritem1 = (By.XPATH, "(//*[text()=' Save for later '])[1]")

    saveforlateritem2 = (By.XPATH, "(//*[text()=' Save for later '])[2]")

    def saveforlater_item1(self):
        self.driver.find_element(*Basket.saveforlateritem1).click()
        sleep(8)

    def saveforlater_item2(self):
        self.driver.find_element(*Basket.saveforlateritem2).click()
        sleep(8)

    #-------------------------------------------------------------------------------------------------------------------

    movetobasketitem1 = (By.XPATH, "(//*[text()=' Move to basket '])[1]")

    movetobasketitem2 = (By.XPATH, "(//*[text()=' Move to basket '])[2]")

    def movetobasket_item1(self):
        self.driver.find_element(*Basket.movetobasketitem1).click()
        sleep(8)

    def movetobasket_item2(self):
        self.driver.find_element(*Basket.movetobasketitem2).click()
        sleep(8)

    #-------------------------------------------------------------------------------------------------------------------

    qtyitem1 = (By.XPATH, "(//*[contains(@id,'qty-input')])[1]")

    def get_item1_qty(self):
        self.driver.find_element(*Basket.qtyitem1).click()

    #-------------------------------------------------------------------------------------------------------------------

    items = (By.XPATH, "//*[@class='media-body']/a")

    def get_items(self):
        return self.driver.find_elements(*Basket.items).text

    #-------------------------------------------------------------------------------------------------------------------

    plusitem1 = (By.XPATH, "(//*[contains(@class,'plus qty')])[1]")

    def increase_item1_qty(self):
        self.driver.find_element(*Basket.plusitem1).click()
        sleep(8)

    #-------------------------------------------------------------------------------------------------------------------
    basket_items = (By.XPATH, "//div[@class='product']")

    def basket_items_list(self):
        return self.driver.find_elements(*Basket.basket_items)

    def basket_items_displayed(self):
        items = self.basket_items_list()
        basket_list = [item.text for item in items]
        return basket_list


