from selenium.webdriver.common.by import By
from time import sleep

from page_OBJECTS.data import Data

class Basket:

    def __init__(self, driver):
        self.driver = driver

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
        return self.driver.find_element(*Basket.itemprice1).text.replace("\n","")

    def get_itemprice1_without_whitespace(self):
        return self.driver.find_element(*Basket.itemprice1).text.strip()

    def get_aud_TT_B2FSS_price(self):
        return self.get_itemprice1_with_whitespace()

    def get_cad_TT_B2FSS_price(self):
        return self.get_itemprice1_with_whitespace()

    def get_eur_TT_B2FSS_price(self):
        return self.get_itemprice1_without_whitespace()

    def get_eur_c_SF_L1DSB_price(self):
        return self.get_itemprice1_without_whitespace()

    def get_eur_i_SF_L1DSB_price(self):
        return self.get_itemprice1_without_whitespace()

    def get_gbp_TT_B2FSS_price(self):
        return self.get_itemprice1_without_whitespace()

    def get_nzd_TT_B2FSS_price(self):
        return self.get_itemprice1_with_whitespace()

    def get_usd_TT_B2FSS_price(self):
        return self.get_itemprice1_with_whitespace()

    def get_usd_e_SF_L1DSB_price(self):
        return self.get_itemprice1_with_whitespace()

    def get_usd_n_SF_L1DSB_price(self):
        return self.get_itemprice1_with_whitespace()

    #-------------------------------------------------------------------------------------------------------------------

    ordertotal = (By.XPATH, "(//*[contains(@class,'basket-description')]/p[2])[1]")

    def get_ordertotal_with_whitespace(self):
        return self.driver.find_element(*Basket.ordertotal).text.replace(" \n", " ")

    def get_ordertotal_without_whitespace(self):
        return self.driver.find_element(*Basket.ordertotal).text.strip()

    def get_aud_subtotal(self):
        return self.get_ordertotal_with_whitespace()

    def get_cad_subtotal(self):
        return self.get_ordertotal_with_whitespace()

    def get_eur_subtotal(self):
        return self.get_ordertotal_without_whitespace()

    def get_eur_c_subtotal(self):
        return self.get_ordertotal_without_whitespace()

    def get_eur_i_subtotal(self):
        return self.get_ordertotal_without_whitespace()

    def get_gbp_subtotal(self):
        return self.get_ordertotal_without_whitespace()

    def get_nzd_subtotal(self):
        return self.get_ordertotal_with_whitespace()

    def get_usd_subtotal(self):
        return self.get_ordertotal_with_whitespace()

    def get_usd_e_subtotal(self):
        return self.get_ordertotal_with_whitespace()

    def get_usd_n_subtotal(self):
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

    xitem1 = (By.XPATH, "(//*[contains(@class,'close')])[1]")

    xitem2 = (By.XPATH, "(//*[contains(@class,'close')])[2]")

    xitem3 = (By.XPATH, "(//*[contains(@class,'close')])[3]")

    def x_item1(self):
        self.driver.find_element(*Basket.xitem1).click()
        sleep(2)

    def x_item2(self):
        self.driver.find_element(*Basket.xitem2).click()
        sleep(2)

    def x_item3(self):
        self.driver.find_element(*Basket.xitem3).click()
        sleep(2)

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
    # basket_product = (By.XPATH, "//div[@class='product']")
    #
    # def basket_products_list(self):
    #     return self.driver.find_elements(*Basket.basket_product)
    #
    # def basket_items_displayed(self):
    #     products = self.basket_products_list()
    #     basket_list = [product.text for product in products]
    #     return basket_list

    def basket_items(self):
       return self.driver.find_elements(*Basket.items)

    def basket_items_set(self):
        sleep(5)
        basket_items = [item.text for item in self.basket_items()]
        print("\nNumber of items in Review order page:", len(basket_items))
        print("List of items in Review order page:", basket_items)
        return basket_items

    def get_basket_items(self):
        basket_items = [item.text for item in self.basket_items()]
        return basket_items

    #-------------------------------------------------------------------------------------------------------------------

    legal         = (By.XPATH, "//*[text()=' Legal ']")

    privacynotice = (By.XPATH, "//*[text()=' Privacy Notice ']")

    accessibilty  = (By.XPATH, "//*[text()=' Accessibility ']")

    help          = (By.XPATH, "//*[text()=' Help ']")

    def click_legal(self):
        return self.driver.find_element(*Basket.legal).click()

    def click_privacynotice(self):
        self.driver.find_element(*Basket.privacynotice).click()

    def click_accessibility(self):
        self.driver.find_element(*Basket.accessibilty).click()

    def click_help(self):
        self.driver.find_element(*Basket.help).click()

    def verify_footers_are_accessible(self):

        i = Data(self.driver)

        main_window = self.driver.window_handles[0]

        self.click_legal()
        sleep(25)
        legal_window = self.driver.window_handles[1]
        self.driver.switch_to.window(legal_window)
        assert i.legal_title == self.driver.title
        self.driver.close()

        self.driver.switch_to.window(main_window)

        self.click_privacynotice()
        sleep(25)
        privacynotice_window = self.driver.window_handles[1]
        self.driver.switch_to.window(privacynotice_window)
        assert i.privacynotice_title == self.driver.title
        self.driver.close()

        self.driver.switch_to.window(main_window)

        self.click_accessibility()
        sleep(25)
        accessibility_window = self.driver.window_handles[1]
        self.driver.switch_to.window(accessibility_window)
        assert i.accessibility_title == self.driver.title
        self.driver.close()

        self.driver.switch_to.window(main_window)

        self.click_help()
        sleep(25)
        help_window = self.driver.window_handles[1]
        self.driver.switch_to.window(help_window)
        assert i.help_title == self.driver.title
        self.driver.close()

        self.driver.switch_to.window(main_window)

    #-------------------------------------------------------------------------------------------------------------------

    cart = (By.XPATH, "//*[contains(@class,'cart')]")

    def click_cart(self):
        self.driver.find_element(*Basket.cart).click()
        sleep(25)

    #-------------------------------------------------------------------------------------------------------------------

    TT_B2FSS = (By.XPATH, "//*[@src='//assets.cambridge.org/97810090/03452/cover/9781009003452.jpg' and @class='product__image']")

    TT_C1ASS = (By.XPATH, "//*[@src='//assets.cambridge.org/97811089/91667/cover/9781108991667.jpg' and @class='product__image']")

    def get_TT_B2FSS(self):
        return self.driver.find_element(*Basket.TT_B2FSS)

    def get_TT_C1ASS(self):
        return self.driver.find_element(*Basket.TT_C1ASS)

    def click_TT_B2FSS(self):
        self.driver.find_element(*Basket.TT_B2FSS).click()
        sleep(25)

    def click_TT_C1ASS(self):
        self.driver.find_element(*Basket.TT_C1ASS).click()
        sleep(25)

    def verify_TT_B2FSS_is_accessible(self):

        main_window = self.driver.window_handles[0]
        self.click_TT_B2FSS()
        TT_B2FSS_window = self.driver.window_handles[1]
        self.driver.switch_to.window(TT_B2FSS_window)
        ss_path = ('C:\\Users\\jgabriel\OneDrive - Cambridge\\Documents\\GitHub\\Checkout_Regression\\saved_SCREENSHOTS'
                   '\\VERIFY_IF_TT_B2FSS_WINDOW_IS_DISPLAYED_WHEN_ACCESSED_THROUGH_THE_BASKET_PAGE.png')
        self.driver.save_screenshot(ss_path)
        self.driver.close()
        self.driver.switch_to.window(main_window)

    def verify_TT_C1ASS_is_accessible(self):

        main_window = self.driver.window_handles[0]
        self.click_TT_C1ASS()
        TT_C1ASS_window = self.driver.window_handles[1]
        self.driver.switch_to.window(TT_C1ASS_window)
        ss_path = ('C:\\Users\\jgabriel\OneDrive - Cambridge\\Documents\\GitHub\\Checkout_Regression\\saved_SCREENSHOTS'
                   '\\VERIFY_IF_TT_C1ASS_WINDOW_IS_DISPLAYED_WHEN_ACCESSED_THROUGH_THE_BASKET_PAGE.png')
        self.driver.save_screenshot(ss_path)
        self.driver.close()
        self.driver.switch_to.window(main_window)

    #-------------------------------------------------------------------------------------------------------------------

    # SFL = SAVE FOR LATER

    # PC = PRODUCT CARD

    # YI = YOUR ITEMS

    # SFLI = SAVE FOR LATER ITEMS

    # PC = PRODUCT CARD

    TT_B2FSS_SFL       = (By.XPATH, "//*[@class='product'][contains(.,'B2')]//*[contains(text(),'Save for later')]")

    TT_B2FSS_MTB       = (By.XPATH, "//*[@id='collapseBookmarkedItems']//*[@class='product'][contains(.,'B2')]//*[contains(@title,'Move to basket')]")

    YI_TT_B2FSS_DEL    = (By.XPATH, "//*[@id='collapseBasketItems']//*[@class='product'][contains(.,'B2')]//*[contains(@title,'Remove')]")

    YI_TT_B2FSS_PC     = (By.XPATH, "//*[@id='collapseBasketItems']//*[@class='product'][contains(.,'B2')]")

    SFLI_TT_B2FSS_PC   = (By.XPATH, "//*[@id='collapseBookmarkedItems']//*[@class='product'][contains(.,'B2')]")

    SFLI_TT_B2FSS_DEL  = (By.XPATH, "//*[@id='collapseBookmarkedItems']//*[@class='product'][contains(.,'B2')]//*[contains(@title,'Remove')]")

    TT_B2FSS_DEC       = (By.XPATH, "//*[@class='product'][contains(.,'B2')]//*[contains(@class,'subtract')]")

    TT_B2FSS_INC       = (By.XPATH, "//*[@class='product'][contains(.,'B2')]//*[contains(@class,'plus')]")

    TT_B2FSS_PRICE     = (By.XPATH, "//*[@class='product'][contains(.,'B2')]//*[contains(@class,'price')]/strong")

    def verify_YI_TT_B2FSS_is_displayed(self):
        return self.driver.find_element(*Basket.YI_TT_B2FSS_PC).is_displayed()

    def verify_SFLI_TT_B2FSS_is_displayed(self):
        return self.driver.find_element(*Basket.SFLI_TT_B2FSS_PC).is_displayed()

    def saveforlater_TT_B2FSS(self):
        self.driver.find_element(*Basket.TT_B2FSS_SFL).click()
        sleep(8)

    def movetobasket_TT_B2FSS(self):
        self.driver.find_element(*Basket.TT_B2FSS_MTB).click()
        sleep(8)

    def YI_delete_TT_B2FSS(self):
        self.driver.find_element(*Basket.YI_TT_B2FSS_DEL).click()
        sleep(8)

    def SFLI_delete_TT_B2FSS(self):
        self.driver.find_element(*Basket.SFLI_TT_B2FSS_DEL).click()
        sleep(8)

    def decrease_TT_B2FSS(self):
        self.driver.find_element(*Basket.TT_B2FSS_DEC).click()
        sleep(8)

    def increase_TT_B2FSS(self):
        self.driver.find_element(*Basket.TT_B2FSS_INC).click()
        sleep(8)

    def get_TT_B2FSS_price(self):
        return self.driver.find_element(*Basket.TT_B2FSS_PRICE).text

    TT_C1ASS_SFL       = (By.XPATH, "//*[@class='product'][contains(.,'C1')]//*[contains(text(),'Save for later')]")

    TT_C1ASS_MTB       = (By.XPATH,"//*[@id='collapseBookmarkedItems']//*[@class='product'][contains(.,'C1')]//*[contains(@title,'Move to basket')]")

    YI_TT_C1ASS_DEL    = (By.XPATH, "//*[@id='collapseBasketItems']//*[@class='product'][contains(.,'C1')]//*[contains(@title,'Remove')]")

    YI_TT_C1ASS_PC     = (By.XPATH, "//*[@id='collapseBasketItems']//*[@class='product'][contains(.,'C1')]")

    SFLI_TT_C1ASS_PC   = (By.XPATH, "//*[@id='collapseBookmarkedItems']//*[@class='product'][contains(.,'C1')]")

    SFLI_TT_C1ASS_DEL  = (By.XPATH, "//*[@id='collapseBookmarkedItems']//*[@class='product'][contains(.,'C1')]//*[contains(@title,'Remove')]")

    TT_C1ASS_DEC       = (By.XPATH, "//*[@class='product'][contains(.,'C1')]//*[contains(@class,'subtract')]")

    TT_C1ASS_INC       = (By.XPATH, "//*[@class='product'][contains(.,'C1')]//*[contains(@class,'plus')]")

    TT_C1ASS_PRICE     = (By.XPATH, "//*[@class='product'][contains(.,'C1')]//*[contains(@class,'price')]/strong")

    def verify_YI_TT_C1ASS_is_displayed(self):
        return self.driver.find_element(*Basket.YI_TT_C1ASS_PC).is_displayed()

    def verify_SFLI_TT_C1ASS_is_displayed(self):
        return self.driver.find_element(*Basket.SFLI_TT_C1ASS_PC).is_displayed()

    def saveforlater_TT_C1ASS(self):
        self.driver.find_element(*Basket.TT_C1ASS_SFL).click()
        sleep(8)

    def movetobasket_TT_C1ASS(self):
        self.driver.find_element(*Basket.TT_C1ASS_MTB).click()
        sleep(8)

    def YI_delete_TT_C1ASS(self):
        self.driver.find_element(*Basket.YI_TT_C1ASS_DEL).click()
        sleep(8)

    def SFLI_delete_TT_C1ASS(self):
        self.driver.find_element(*Basket.SFLI_TT_C1ASS_DEL).click()
        sleep(8)

    def decrease_TT_C1ASS(self):
        self.driver.find_element(*Basket.TT_C1ASS_DEC).click()
        sleep(8)

    def increase_TT_C1ASS(self):
        self.driver.find_element(*Basket.TT_C1ASS_INC).click()
        sleep(8)

    def get_TT_C1ASS_price(self):
        return self.driver.find_element(*Basket.TT_C1ASS_PRICE).text

    TT_A2KSSS_SFL      = (By.XPATH, "//*[@class='product'][contains(.,'A2')]//*[contains(text(),'Save for later')]")

    TT_A2KSSS_MTB      = (By.XPATH,"//*[@id='collapseBookmarkedItems']//*[@class='product'][contains(.,'A2')]//*[contains(@title,'Move to basket')]")

    YI_TT_A2KSSS_DEL   = (By.XPATH, "//*[@id='collapseBasketItems']//*[@class='product'][contains(.,'A2')]//*[contains(@title,'Remove')]")

    YI_TT_A2KSSS_PC    = (By.XPATH, "//*[@id='collapseBasketItems']//*[@class='product'][contains(.,'A2')]")

    SFLI_TT_A2KSSS_PC  = (By.XPATH, "//*[@id='collapseBookmarkedItems']//*[@class='product'][contains(.,'A2')]")

    SFLI_TT_A2KSSS_DEL = (By.XPATH, "//*[@id='collapseBookmarkedItems']//*[@class='product'][contains(.,'A2')]//*[contains(@title,'Remove')]")

    TT_A2KSSS_DEC      = (By.XPATH, "//*[@class='product'][contains(.,'A2')]//*[contains(@class,'subtract')]")

    TT_A2KSSS_INC      = (By.XPATH, "//*[@class='product'][contains(.,'A2')]//*[contains(@class,'plus')]")

    TT_A2KSSS_PRICE    = (By.XPATH, "//*[@class='product'][contains(.,'A2')]//*[contains(@class,'price')]/strong")

    def verify_YI_TT_A2KSSS_is_displayed(self):
        return self.driver.find_element(*Basket.YI_TT_A2KSSS_PC).is_displayed()

    def verify_SFLI_TT_A2KSSS_is_displayed(self):
        return self.driver.find_element(*Basket.SFLI_TT_A2KSSS_PC).is_displayed()

    def saveforlater_TT_A2KSSS(self):
        self.driver.find_element(*Basket.TT_A2KSSS_SFL).click()
        sleep(8)

    def movetobasket_TT_A2KSSS(self):
        self.driver.find_element(*Basket.TT_A2KSSS_MTB).click()
        sleep(8)

    def YI_delete_TT_A2KSSS(self):
        self.driver.find_element(*Basket.YI_TT_A2KSSS_DEL).click()
        sleep(8)

    def SFLI_delete_TT_A2KSSS(self):
        self.driver.find_element(*Basket.SFLI_TT_A2KSSS_DEL).click()
        sleep(8)

    def decrease_TT_A2KSSS(self):
        self.driver.find_element(*Basket.TT_A2KSSS_DEC).click()
        sleep(8)

    def increase_TT_A2KSSS(self):
        self.driver.find_element(*Basket.TT_A2KSSS_INC).click()
        sleep(8)

    def get_TT_A2KSSS_price(self):
        return self.driver.find_element(*Basket.TT_A2KSSS_PRICE).text

    # TEST PRODUCT 1

    YI_TP1_PC  = (By.XPATH, "//*[@id='collapseBasketItems']//*[@class='product'][contains(.,'Test Product 1')]")

    TP1_DEC    = (By.XPATH, "//*[@class='product'][contains(.,'Test Product 1')]//*[contains(@class,'subtract')]")

    TP1_INC    = (By.XPATH, "//*[@class='product'][contains(.,'Test Product 1')]//*[contains(@class,'plus')]")

    TP1_QTY    = (By.XPATH, "//*[@class='product'][contains(.,'Test Product 1')]//*[contains(@id,'qty')]")

    YI_TP1_DEL = (By.XPATH, "//*[@id='collapseBasketItems']//*[@class='product'][contains(.,'Test Product 1')]//*[contains(@title,'Remove')]")

    TP1_SFL    = (By.XPATH, "//*[@class='product'][contains(.,'Test Product 1')]//*[contains(text(),'Save for later')]")

    TP1_MTB    = (By.XPATH, "//*[@id='collapseBookmarkedItems']//*[@class='product'][contains(.,'Test Product 1')]//*[contains(@title,'Move to basket')]")

    def verify_YI_TP1_is_displayed(self):
        return self.driver.find_element(*Basket.YI_TP1_PC).is_displayed()

    def decrease_TP1(self):
        self.driver.find_element(*Basket.TP1_DEC).click()
        sleep(8)

    def verify_decrease_TP1_is_enabled(self):
        return self.driver.find_element(*Basket.TP1_DEC).is_enabled()

    def increase_TP1(self):
        self.driver.find_element(*Basket.TP1_INC).click()
        sleep(8)

    def verify_increase_TP1_is_enabled(self):
        return self.driver.find_element(*Basket.TP1_INC).is_enabled()

    def get_TP1_qty(self):
        return self.driver.find_element(*Basket.TP1_QTY).get_attribute('value')

    def YI_delete_TP1(self):
        self.driver.find_element(*Basket.YI_TP1_DEL).click()
        sleep(8)

    def saveforlater_TP1(self):
        self.driver.find_element(*Basket.TP1_SFL).click()
        sleep(8)

    def movetobasket_TP1(self):
        self.driver.find_element(*Basket.TP1_MTB).click()
        sleep(8)

    def verify_TP1_increments_by_1(self):

        initial_qty = self.get_TP1_qty()

        for i in range(4):
            self.increase_TP1()
            new_qty = int(initial_qty) + i + 1
            assert self.get_TP1_qty()                    == str(new_qty)
            assert self.verify_decrease_TP1_is_enabled() == True
            assert self.your_items_total()               == self.get_cart_total() in self.get_your_items_total()
            assert self.subtotal()                       == self.get_subtotal()

    def verify_TP1_decrements_by_1(self):

        initial_qty = self.get_TP1_qty()

        for i in range(4):
            self.decrease_TP1()
            new_qty = int(initial_qty) - i - 1
            assert self.get_TP1_qty()                    == str(new_qty)
            assert self.verify_increase_TP1_is_enabled() == True
            assert self.your_items_total()               == self.get_cart_total() in self.get_your_items_total()
            assert self.subtotal()                       == self.get_subtotal()

    def verify_TP1_qty_remains_unchanged_when_deleted_and_undone(self):
        before_delete_qty = self.get_TP1_qty()
        self.YI_delete_TP1()
        self.undo_item1()
        assert before_delete_qty == self.get_TP1_qty()

    def verify_TP1_qty_remains_unchanged_when_saved_for_later_and_moved_to_basket(self):
        before_saved_for_later_qty = self.get_TP1_qty()
        self.saveforlater_TP1()
        self.movetobasket_TP1()
        assert before_saved_for_later_qty == self.get_TP1_qty()

    #-------------------------------------------------------------------------------------------------------------------

    YI_price = (By.XPATH, "//*[@id='collapseBasketItems']//*[contains(@class,'price')]/strong")

    def get_YI_price(self):
        return self.driver.find_elements(*Basket.YI_price)

    def order_total(self):

        prices = [float(price.text.strip('£')) for price in self.get_YI_price()]

        a = sum(prices)
        b = format(a,'.2f')
        c = str(b)

        d = '£' + c

        return d

    def subtotal(self):

        prices = [float(price.text.strip('£')) for price in self.get_YI_price()]

        a = sum(prices)
        b = format(a,'.2f')
        c = str(b)

        d = '£' + c

        return d

    #-------------------------------------------------------------------------------------------------------------------

    Y_items    = (By.XPATH, "//*[@id='collapseBasketItems']//*[@class='product']//*[contains(@id,'qty-input')]")

    SFL_items  = (By.XPATH, "//*[@id='collapseBookmarkedItems']//*[@class='product']")

    SFL_header = (By.XPATH, "//*[@data-target='#collapseBookmarkedItems']")

    YI_header  = (By.XPATH, "//*[@data-target='#collapseBasketItems']")

    itemtotal  = (By.XPATH, "(//*[@class='basket-summary']//*[contains(text(),'Total')])[1]")

    def saveforlater_items(self):
        return self.driver.find_elements(*Basket.SFL_items)

    def save_for_later_items(self):

        saveforlateritems = len(self.saveforlater_items())

        a = str(saveforlateritems)

        return a

    def get_save_for_later_items(self):
        return self.driver.find_element(*Basket.SFL_header).text

    def verify_save_for_later_items_is_displayed(self):
        return self.driver.find_element(*Basket.SFL_header).is_displayed()

    def verify_your_items_is_displayed(self):
        return self.driver.find_element(*Basket.YI_header).is_displayed()

    def your_items(self):
        return self.driver.find_elements(*Basket.Y_items)

    def your_items_total(self):

        items = [int(item.get_attribute('value')) for item in self.your_items()]

        a = sum(items)
        b = str(a)

        return b

    def get_your_items_total(self):
        return self.driver.find_element(*Basket.itemtotal).text

    #-------------------------------------------------------------------------------------------------------------------

    cart_total = (By.XPATH, "//*[contains(@class,'oval')]/span")

    def get_cart_total(self):
        return self.driver.find_element(*Basket.cart_total).text

    #-------------------------------------------------------------------------------------------------------------------

    ordersummary = (By.XPATH, "//*[@class='basket-summary']")

    emptybasket = (By.XPATH, "//*[contains(@class,'empty-basket')]")

    def verify_order_summary_is_displayed(self):
        return self.driver.find_element(*Basket.ordersummary).is_displayed()

    def verify_empty_basket_is_displayed(self):
        return self.driver.find_element(*Basket.emptybasket).is_displayed()

    def page_src(self):
        body = self.driver.find_element(By.TAG_NAME, 'body').text
        return body

    #-------------------------------------------------------------------------------------------------------------------

    item1removed = (By.XPATH, "(//*[@class='undo'])[1]")

    item2removed = (By.XPATH, "(//*[@class='undo'])[2]")

    item3removed = (By.XPATH, "(//*[@class='undo'])[3]")

    def verify_item1_removed_is_displayed(self):
        return self.driver.find_element(*Basket.item1removed).is_displayed()

    def verify_item2_removed_is_displayed(self):
        return self.driver.find_element(*Basket.item2removed).is_displayed()

    def verify_item3_removed_is_displayed(self):
        return self.driver.find_element(*Basket.item3removed).is_displayed()

    #-------------------------------------------------------------------------------------------------------------------

    maximumqtylimitmodal = (By.XPATH, "//*[@class='popover-body']//*[contains(text(),'maximum quantity')]")

    taxinclusivemodal    = (By.XPATH, "//*[@class='popover-body']//*[contains(text(),'tax due is already included')]")

    def maximum_qty_limit_modal_is_displayed(self):
        return self.driver.find_element(*Basket.maximumqtylimitmodal).is_displayed()

    def click_maximum_qty_limit_modal(self):
        return self.driver.find_element(*Basket.maximumqtylimitmodal).click()

    def verify_maximum_qty_limit_is_displayed(self):
        assert self.maximum_qty_limit_modal_is_displayed() == True
        self.click_maximum_qty_limit_modal()

    def verify_tax_inclusive_modal_is_displayed(self):
        return self.driver.find_element(*Basket.taxinclusivemodal).is_displayed()

    #-------------------------------------------------------------------------------------------------------------------

    getsubtotal = (By.XPATH, "(//*[contains(@class,'sub-total')])[1]/p/strong")

    def get_subtotal(self):
        return self.driver.find_element(*Basket.getsubtotal).text

    #-------------------------------------------------------------------------------------------------------------------

    bp1qty = (By.XPATH, "//*[@class='product'][contains(.,'Bookable Product 1')]//*[contains(@id,'qty')]")

    def get_BP1_qty(self):
        return self.driver.find_element(*Basket.bp1qty).get_attribute('value')



    price_label = (By.XPATH, "//div[contains(@class, 'price-wrapper')]")

    def gratis_label_check(self):
        text = self.driver.find_element(*Basket.price_label).text
        return text