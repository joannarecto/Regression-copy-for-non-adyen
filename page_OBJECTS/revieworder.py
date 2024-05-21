from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException

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
    #qa
    edit_address_btn = (By.XPATH, "//button[contains(@class, 'edit-address')]")

    #staging
    # edit_address_btn = (By.XPATH, "//a[@class='edit-address']")

    def click_edit_address(self):
        self.driver.find_element(*ReviewOrder.edit_address_btn).click()
        sleep(5)

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

    cart = (By.XPATH, "//*[contains(@class,'cart')]")

    def click_cart(self):
        self.driver.find_element(*ReviewOrder.cart).click()
        sleep(25)

    #-------------------------------------------------------------------------------------------------------------------

    checkbox_coupon = (By.XPATH, "//div[@class='custom-control custom-checkbox mb-0']")

    input_coupon = (By.XPATH, "//*[@id='discount_input']")

    button_coupon = (By.XPATH, "//button[text()=' Use code ']")

    remove_coupon = (By.XPATH, "(//button[@class='btn btn-icon'])[2]")

    def tick_discountcode(self):
        self.driver.find_element(*ReviewOrder.checkbox_coupon).click()
        sleep(3)

    def enter_discountcode(self):
        self.driver.find_element(*ReviewOrder.input_coupon).send_keys('TC599AC1')
        sleep(3)

    def click_discountcode_btn(self):
        self.driver.find_element(*ReviewOrder.button_coupon).click()
        sleep(5)

    def remove_discountcode(self):
        self.driver.find_element(*ReviewOrder.remove_coupon).click()
        sleep(5)

    def use_discountcode(self):
        self.tick_discountcode()
        self.enter_discountcode()
        self.click_discountcode_btn()


    discount_fields = (By.XPATH, "(//div[@data-v-4bf493bc=''])[5]")

    discount_ordertotals_field = (By.XPATH, "//div[@class='order-description sub-total order-discount']")

    def check_discountcode_displayed(self):
        totals = self.driver.find_element(*ReviewOrder.discount_ordertotals_field).is_displayed()
        fields = self.driver.find_element(*ReviewOrder.discount_fields).is_displayed()
        return totals and fields


    coupon_error = (By.XPATH, "//*[@id='coupon_code_error']")

    def check_discount_error_displayed(self):
        return self.driver.find_element(*ReviewOrder.coupon_error).is_displayed()

    def check_discount_error_text(self):
        text = self.driver.find_element(*ReviewOrder.coupon_error).text
        return text

    def assert_discount_code_displayed(self):
        try:
            assert self.check_discount_error_displayed() == False
        except NoSuchElementException:
            pass

        try:
            assert self.check_discountcode_displayed() == True
        except NoSuchElementException:
            assert False, "NoSuchElementException occurred, test failed"

        assert self.get_totalorder() == "£15.00"


    def assert_error_discount_code_displayed(self):
        try:
            assert self.check_discountcode_displayed() == False
        except NoSuchElementException:
            pass

        try:
            assert self.check_discount_error_displayed() == True
        except NoSuchElementException:
            assert False, "NoSuchElementException occurred, test failed"


    totalorder = (By.XPATH, "//*[@class='order-description sub-total']/p[2]")

    def get_totalorder(self):
        text = self.driver.find_element(*ReviewOrder.totalorder).text.strip()
        return text

    cardbutton_totalorder = (By.XPATH, "//button[@class='payment-btn btn btn-primary']//strong")

    def get_cardbutton_totalorder(self):
        text = self.driver.find_element(*ReviewOrder.cardbutton_totalorder).text.strip()
        return text


    def pay_via_card_no_clickcard(self):
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

    firstname           = (By.XPATH, "//*[@id='first_name']")

    lastname            = (By.XPATH, "//*[@id='last_name']")

    country             = (By.XPATH, "//*[@id='country']")

    #qa
    billingaddressline1 = (By.XPATH, "//*[@id='street_1']")

    billingaddressline2 = (By.XPATH, "//*[@id='street_2']")


    #staging
    # billingaddressline1 = (By.XPATH, "//*[@id='street_address']")
    #
    # billingaddressline2 = (By.XPATH, "//*[@id='street_address_1']")

    city                = (By.XPATH, "//*[@id='city']")

    state               = (By.XPATH, "//*[@id='state']")

    postcode            = (By.XPATH, "//*[@id='postcode']")


    # Select countries for target market country test

    bra                 = (By.XPATH, "//a[text()='Brazil']")

    can                 = (By.XPATH, "//a[text()='Canada']")

    ind                 = (By.XPATH, "//a[text()='India']")

    ita                 = (By.XPATH, "//a[text()='Italy']")

    mex                 = (By.XPATH, "//a[text()='Mexico']")

    nld                 = (By.XPATH, "//a[text()='Netherlands']")

    phl                 = (By.XPATH, "//a[text()='Philippines']")

    pol                 = (By.XPATH, "//a[text()='Poland']")

    prt                 = (By.XPATH, "//a[text()='Portugal']")

    rus                 = (By.XPATH, "//a[text()='Russian Federation']")

    esp                 = (By.XPATH, "//a[text()='Spain']")

    che                 = (By.XPATH, "//a[text()='Switzerland']")

    gbr                 = (By.XPATH, "//a[text()='United Kingdom']")

    usa                 = (By.XPATH, "//a[text()='United States']")

    tur                 = (By.XPATH, "//a[text()='Türkiye']")


    #Button to Review order

    updateaddress     = (By.XPATH, "//div[@class='save-details-container']")

    def click_updateaddress(self):
        self.driver.find_element(*ReviewOrder.updateaddress).click()
        sleep(10)

    def input_bra_country(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.country).send_keys(i.bra_country)
        sleep(2)

    def input_can_country(self):

        i = Data(self.driver)

        self.driver.find_element(*ReviewOrder.country).send_keys(i.can_country)
        sleep(2)

    def input_che_country(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.country).send_keys(i.che_country)
        sleep(2)

    def input_esp_country(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.country).send_keys(i.esp_country)
        sleep(2)

    def input_gbr_country(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.country).send_keys(i.gbr_country)
        sleep(2)

    def input_ind_country(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.country).send_keys(i.ind_country)
        sleep(2)

    def input_ita_country(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.country).send_keys(i.ita_country)
        sleep(2)

    def input_mex_country(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.country).send_keys(i.mex_country)
        sleep(5)

    def input_nld_country(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.country).send_keys(i.nld_country)
        sleep(5)

    def input_phl_country(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.country).send_keys(i.phl_country)
        sleep(5)

    def input_pol_country(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.country).send_keys(i.pol_country)
        sleep(5)

    def input_prt_country(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.country).send_keys(i.prt_country)
        sleep(5)

    def input_rus_country(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.country).send_keys(i.rus_country)
        sleep(5)

    def input_usa_country(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.country).send_keys(i.usa_country)
        sleep(5)

    #-------------------------------------------------------------------------------------------------------------------
    # Countries: billing address line1

    def input_bra_billingaddressline1(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.billingaddressline1).send_keys(i.bra_billingaddressline1)
        sleep(5)

    def input_can_billingaddressline1(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.billingaddressline1).send_keys(i.can_billingaddressline1)
        sleep(5)

    def input_che_billingaddressline1(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.billingaddressline1).send_keys(i.che_billingaddressline1)
        sleep(5)

    def input_esp_billingaddressline1(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.billingaddressline1).send_keys(i.esp_billingaddressline1)
        sleep(5)

    def input_gbr_billingaddressline1(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.billingaddressline1).send_keys(i.gbr_billingaddressline1)
        sleep(5)

    def input_ind_billingaddressline1(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.billingaddressline1).send_keys(i.ind_billingaddressline1)
        sleep(5)

    def input_ita_billingaddressline1(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.billingaddressline1).send_keys(i.ita_billingaddressline1)
        sleep(5)

    def input_mex_billingaddressline1(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.billingaddressline1).send_keys(i.mex_billingaddressline1)
        sleep(5)

    def input_nld_billingaddressline1(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.billingaddressline1).send_keys(i.nld_billingaddressline1)
        sleep(5)

    def input_phl_billingaddressline1(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.billingaddressline1).send_keys(i.phl_billingaddressline1)
        sleep(5)

    def input_pol_billingaddressline1(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.billingaddressline1).send_keys(i.pol_billingaddressline1)
        sleep(5)

    def input_prt_billingaddressline1(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.billingaddressline1).send_keys(i.prt_billingaddressline1)
        sleep(5)

    def input_rus_billingaddressline1(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.billingaddressline1).send_keys(i.rus_billingaddressline1)
        sleep(5)

    def input_usa_billingaddressline1(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.billingaddressline1).send_keys(i.usa_billingaddressline1)
        sleep(5)

    #-------------------------------------------------------------------------------------------------------------------
    # Countries: billing address line2


    def input_bra_billingaddressline2(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.billingaddressline2).send_keys(i.bra_billingaddressline2)
        sleep(5)

    def input_can_billingaddressline2(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.billingaddressline2).send_keys(i.can_billingaddressline2)
        sleep(5)

    def input_che_billingaddressline2(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.billingaddressline2).send_keys(i.che_billingaddressline2)
        sleep(5)

    def input_esp_billingaddressline2(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.billingaddressline2).send_keys(i.esp_billingaddressline2)
        sleep(5)

    def input_gbr_billingaddressline2(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.billingaddressline2).send_keys(i.gbr_billingaddressline2)
        sleep(5)

    def input_ind_billingaddressline2(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.billingaddressline2).send_keys(i.ind_billingaddressline2)
        sleep(5)

    def input_ita_billingaddressline2(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.billingaddressline2).send_keys(i.ita_billingaddressline2)
        sleep(5)

    def input_mex_billingaddressline2(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.billingaddressline2).send_keys(i.mex_billingaddressline2)
        sleep(5)

    def input_nld_billingaddressline2(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.billingaddressline2).send_keys(i.nld_billingaddressline2)
        sleep(5)

    def input_phl_billingaddressline2(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.billingaddressline2).send_keys(i.phl_billingaddressline2)
        sleep(5)

    def input_pol_billingaddressline2(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.billingaddressline2).send_keys(i.pol_billingaddressline2)
        sleep(5)

    def input_prt_billingaddressline2(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.billingaddressline2).send_keys(i.prt_billingaddressline2)
        sleep(5)

    def input_rus_billingaddressline2(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.billingaddressline2).send_keys(i.rus_billingaddressline2)
        sleep(5)

    def input_usa_billingaddressline2(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.billingaddressline2).send_keys(i.usa_billingaddressline2)
        sleep(5)

    #-------------------------------------------------------------------------------------------------------------------
    # Countries: Input city

    def input_bra_city(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.city).send_keys(i.bra_city)
        sleep(5)

    def input_can_city(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.city).send_keys(i.can_city)
        sleep(5)

    def input_che_city(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.city).send_keys(i.che_city)
        sleep(5)

    def input_esp_city(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.city).send_keys(i.esp_city)
        sleep(5)

    def input_gbr_city(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.city).send_keys(i.gbr_city)
        sleep(5)

    def input_ind_city(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.city).send_keys(i.ind_city)
        sleep(5)

    def input_ita_city(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.city).send_keys(i.ita_city)
        sleep(5)

    def input_mex_city(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.city).send_keys(i.mex_city)
        sleep(5)

    def input_nld_city(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.city).send_keys(i.nld_city)
        sleep(5)

    def input_phl_city(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.city).send_keys(i.phl_city)
        sleep(5)

    def input_pol_city(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.city).send_keys(i.pol_city)
        sleep(5)

    def input_prt_city(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.city).send_keys(i.prt_city)
        sleep(5)

    def input_rus_city(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.city).send_keys(i.rus_city)
        sleep(5)

    def input_usa_city(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.city).send_keys(i.usa_city)
        sleep(5)

    #-------------------------------------------------------------------------------------------------------------------
    # Countries: Input state


    def input_bra_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.state).send_keys(i.bra_state)
        sleep(5)

    def input_can_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.state).send_keys(i.can_state)
        sleep(5)

    def input_che_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.state).send_keys(i.che_state)
        sleep(5)

    def input_esp_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.state).send_keys(i.esp_state)
        sleep(5)

    def input_gbr_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.state).send_keys(i.gbr_state)
        sleep(5)

    def input_ind_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.state).send_keys(i.ind_state)
        sleep(5)

    def input_ita_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.state).send_keys(i.ita_state)
        sleep(5)

    def input_mex_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.state).send_keys(i.mex_state)
        sleep(5)

    def input_nld_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.state).send_keys(i.nld_state)
        sleep(5)

    def input_phl_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.state).send_keys(i.phl_state)
        sleep(5)

    def input_pol_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.state).send_keys(i.pol_state)
        sleep(5)

    def input_prt_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.state).send_keys(i.prt_state)
        sleep(5)

    def input_rus_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.state).send_keys(i.rus_state)
        sleep(5)

    def input_usa_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.state).send_keys(i.usa_state)
        sleep(5)

    #-------------------------------------------------------------------------------------------------------------------
    # Countries: Input post code

    def input_bra_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.postcode).send_keys(i.bra_postcode)
        sleep(5)

    def input_can_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.postcode).send_keys(i.can_postcode)
        sleep(5)

    def input_che_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.postcode).send_keys(i.che_postcode)
        sleep(5)

    def input_esp_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.postcode).send_keys(i.esp_postcode)
        sleep(5)

    def input_gbr_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.postcode).send_keys(i.gbr_postcode)
        sleep(5)

    def input_ind_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.postcode).send_keys(i.ind_postcode)
        sleep(5)

    def input_ita_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.postcode).send_keys(i.ita_postcode)
        sleep(5)

    def input_mex_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.postcode).send_keys(i.mex_postcode)
        sleep(5)

    def input_nld_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.postcode).send_keys(i.nld_postcode)
        sleep(5)

    def input_phl_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.postcode).send_keys(i.phl_postcode)
        sleep(5)

    def input_pol_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.postcode).send_keys(i.pol_postcode)
        sleep(5)

    def input_prt_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.postcode).send_keys(i.prt_postcode)
        sleep(5)

    def input_rus_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.postcode).send_keys(i.rus_postcode)
        sleep(5)

    def input_usa_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.postcode).send_keys(i.usa_postcode)
        sleep(5)

    #-------------------------------------------------------------------------------------------------------------------
    # Countries: Select country

    def select_bra(self):
        self.driver.find_element(*ReviewOrder.bra).click()
        sleep(10)

    def select_can(self):
        self.driver.find_element(*ReviewOrder.can).click()
        sleep(10)

    def select_che(self):
        self.driver.find_element(*ReviewOrder.che).click()
        sleep(10)

    def select_esp(self):
        self.driver.find_element(*ReviewOrder.esp).click()
        sleep(10)

    def select_gbr(self):
        self.driver.find_element(*ReviewOrder.gbr).click()
        sleep(10)

    def select_ind(self):
        self.driver.find_element(*ReviewOrder.ind).click()
        sleep(10)

    def select_ita(self):
        self.driver.find_element(*ReviewOrder.ita).click()
        sleep(10)

    def select_mex(self):
        self.driver.find_element(*ReviewOrder.mex).click()
        sleep(10)

    def select_nld(self):
        self.driver.find_element(*ReviewOrder.nld).click()
        sleep(10)

    def select_phl(self):
        self.driver.find_element(*ReviewOrder.phl).click()
        sleep(10)

    def select_pol(self):
        self.driver.find_element(*ReviewOrder.pol).click()
        sleep(10)

    def select_prt(self):
        self.driver.find_element(*ReviewOrder.prt).click()
        sleep(10)

    def select_rus(self):
        self.driver.find_element(*ReviewOrder.rus).click()
        sleep(10)

    def select_usa(self):
        self.driver.find_element(*ReviewOrder.usa).click()
        sleep(10)

    # Update countries

    def clear_country_input(self):
        self.driver.find_element(*ReviewOrder.country).click()
        self.driver.find_element(*ReviewOrder.country).clear()
        sleep(5)



    def edit_bra_country_details_and_update(self):
        self.clear_country_input()
        self.input_bra_country()
        self.select_bra()
        self.input_bra_billingaddressline1()
        self.input_bra_billingaddressline2()
        self.input_bra_city()
        self.input_bra_state()
        self.input_bra_postcode()
        self.click_updateaddress()

    def edit_can_billing_details_and_update(self):
        self.clear_country_input()
        self.input_can_country()
        self.select_can()
        self.input_can_billingaddressline1()
        self.input_can_billingaddressline2()
        self.input_can_city()
        self.input_can_state()
        self.input_can_postcode()
        self.click_updateaddress()

    def edit_che_billing_details_and_update(self):
        self.clear_country_input()
        self.input_che_country()
        self.select_che()
        self.input_che_billingaddressline1()
        self.input_che_billingaddressline2()
        self.input_che_city()
        self.input_che_state()
        self.input_che_postcode()
        self.click_updateaddress()

    def edit_esp_billing_details_and_update(self):
        self.clear_country_input()
        self.input_esp_country()
        self.select_esp()
        self.input_esp_billingaddressline1()
        self.input_esp_billingaddressline2()
        self.input_esp_city()
        self.input_esp_state()
        self.input_esp_postcode()
        self.click_updateaddress()

    def edit_gbr_billing_details_and_update(self):
        self.clear_country_input()
        self.input_gbr_country()
        self.select_gbr()
        self.input_gbr_billingaddressline1()
        self.input_gbr_billingaddressline2()
        self.input_gbr_city()
        self.input_gbr_state()
        self.input_gbr_postcode()
        self.click_updateaddress()

    def edit_ind_billing_details_and_update(self):
        self.clear_country_input()
        self.input_ind_country()
        self.select_ind()
        self.input_ind_billingaddressline1()
        self.input_ind_billingaddressline2()
        self.input_ind_city()
        self.input_ind_state()
        self.input_ind_postcode()
        self.click_updateaddress()

    def edit_ita_billing_details_and_update(self):
        self.clear_country_input()
        self.input_ita_country()
        self.select_ita()
        self.input_ita_billingaddressline1()
        self.input_ita_billingaddressline2()
        self.input_ita_city()
        self.input_ita_state()
        self.input_ita_postcode()
        self.click_updateaddress()

    def edit_mex_billing_details_and_update(self):
        self.clear_country_input()
        self.input_mex_country()
        self.select_mex()
        self.input_mex_billingaddressline1()
        self.input_mex_billingaddressline2()
        self.input_mex_city()
        self.input_mex_state()
        self.input_mex_postcode()
        self.click_updateaddress()

    def edit_nld_billing_details_and_update(self):
        self.clear_country_input()
        self.input_nld_country()
        self.select_nld()
        self.input_nld_billingaddressline1()
        self.input_nld_billingaddressline2()
        self.input_nld_city()
        self.input_nld_state()
        self.input_nld_postcode()
        self.click_updateaddress()

    def edit_phl_billing_details_and_update(self):
        self.clear_country_input()
        self.input_phl_country()
        self.select_phl()
        self.input_phl_billingaddressline1()
        self.input_phl_billingaddressline2()
        self.input_phl_city()
        self.input_phl_state()
        self.input_phl_postcode()
        self.click_updateaddress()

    def edit_pol_billing_details_and_update(self):
        self.clear_country_input()
        self.input_pol_country()
        self.select_pol()
        self.input_pol_billingaddressline1()
        self.input_pol_billingaddressline2()
        self.input_pol_city()
        self.input_pol_state()
        self.input_pol_postcode()
        self.click_updateaddress()

    def edit_prt_billing_details_and_update(self):
        self.clear_country_input()
        self.input_prt_country()
        self.select_prt()
        self.input_prt_billingaddressline1()
        self.input_prt_billingaddressline2()
        self.input_prt_city()
        self.input_prt_state()
        self.input_prt_postcode()
        self.click_updateaddress()

    def edit_rus_billing_details_and_update(self):
        self.clear_country_input()
        self.input_rus_country()
        self.select_rus()
        self.input_rus_billingaddressline1()
        self.input_rus_billingaddressline2()
        self.input_rus_city()
        self.input_rus_state()
        self.input_rus_postcode()
        self.click_updateaddress()

    def edit_usa_billing_details_and_update(self):
        self.clear_country_input()
        self.input_usa_country()
        self.select_usa()
        self.input_usa_billingaddressline1()
        self.input_usa_billingaddressline2()
        self.input_usa_city()
        self.input_usa_state()
        self.input_usa_postcode()
        self.click_updateaddress()


