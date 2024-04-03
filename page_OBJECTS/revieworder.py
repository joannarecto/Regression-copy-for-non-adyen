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

    def input_amex_challenge_cardnumber(self):
        return self.driver.find_element(*ReviewOrder.cardnumber).send_keys("3400 000000 02534")
        sleep(5)

    def input_mastercard_challenge_cardnumber(self):
        return self.driver.find_element(*ReviewOrder.cardnumber).send_keys("5200 0000 0000 2151")
        sleep(5)

    def input_visa_challenge_cardnumber(self):
        return self.driver.find_element(*ReviewOrder.cardnumber).send_keys("4456 5300 0000 1096")
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
