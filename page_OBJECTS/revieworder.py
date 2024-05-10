from selenium.webdriver.common.by import By
from time import sleep

from page_OBJECTS.data import Data

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

    def input_amex_challenge_cardnumber(self):
        return self.driver.find_element(*ReviewOrder.cardnumber).send_keys("3400 000000 02534")
        sleep(5)

    def input_mastercard_challenge_cardnumber(self):
        return self.driver.find_element(*ReviewOrder.cardnumber).send_keys("5200 0000 0000 2151")
        sleep(5)

    def input_visa_challenge_cardnumber(self):
        return self.driver.find_element(*ReviewOrder.cardnumber).send_keys("4456 5300 0000 1096")
        sleep(5)

    def input_failed_challenge_cardnumber(self):
        return self.driver.find_element(*ReviewOrder.cardnumber).send_keys("4456 5300 0000 1104")
        sleep(5)

    def input_amex_frictionless_cardnumber(self):
        return self.driver.find_element(*ReviewOrder.cardnumber).send_keys("3400 000000 02708")
        sleep(5)

    def input_mastercard_frictionless_cardnumber(self):
        return self.driver.find_element(*ReviewOrder.cardnumber).send_keys("5200 0000 0000 2235")
        sleep(5)

    def input_visa_frictionless_cardnumber(self):
        return self.driver.find_element(*ReviewOrder.cardnumber).send_keys("4456 5300 0000 1005")
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

    def input_amex_securitycode(self):
        return self.driver.find_element(*ReviewOrder.securitycode).send_keys("1235")
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

    def pay_via_amex_challenge_card(self):
        self.click_card()
        self.driver.switch_to.frame(self.cardnumber_frame())
        self.input_amex_challenge_cardnumber()
        self.driver.switch_to.default_content()
        self.input_expirymonth()
        self.input_expiryyear()
        self.driver.switch_to.frame(self.securitycode_frame())
        self.input_amex_securitycode()
        self.driver.switch_to.default_content()
        self.click_paynow()

    def pay_via_mastercard_challenge_card(self):
        self.click_card()
        self.driver.switch_to.frame(self.cardnumber_frame())
        self.input_mastercard_challenge_cardnumber()
        self.driver.switch_to.default_content()
        self.input_expirymonth()
        self.input_expiryyear()
        self.driver.switch_to.frame(self.securitycode_frame())
        self.input_securitycode()
        self.driver.switch_to.default_content()
        self.click_paynow()

    def pay_via_visa_challenge_card(self):
        self.click_card()
        self.driver.switch_to.frame(self.cardnumber_frame())
        self.input_visa_challenge_cardnumber()
        self.driver.switch_to.default_content()
        self.input_expirymonth()
        self.input_expiryyear()
        self.driver.switch_to.frame(self.securitycode_frame())
        self.input_securitycode()
        self.driver.switch_to.default_content()
        self.click_paynow()

    def pay_via_failed_challenge_card(self):
        self.click_card()
        self.driver.switch_to.frame(self.cardnumber_frame())
        self.input_failed_challenge_cardnumber()
        self.driver.switch_to.default_content()
        self.input_expirymonth()
        self.input_expiryyear()
        self.driver.switch_to.frame(self.securitycode_frame())
        self.input_securitycode()
        self.driver.switch_to.default_content()
        self.click_paynow()

    def pay_via_amex_frictionless_card(self):
        self.click_card()
        self.driver.switch_to.frame(self.cardnumber_frame())
        self.input_amex_frictionless_cardnumber()
        self.driver.switch_to.default_content()
        self.input_expirymonth()
        self.input_expiryyear()
        self.driver.switch_to.frame(self.securitycode_frame())
        self.input_amex_securitycode()
        self.driver.switch_to.default_content()
        self.click_paynow()

    def pay_via_mastercard_frictionless_card(self):
        self.click_card()
        self.driver.switch_to.frame(self.cardnumber_frame())
        self.input_mastercard_frictionless_cardnumber()
        self.driver.switch_to.default_content()
        self.input_expirymonth()
        self.input_expiryyear()
        self.driver.switch_to.frame(self.securitycode_frame())
        self.input_securitycode()
        self.driver.switch_to.default_content()
        self.click_paynow()

    def pay_via_visa_frictionless_card(self):
        self.click_card()
        self.driver.switch_to.frame(self.cardnumber_frame())
        self.input_visa_frictionless_cardnumber()
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



# ---------------------------------------------------------------------------------------------------------------------
#     checkout_price1 = (By.XPATH, "(//*[contains(@class, 'price-wrapper')])[1]")
#     checkout_total = (By.XPATH, "(//*[contains(@class, 'm-0')]/strong)[1]")
#
#     def check_checkout_itemcurrency(self):
#         currency_text = self.driver.find_element(*ReviewOrder.checkout_price1).text
#         currency_str = currency_text.replace("\n", "")
#         return currency_str
#
#     def check_checkout_totalcurrency(self):
#         currency_text = self.driver.find_element(*ReviewOrder.checkout_price1).text
#         currency_str = currency_text.replace("\n", "")
#         return currency_str

    #-------------------------------------------------------------------------------------------------------------------

    itemprice1 = (By.XPATH, "//*[contains(@class,'price')]")

    def get_itemprice1_with_whitespace(self):
        return self.driver.find_element(*ReviewOrder.itemprice1).text.replace(" \n", " ")

    def get_itemprice1_without_whitespace(self):
        return self.driver.find_element(*ReviewOrder.itemprice1).text.strip()

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

    subtotal = (By.XPATH, "(//*[contains(@class,'order-description')])[1]/p[2]")

    def get_subtotal_with_whitespace(self):
        return self.driver.find_element(*ReviewOrder.subtotal).text.replace(" \n", " ")

    def get_subtotal_without_whitespace(self):
        return self.driver.find_element(*ReviewOrder.subtotal).text.strip()

    def get_aud_subtotal(self):
        return self.get_subtotal_with_whitespace()

    def get_cad_subtotal(self):
        return self.get_subtotal_with_whitespace()

    def get_eur_subtotal(self):
        return self.get_subtotal_without_whitespace()

    def get_eur_c_subtotal(self):
        return self.get_subtotal_without_whitespace()

    def get_eur_i_subtotal(self):
        return self.get_subtotal_without_whitespace()

    def get_gbp_subtotal(self):
        return self.get_subtotal_without_whitespace()

    def get_nzd_subtotal(self):
        return self.get_subtotal_with_whitespace()

    def get_usd_subtotal(self):
        return self.get_subtotal_with_whitespace()

    def get_usd_e_subtotal(self):
        return self.get_subtotal_with_whitespace()

    def get_usd_n_subtotal(self):
        return self.get_subtotal_with_whitespace()

    #-------------------------------------------------------------------------------------------------------------------

    ordertotal = (By.XPATH, "(//*[contains(@class,'order-description')])[2]/p[2]")

    def get_ordertotal_with_whitespace(self):
        return self.driver.find_element(*ReviewOrder.ordertotal).text.replace(" \n", " ")

    def get_ordertotal_without_whitespace(self):
        return self.driver.find_element(*ReviewOrder.ordertotal).text.strip()

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
        self.driver.find_element(*ReviewOrder.backtoshopping).click()
        sleep(25)

    def backtoshopping_enabled(self):
        return self.driver.find_element(*ReviewOrder.backtoshopping).is_enabled()

    #-------------------------------------------------------------------------------------------------------------------

    continueshopping = (By.XPATH, "//*[text()=' Continue shopping ']")

    def click_continueshopping(self):
        self.driver.find_element(*ReviewOrder.continueshopping).click()
        sleep(25)

    def continueshopping_enabled(self):
        return self.driver.find_element(*ReviewOrder.continueshopping).is_enabled()

    #-------------------------------------------------------------------------------------------------------------------

    chevron = (By.XPATH, "//*[contains(@class,'chevron')]")

    def click_chevron(self):
        self.driver.find_element(*ReviewOrder.chevron).click()
        sleep(25)

    def chevron_enabled(self):
        return self.driver.find_element(*ReviewOrder.chevron).is_enabled()

    #-------------------------------------------------------------------------------------------------------------------

    deleteitem1 = (By.XPATH, "(//*[contains(@class,'basket-delete')])[1]")

    deleteitem2 = (By.XPATH, "(//*[contains(@class,'basket-delete')])[2]")

    def delete_item1(self):
        self.driver.find_element(*ReviewOrder.deleteitem1).click()
        sleep(8)

    def delete_item2(self):
        self.driver.find_element(*ReviewOrder.deleteitem2).click()
        sleep(8)

    #-------------------------------------------------------------------------------------------------------------------

    undoitem1 = (By.XPATH, "(//*[text()=' Undo '])[1]")

    def undo_item1(self):
        self.driver.find_element(*ReviewOrder.undoitem1).click()
        sleep(8)

    #-------------------------------------------------------------------------------------------------------------------

    plusitem1 = (By.XPATH, "(//*[contains(@class,'plus qty')])[1]")

    def increase_item1_qty(self):
        self.driver.find_element(*ReviewOrder.plusitem1).click()
        sleep(8)

    #-------------------------------------------------------------------------------------------------------------------

    qtyitem1 = (By.XPATH, "(//*[contains(@id,'qty-input')])[1]")

    def get_item1_qty(self):
        self.driver.find_element(*ReviewOrder.qtyitem1).click()

    #-------------------------------------------------------------------------------------------------------------------

    edit_address_btn = (By.XPATH, "//button[contains(@class, 'edit-address')]")

    def click_edit_address(self):
        self.driver.find_element(*ReviewOrder.edit_address_btn).click()
        sleep(10)

    #-------------------------------------------------------------------------------------------------------------------

    def page_src(self):
        body = self.driver.find_element(By.TAG_NAME, 'body').text
        return body

    #-------------------------------------------------------------------------------------------------------------------

    country = (By.XPATH, "//*[@id='country']")

    def check_country_value(self):
        value = self.driver.find_element(*ReviewOrder.country).get_attribute("value")
        return value

    #-------------------------------------------------------------------------------------------------------------------

    legal         = (By.XPATH, "//*[text()=' Legal ']")

    privacynotice = (By.XPATH, "//*[text()=' Privacy Notice ']")

    accessibilty  = (By.XPATH, "//*[text()=' Accessibility ']")

    help          = (By.XPATH, "//*[text()=' Help ']")

    def click_legal(self):
        return self.driver.find_element(*ReviewOrder.legal).click()

    def click_privacynotice(self):
        self.driver.find_element(*ReviewOrder.privacynotice).click()

    def click_accessibility(self):
        self.driver.find_element(*ReviewOrder.accessibilty).click()

    def click_help(self):
        self.driver.find_element(*ReviewOrder.help).click()

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
