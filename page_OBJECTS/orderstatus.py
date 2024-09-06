from selenium.webdriver.common.by import By
from time import sleep

from page_OBJECTS.data import Data

class OrderStatus:

    def __init__(self, driver):
        self.driver = driver


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

    def backtoshopping_enabled(self):
        return self.driver.find_element(*OrderStatus.backtoshopping).is_enabled()

    #-------------------------------------------------------------------------------------------------------------------

    def switch_window_to_registerpage(self):
        handles = self.driver.window_handles
        newHandle = handles[1]
        self.driver.switch_to.window(newHandle)

    #-------------------------------------------------------------------------------------------------------------------

    register_btn = (By.XPATH, "//*[text()=' Create Cambridge account ']")

    def click_registerbutton(self):
        self.driver.find_element(*OrderStatus.register_btn).click()
        self.switch_window_to_registerpage()
        sleep(15)

    #-------------------------------------------------------------------------------------------------------------------

    legal = (By.XPATH, "//*[text()=' Legal ']")

    privacynotice = (By.XPATH, "//*[text()=' Privacy Notice ']")

    accessibilty = (By.XPATH, "//*[text()=' Accessibility ']")

    help = (By.XPATH, "//*[text()=' Help ']")

    def click_legal(self):
        return self.driver.find_element(*OrderStatus.legal).click()

    def click_privacynotice(self):
        self.driver.find_element(*OrderStatus.privacynotice).click()

    def click_accessibility(self):
        self.driver.find_element(*OrderStatus.accessibilty).click()

    def click_help(self):
        self.driver.find_element(*OrderStatus.help).click()

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

    checkdetailsandtryagain = (By.XPATH, "//*[contains(@class,'primary btn')]")

    def check_details_and_try_again(self):
        self.driver.find_element(*OrderStatus.checkdetailsandtryagain).click()
        sleep(25)

    #-------------------------------------------------------------------------------------------------------------------

    cart = (By.XPATH, "//*[contains(@class,'cart')]")

    def click_cart(self):
        self.driver.find_element(*OrderStatus.cart).click()
        sleep(25)

    #-------------------------------------------------------------------------------------------------------------------

    order_phrase1 = (By.XPATH, "//h1[@class='message-text']")

    def order_text1(self):
        text = self.driver.find_element(*OrderStatus.order_phrase1).text
        sleep(5)
        return text

    order_phrase2 = (By.XPATH, "//button[@class='btn purchase-receipt-title']")

    def order_text2(self):
        text = self.driver.find_element(*OrderStatus.order_phrase2).text
        sleep(5)
        return text

    #-------------------------------------------------------------------------------------------------------------------

    totalorder = (By.XPATH, "//p[@class='col-3 text-right m-0']/strong")

    def get_totalorder(self):
        text = self.driver.find_element(*OrderStatus.totalorder).text.strip()
        return text


    discount_row = (By.XPATH, "//div[@class='row order-discount my-3']")

    def check_discount_row_displayed(self):
        return self.driver.find_element(*OrderStatus.discount_row).is_displayed()

    #-------------------------------------------------------------------------------------------------------------------

    TT_B2FSS = (By.XPATH, "//*[@src='//assets.cambridge.org/97810090/03452/cover/9781009003452.jpg']")

    TT_C1ASS = (By.XPATH, "//*[@src='//assets.cambridge.org/97811089/91667/cover/9781108991667.jpg']")

    def get_TT_B2FSS(self):
        return self.driver.find_element(*OrderStatus.TT_B2FSS)

    def get_TT_C1ASS(self):
        return self.driver.find_element(*OrderStatus.TT_C1ASS)

    def click_TT_B2FSS(self):
        self.driver.find_element(*OrderStatus.TT_B2FSS).click()
        sleep(25)

    def click_TT_C1ASS(self):
        self.driver.find_element(*OrderStatus.TT_C1ASS).click()
        sleep(25)

    def verify_TT_B2FSS_is_accessible(self):

        main_window = self.driver.window_handles[0]
        self.click_TT_B2FSS()
        TT_B2FSS_window = self.driver.window_handles[1]
        self.driver.switch_to.window(TT_B2FSS_window)
        ss_path = ('C:\\Users\\jgabriel\OneDrive - Cambridge\\Documents\\GitHub\\Checkout_Regression\\saved_SCREENSHOTS'
                   '\\VERIFY_IF_TT_B2FSS_WINDOW_IS_DISPLAYED_WHEN_ACCESSED_THROUGH_THE_ORDER_STATUS_PAGE.png')
        self.driver.save_screenshot(ss_path)
        self.driver.close()
        self.driver.switch_to.window(main_window)

    def verify_TT_C1ASS_is_accessible(self):

        main_window = self.driver.window_handles[0]
        self.click_TT_C1ASS()
        TT_C1ASS_window = self.driver.window_handles[1]
        self.driver.switch_to.window(TT_C1ASS_window)
        ss_path = ('C:\\Users\\jgabriel\OneDrive - Cambridge\\Documents\\GitHub\\Checkout_Regression\\saved_SCREENSHOTS'
                   '\\VERIFY_IF_TT_C1ASS_WINDOW_IS_DISPLAYED_WHEN_ACCESSED_THROUGH_THE_ORDER_STATUS_PAGE.png')
        self.driver.save_screenshot(ss_path)
        self.driver.close()
        self.driver.switch_to.window(main_window)

    #-------------------------------------------------------------------------------------------------------------------

    
