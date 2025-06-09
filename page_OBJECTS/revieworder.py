from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from utilities.wait import wait_for_element, wait_for_elements

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
        return self.driver.find_element(*ReviewOrder.cardnumber).send_keys("5200000000002151")
        sleep(5)

    def input_amex_challenge_cardnumber(self):
        return self.driver.find_element(*ReviewOrder.cardnumber).send_keys("3400 000000 02534")
        sleep(5)

    def input_mastercard_challenge_cardnumber(self):
        return self.driver.find_element(*ReviewOrder.cardnumber).send_keys("5200000000002151")
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
        return self.driver.find_element(*ReviewOrder.expirydate).send_keys("25")
        sleep(5)

    def securitycode_frame(self):
        return self.driver.find_elements(by=By.TAG_NAME, value="iframe")[1]

    def input_securitycode(self):
        return self.driver.find_element(*ReviewOrder.securitycode).send_keys("123")
        sleep(5)

    def input_failed_securitycode(self):
        return self.driver.find_element(*ReviewOrder.securitycode).send_keys("124")
        sleep(5)

    def input_amex_securitycode(self):
        return self.driver.find_element(*ReviewOrder.securitycode).send_keys("1235")
        sleep(5)

    def click_paynow(self):
        self.driver.find_element(*ReviewOrder.paynow).click()
        sleep(30)

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

    def pay_failed_securitycode_via_card(self):
        self.click_card()
        self.driver.switch_to.frame(self.cardnumber_frame())
        self.input_cardnumber()
        self.driver.switch_to.default_content()
        self.input_expirymonth()
        self.input_expiryyear()
        self.driver.switch_to.frame(self.securitycode_frame())
        self.input_failed_securitycode()
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

    paypalbutton = (By.XPATH, "//*[@id='accordionPaypal']/div/div/div")

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
        return self.driver.find_element(*ReviewOrder.itemprice1).text.replace("\n", "")

    def get_itemprice1_without_whitespace(self):
        return self.driver.find_element(*ReviewOrder.itemprice1).text.strip()

    # AUD
    def get_aud_TT_B2FSS_price(self):
        return self.get_itemprice1_with_whitespace()

    def get_aud_PP1_price(self):
        return self.get_itemprice1_with_whitespace()

    # CAD
    def get_cad_TT_B2FSS_price(self):
        return self.get_itemprice1_with_whitespace()

    def get_cad_PP1_price(self):
        return self.get_itemprice1_with_whitespace()

    # EUR
    def get_eur_TT_B2FSS_price(self):
        return self.get_itemprice1_without_whitespace()

    def get_eur_PP1_price(self):
        return self.get_itemprice1_without_whitespace()

    # EUR C
    def get_eur_c_SF_L1DSB_price(self):
        return self.get_itemprice1_without_whitespace()

    def get_eur_c_TT_B2FSS_price(self):
        return self.get_itemprice1_without_whitespace()

    def get_eur_c_PP1_price(self):
        return self.get_itemprice1_with_whitespace()

    # EUR I
    def get_eur_i_SF_L1DSB_price(self):
        return self.get_itemprice1_without_whitespace()

    def get_eur_i_TT_B2FSS_price(self):
        return self.get_itemprice1_without_whitespace()

    def get_eur_i_PP1_price(self):
        return self.get_itemprice1_with_whitespace()

    # GBP
    def get_gbp_TT_B2FSS_price(self):
        return self.get_itemprice1_without_whitespace()

    def get_gbp_PP1_price(self):
        return self.get_itemprice1_without_whitespace()


    # NZD
    def get_nzd_TT_B2FSS_price(self):
        return self.get_itemprice1_with_whitespace()

    def get_nzd_PP1_price(self):
        return self.get_itemprice1_with_whitespace()

    # USD
    def get_usd_TT_B2FSS_price(self):
        return self.get_itemprice1_with_whitespace()

    def get_usd_PP1_price(self):
        return self.get_itemprice1_with_whitespace()

    # USD E
    def get_usd_e_SF_L1DSB_price(self):
        return self.get_itemprice1_with_whitespace()

    def get_usd_e_TT_B2FSS_price(self):
        return self.get_itemprice1_with_whitespace()

    def get_usd_e_PP1_price(self):
        return self.get_itemprice1_with_whitespace()

    # USD N
    def get_usd_n_SF_L1DSB_price(self):
        return self.get_itemprice1_with_whitespace()

    def get_usd_n_TT_B2FSS_price(self):
        return self.get_itemprice1_with_whitespace()

    def get_usd_n_PP1_price(self):
        return self.get_itemprice1_with_whitespace()

# ------------------------MIXED PRICE----------------------------------------------------------------------------
    # mixed_price = (By.XPATH, "(//div[contains(@class, 'price-wrapper')]")

    def get_aud_mixed_price(self):
        def extract_price(currency_str):
            return float(currency_str.replace("AU $", "").replace(",", "").strip())

        prices = self.driver.find_elements(*ReviewOrder.itemprice1)
        price_list = [price.text for price in prices]
        total_value = sum(extract_price(price) for price in price_list)
        total_amount = f"AU ${total_value:.2f}"
        return total_amount

    def get_cad_mixed_price(self):
        def extract_price(currency_str):
            return float(currency_str.replace("CA $", "").replace(",", "").strip())

        prices = self.driver.find_elements(*ReviewOrder.itemprice1)
        price_list = [price.text for price in prices]
        total_value = sum(extract_price(price) for price in price_list)
        total_amount = f"CA ${total_value:.2f}"
        return total_amount

    def get_gbp_mixed_price(self):
        def extract_price(currency_str):
            return float(currency_str.replace("£", "").replace(",", "").strip())

        prices = self.driver.find_elements(*ReviewOrder.itemprice1)
        price_list = [price.text for price in prices]
        total_value = sum(extract_price(price) for price in price_list)
        total_amount = f"£{total_value:.2f}"
        return total_amount

    def get_nzd_mixed_price(self):
        def extract_price(currency_str):
            return float(currency_str.replace("NZ $", "").replace(",", "").strip())

        prices = self.driver.find_elements(*ReviewOrder.itemprice1)
        price_list = [price.text for price in prices]
        total_value = sum(extract_price(price) for price in price_list)
        total_amount = f"NZ ${total_value:.2f}"
        return total_amount

    def get_eur_c_mixed_price(self):
        def extract_price(currency_str):
            return float(currency_str.replace("€", "").replace(",", "").strip())

        prices = self.driver.find_elements(*ReviewOrder.itemprice1)
        price_list = [price.text for price in prices]
        total_value = sum(extract_price(price) for price in price_list)
        total_value_in_euros = total_value / 100
        formatted_value = f"€{total_value_in_euros:.2f}".replace('.', ',')
        return formatted_value

    def get_eur_i_mixed_price(self):
        def extract_price(currency_str):
            return float(currency_str.replace("€", "").replace(",", "").strip())

        prices = self.driver.find_elements(*ReviewOrder.itemprice1)
        price_list = [price.text for price in prices]
        total_value = sum(extract_price(price) for price in price_list)
        total_value_in_euros = total_value / 100
        formatted_value = f"€{total_value_in_euros:.2f}".replace('.', ',')
        return formatted_value

    def get_usd_e_mixed_price(self):
        def extract_price(currency_str):
            return float(currency_str.replace("US $", "").replace(",", "").strip())

        prices = self.driver.find_elements(*ReviewOrder.itemprice1)
        price_list = [price.text for price in prices]
        total_value = sum(extract_price(price) for price in price_list)
        total_amount = f"US ${total_value:.2f}"
        return total_amount

    def get_usd_n_mixed_price(self):
        def extract_price(currency_str):
            return float(currency_str.replace("US $", "").replace(",", "").strip())

        prices = self.driver.find_elements(*ReviewOrder.itemprice1)
        price_list = [price.text for price in prices]
        total_value = sum(extract_price(price) for price in price_list)
        total_amount = f"US ${total_value:.2f}"
        return total_amount

    #-------------------------------------------------------------------------------------------------------------------

    subtotalvalue = (By.XPATH, "//div[@class='order-description sub-total mt-3' and contains(p/text(), 'Subtotal')]/span")

    def get_subtotal_with_whitespace(self):
        return self.driver.find_element(*ReviewOrder.subtotalvalue).text.replace(" \n", " ")

    def get_subtotal_without_whitespace(self):
        return self.driver.find_element(*ReviewOrder.subtotalvalue).text.strip()

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

    ordertotalvalue = (By.XPATH, "//div[@class='order-description sub-total' and div/p[contains(text(), 'Order Total')]]/span")

    def get_ordertotal_with_whitespace(self):
        return self.driver.find_element(*ReviewOrder.ordertotalvalue).text.replace(" \n", " ")

    def get_ordertotal_without_whitespace(self):
        return self.driver.find_element(*ReviewOrder.ordertotalvalue).text.strip()

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

    deliverycharge = (By.XPATH, "//div[@class='order-description sub-total mt-3']//p[text()='Delivery']/following-sibling::span/strong")

    def get_deliverycharge_with_whitespace(self):
        return self.driver.find_element(*ReviewOrder.deliverycharge).text.replace(" \n", " ")

    def get_deliverycharge_without_whitespace(self):
        return self.driver.find_element(*ReviewOrder.deliverycharge).text.strip()

    def get_aud_deliverycharge(self):
        return self.get_deliverycharge_with_whitespace()

    def get_cad_deliverycharge(self):
        return self.get_deliverycharge_with_whitespace()

    def get_eur_deliverycharge(self):
        return self.get_deliverycharge_without_whitespace()

    def get_eur_c_deliverycharge(self):
        return self.get_deliverycharge_without_whitespace()

    def get_eur_i_deliverycharge(self):
        return self.get_deliverycharge_without_whitespace()

    def get_gbp_deliverycharge(self):
        return self.get_deliverycharge_without_whitespace()

    def get_nzd_deliverycharge(self):
        return self.get_deliverycharge_with_whitespace()

    def get_usd_deliverycharge(self):
        return self.get_deliverycharge_with_whitespace()

    def get_usd_e_deliverycharge(self):
        return self.get_deliverycharge_with_whitespace()

    def get_usd_n_deliverycharge(self):
        return self.get_deliverycharge_with_whitespace()

    #-------------------------------------------------------------------------------------------------------------------
    shippingcharge = (By.XPATH, "//span[contains(text(),'Standard Shipping -')]/following-sibling::span/strong")

    def get_shippingcharge_with_whitespace(self):
        return self.driver.find_element(*ReviewOrder.shippingcharge).text.replace(" \n", " ")

    def get_shippingcharge_without_whitespace(self):
        return self.driver.find_element(*ReviewOrder.shippingcharge).text.strip()

    def get_aud_shippingcharge(self):
        return self.get_shippingcharge_with_whitespace()

    def get_cad_shippingcharge(self):
        return self.get_shippingcharge_with_whitespace()

    def get_eur_shippingcharge(self):
        return self.get_shippingcharge_without_whitespace()

    def get_eur_c_shippingcharge(self):
        return self.get_shippingcharge_without_whitespace()

    def get_eur_i_shippingcharge(self):
        return self.get_shippingcharge_without_whitespace()

    def get_gbp_shippingcharge(self):
        return self.get_shippingcharge_without_whitespace()

    def get_nzd_shippingcharge(self):
        return self.get_shippingcharge_with_whitespace()

    def get_usd_shippingcharge(self):
        return self.get_shippingcharge_with_whitespace()

    def get_usd_e_shippingcharge(self):
        return self.get_shippingcharge_with_whitespace()

    def get_usd_n_shippingcharge(self):
        return self.get_shippingcharge_with_whitespace()

    #-------------------------------------------------------------------------------------------------------------------
    delivery_date =  (By.XPATH, "//span[contains(text(),'Estimated delivery')]/following-sibling::strong/span")

    def estimate_delivery_date(self):
        return self.driver.find_element(*ReviewOrder.delivery_date).text

    delivery_days =  (By.XPATH, "(//div[@class='shipping-details']//div//span)[last()]")
    def estimate_delivery_days(self):
        return self.driver.find_element(*ReviewOrder.delivery_days).text

    #-------------------------------------------------------------------------------------------------------------------

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

    def back_to_shopping_is_enabled(self):
        return self.driver.find_element(*ReviewOrder.backtoshopping).is_enabled()

    #-------------------------------------------------------------------------------------------------------------------

    continueshopping = (By.XPATH, "//*[text()=' Continue shopping ']")

    def click_continueshopping(self):
        self.driver.find_element(*ReviewOrder.continueshopping).click()
        sleep(25)

    def continueshopping_enabled(self):
        return self.driver.find_element(*ReviewOrder.continueshopping).is_enabled()

    def continue_shopping_is_enabled(self):
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

    xitem1 = (By.XPATH, "(//*[contains(@class,'close')])[1]")

    xitem2 = (By.XPATH, "(//*[contains(@class,'close')])[2]")

    xitem3 = (By.XPATH, "(//*[contains(@class,'close')])[3]")

    def x_item1(self):
        self.driver.find_element(*ReviewOrder.xitem1).click()
        sleep(2)

    def x_item2(self):
        self.driver.find_element(*ReviewOrder.xitem2).click()
        sleep(2)

    def x_item3(self):
        self.driver.find_element(*ReviewOrder.xitem3).click()
        sleep(2)

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

    del_edit_address = (By.XPATH, "//div[@class='delivery-address']//button[@class='btn btn-icon edit-address']")
    bill_edit_address = (By.XPATH, "//div[@class='billing-address']//button[@class='btn btn-icon edit-address']")

    def click_edit_billingaddress(self):
        self.driver.find_element(*ReviewOrder.bill_edit_address).click()
        sleep(5)

    def click_edit_deliveryaddress(self):
        self.driver.find_element(*ReviewOrder.del_edit_address).click()
        sleep(5)

    #-------------------------------------------------------------------------------------------------------------------

    def page_src(self):
        body = self.driver.find_element(By.TAG_NAME, 'body').text
        return body

    header_text = (By.XPATH, "//h1[@class='page-header__title']")
    def page_title(self):
        text = self.driver.find_element(*ReviewOrder.header_text).text
        return text

    #-------------------------------------------------------------------------------------------------------------------

    del_firstname    = (By.XPATH, "//div[@class='delivery-address']//input[@id='first_name']")
    del_lastname     = (By.XPATH, "//div[@class='delivery-address']//input[@id='last_name']")
    del_country      = (By.XPATH, "//div[@class='delivery-address']//input[@id='country']")
    del_addressline1 = (By.XPATH, "//div[@class='delivery-address']//input[@id='street_1']")
    del_addressline2 = (By.XPATH, "//div[@class='delivery-address']//input[@id='street_2']")
    del_city         = (By.XPATH, "//div[@class='delivery-address']//input[@id='city']")
    del_state        = (By.XPATH, "//div[@class='delivery-address']//input[@id='state']")
    del_postcode     = (By.XPATH, "//div[@class='delivery-address']//input[@id='postcode']")



    def get_delivery_firstname_value(self):
        value = self.driver.find_element(*ReviewOrder.del_firstname).get_attribute("value")
        return value

    def get_delivery_lastname_value(self):
        value = self.driver.find_element(*ReviewOrder.del_lastname).get_attribute("value")
        return value

    def get_delivery_country_value(self):
        value = self.driver.find_element(*ReviewOrder.del_country).get_attribute("value")
        return value

    def get_delivery_addressline1_value(self):
        value = self.driver.find_element(*ReviewOrder.del_addressline1).get_attribute("value")
        return value

    def get_delivery_addressline2_value(self):
        value = self.driver.find_element(*ReviewOrder.del_addressline2).get_attribute("value")
        return value

    def get_delivery_city_value(self):
        value = self.driver.find_element(*ReviewOrder.del_city).get_attribute("value")
        return value

    def get_delivery_state_value(self):
        value = self.driver.find_element(*ReviewOrder.del_state).get_attribute("value")
        return value

    def get_delivery_postcode_value(self):
        value = self.driver.find_element(*ReviewOrder.del_postcode).get_attribute("value")
        return value



    bill_firstname    = (By.XPATH, "//div[@class='billing-address']//input[@id='first_name']")
    bill_lastname     = (By.XPATH, "//div[@class='billing-address']//input[@id='last_name']")
    bill_country      = (By.XPATH, "//div[@class='billing-address']//input[@id='country']")
    bill_addressline1 = (By.XPATH, "//div[@class='billing-address']//input[@id='street_1']")
    bill_addressline2 = (By.XPATH, "//div[@class='billing-address']//input[@id='street_2']")
    bill_city         = (By.XPATH, "//div[@class='billing-address']//input[@id='city']")
    bill_state        = (By.XPATH, "//div[@class='billing-address']//input[@id='state']")
    bill_postcode     = (By.XPATH, "//div[@class='billing-address']//input[@id='postcode']")



    def get_billing_firstname_value(self):
        value = self.driver.find_element(*ReviewOrder.bill_firstname).get_attribute("value")
        return value

    def get_billing_lastname_value(self):
        value = self.driver.find_element(*ReviewOrder.bill_lastname).get_attribute("value")
        return value

    def get_billing_country_value(self):
        value = self.driver.find_element(*ReviewOrder.bill_country).get_attribute("value")
        return value

    def get_billing_addressline1_value(self):
        value = self.driver.find_element(*ReviewOrder.bill_addressline1).get_attribute("value")
        return value

    def get_billing_addressline2_value(self):
        value = self.driver.find_element(*ReviewOrder.bill_addressline2).get_attribute("value")
        return value

    def get_billing_city_value(self):
        value = self.driver.find_element(*ReviewOrder.bill_city).get_attribute("value")
        return value

    def get_billing_state_value(self):
        value = self.driver.find_element(*ReviewOrder.bill_state).get_attribute("value")
        return value

    def get_billing_postcode_value(self):
        value = self.driver.find_element(*ReviewOrder.bill_postcode).get_attribute("value")
        return value

    del_fullname_c       = (By.XPATH, "//div[@class='delivery-address']//span[1]")
    del_addressline1_c   = (By.XPATH, "//div[@class='delivery-address']//span[2]")
    del_addressline2_c   = (By.XPATH, "//div[@class='delivery-address']//span[3]")
    del_city_c           = (By.XPATH, "//div[@class='delivery-address']//span[4]")
    del_state_c          = (By.XPATH, "//div[@class='delivery-address']//span[5]")
    del_postcode_c       = (By.XPATH, "//div[@class='delivery-address']//span[6]")
    del_country_c        = (By.XPATH, "//div[@class='delivery-address']//span[7]")

    def get_delivery_fullname(self):
        text = self.driver.find_element(*ReviewOrder.del_fullname_c).text
        value = text.strip().replace(",", "")
        return value

    def get_delivery_country(self):
        text = self.driver.find_element(*ReviewOrder.del_country_c).text
        value = text.strip().replace(",", "")
        return value

    def get_delivery_addressline1(self):
        text = self.driver.find_element(*ReviewOrder.del_addressline1_c).text
        value = text.strip().replace(",", "")
        return value

    def get_delivery_addressline2(self):
        text = self.driver.find_element(*ReviewOrder.del_addressline2_c).text
        value = text.strip().replace(",", "")
        return value

    def get_delivery_city(self):
        text = self.driver.find_element(*ReviewOrder.del_city_c).text
        value = text.strip().replace(",", "")
        return value

    def get_delivery_state(self):
        text = self.driver.find_element(*ReviewOrder.del_state_c).text
        value = text.strip().replace(",", "")
        return value

    def get_delivery_postcode(self):
        text = self.driver.find_element(*ReviewOrder.del_postcode_c).text
        value = text.strip().replace(",", "")
        return value

    bill_fullname_c      = (By.XPATH, "//div[@class='billing-address']//span[1]")
    bill_addressline1_c  = (By.XPATH, "//div[@class='billing-address']//span[2]")
    bill_addressline2_c  = (By.XPATH, "//div[@class='billing-address']//span[3]")
    bill_city_c          = (By.XPATH, "//div[@class='billing-address']//span[4]")
    bill_state_c         = (By.XPATH, "//div[@class='billing-address']//span[5]")
    bill_postcode_c      = (By.XPATH, "//div[@class='billing-address']//span[6]")
    bill_country_c       = (By.XPATH, "//div[@class='billing-address']//span[7]")

    def get_billing_fullname(self):
        text = self.driver.find_element(*ReviewOrder.bill_fullname_c).text
        value = text.strip().replace(",", "")
        return value

    def get_billing_country(self):
        text = self.driver.find_element(*ReviewOrder.bill_country_c).text
        value = text.strip().replace(",", "")
        return value

    def get_billing_addressline1(self):
        text = self.driver.find_element(*ReviewOrder.bill_addressline1_c).text
        value = text.strip().replace(",", "")
        return value

    def get_billing_addressline2(self):
        text = self.driver.find_element(*ReviewOrder.bill_addressline2_c).text
        value = text.strip().replace(",", "")
        return value

    def get_billing_city(self):
        text = self.driver.find_element(*ReviewOrder.bill_city_c).text
        value = text.strip().replace(",", "")
        return value

    def get_billing_state(self):
        text = self.driver.find_element(*ReviewOrder.bill_state_c).text
        value = text.strip().replace(",", "")
        return value

    def get_billing_postcode(self):
        text = self.driver.find_element(*ReviewOrder.bill_postcode_c).text
        value = text.strip().replace(",", "")
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

    items = (By.XPATH, "//*[@class='media-body']/a")

    def revieworder_items(self):
       return self.driver.find_elements(*ReviewOrder.items)

    def revieworder_items_set(self):
        sleep(5)
        basket_items = [item.text for item in self.revieworder_items()]
        return basket_items

    def get_review_order_items(self):
        basket_items = [item.text for item in self.revieworder_items()]
        return basket_items

    #-------------------------------------------------------------------------------------------------------------------

    order_summary_box = (By.XPATH, "//div[@class='order-summary']")

    payment_method_box = (By.XPATH, "//section[contains(@class, 'payment-methods')]")

    checkbox_coupon = (By.XPATH, "//div[@class='custom-control custom-checkbox mb-0']")

    input_coupon = (By.XPATH, "//*[@id='discount_input']")

    button_coupon = (By.XPATH, "//button[text()=' Use code ']")

    remove_coupon = (By.XPATH, "//button[@type='button' and contains(@class, 'btn-icon') and .//span[text()='Remove Discount']]")


    def order_summary_section(self):
        text = self.driver.find_element(*ReviewOrder.order_summary_box).text
        return text

    def payment_method_section(self):
        return self.driver.find_element(*ReviewOrder.payment_method_box).is_displayed()

    def discount_checkbox_section(self):
        return self.driver.find_element(*ReviewOrder.checkbox_coupon).is_displayed()


    def tick_discountcode(self):
        self.driver.find_element(*ReviewOrder.checkbox_coupon).click()
        sleep(3)

    def input_discountcode(self):
        self.driver.find_element(*ReviewOrder.input_coupon).send_keys('TC599AC1')
        sleep(3)

    def input_freeshippingcode(self):
        self.driver.find_element(*ReviewOrder.input_coupon).send_keys('C005')
        sleep(3)

    def click_discountcode_btn(self):
        self.driver.find_element(*ReviewOrder.button_coupon).click()
        sleep(5)

    def remove_discountcode(self):
        self.driver.find_element(*ReviewOrder.remove_coupon).click()
        sleep(5)

    def use_discountcode(self):
        self.tick_discountcode()
        self.input_discountcode()
        self.click_discountcode_btn()

    def use_freeshippingcode(self):
        self.tick_discountcode()
        self.input_freeshippingcode()
        self.click_discountcode_btn()


    discount_fields = (By.XPATH, "//div[@class='discount mb-4']")

    discount_ordertotals_field = (By.XPATH, "//div[@class='order-description sub-total order-discount']")

    def check_discountcode_displayed(self):
        totals = self.driver.find_element(*ReviewOrder.discount_ordertotals_field).is_displayed()
        fields = self.driver.find_element(*ReviewOrder.discount_fields).is_displayed()
        return totals and fields

    def check_freeshippingcode_displayed(self):
        fields = self.driver.find_element(*ReviewOrder.discount_fields).is_displayed()
        return fields


    coupon_error = (By.XPATH, "//*[@id='coupon_code_error']")

    def check_discount_error_displayed(self):
        return self.driver.find_element(*ReviewOrder.coupon_error).is_displayed()

    def check_discount_error_text(self):
        text = self.driver.find_element(*ReviewOrder.coupon_error).text
        return text

    def assert_discountcode_section_displayed(self):
        try:
            assert self.check_discount_error_displayed() == False
        except NoSuchElementException:
            pass

        try:
            assert self.check_discountcode_displayed() == True
        except NoSuchElementException:
            assert False, "NoSuchElementException occurred, test failed"


    def assert_error_discount_code_displayed(self):
        try:
            assert self.check_discountcode_displayed() == False
        except NoSuchElementException:
            pass

        try:
            assert self.check_discount_error_displayed() == True
        except NoSuchElementException:
            assert False, "NoSuchElementException occurred, test failed"






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
        sleep(1)
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

    #-------------------------------------------------------------------------------------------------------------------

    TT_B2FSS = (By.XPATH, "//*[@src='//assets.cambridge.org/97810090/03452/cover/9781009003452.jpg']")

    TT_C1ASS = (By.XPATH, "//*[@src='//assets.cambridge.org/97811089/91667/cover/9781108991667.jpg']")

    def get_TT_B2FSS(self):
        return self.driver.find_element(*ReviewOrder.TT_B2FSS)

    def get_TT_C1ASS(self):
        return self.driver.find_element(*ReviewOrder.TT_C1ASS)

    def click_TT_B2FSS(self):
        self.driver.find_element(*ReviewOrder.TT_B2FSS).click()
        sleep(25)

    def click_TT_C1ASS(self):
        self.driver.find_element(*ReviewOrder.TT_C1ASS).click()
        sleep(25)

    def verify_TT_B2FSS_is_accessible(self):

        main_window = self.driver.window_handles[0]
        self.click_TT_B2FSS()
        TT_B2FSS_window = self.driver.window_handles[1]
        self.driver.switch_to.window(TT_B2FSS_window)
        ss_path = ('C:\\Users\\jgabriel\OneDrive - Cambridge\\Documents\\GitHub\\Checkout_Regression\\saved_SCREENSHOTS'
                   '\\VERIFY_IF_TT_B2FSS_WINDOW_IS_DISPLAYED_WHEN_ACCESSED_THROUGH_THE_REVIEW_ORDER_PAGE.png')
        self.driver.save_screenshot(ss_path)
        self.driver.close()
        self.driver.switch_to.window(main_window)

    def verify_TT_C1ASS_is_accessible(self):

        main_window = self.driver.window_handles[0]
        self.click_TT_C1ASS()
        TT_C1ASS_window = self.driver.window_handles[1]
        self.driver.switch_to.window(TT_C1ASS_window)
        ss_path = ('C:\\Users\\jgabriel\OneDrive - Cambridge\\Documents\\GitHub\\Checkout_Regression\\saved_SCREENSHOTS'
                   '\\VERIFY_IF_TT_C1ASS_WINDOW_IS_DISPLAYED_WHEN_ACCESSED_THROUGH_THE_REVIEW_ORDER_PAGE.png')
        self.driver.save_screenshot(ss_path)
        self.driver.close()
        self.driver.switch_to.window(main_window)

    #-------------------------------------------------------------------------------------------------------------------

    YI_TT_B2FSS_PC  = (By.XPATH, "//*[@class='product'][contains(.,'B2')]")

    YI_TT_B2FSS_DEL = (By.XPATH, "//*[@class='product'][contains(.,'B2')]//*[contains(@title,'Remove')]")

    TT_B2FSS_DEC    = (By.XPATH, "//*[@class='product'][contains(.,'B2')]//*[contains(@class,'subtract')]")

    TT_B2FSS_INC    = (By.XPATH, "//*[@class='product'][contains(.,'B2')]//*[contains(@class,'plus')]")

    TT_B2FSS_PRICE  = (By.XPATH, "//*[@class='product'][contains(.,'B2')]//*[contains(@class,'price')]/strong")

    def verify_YI_TT_B2FSS_is_displayed(self):
        return self.driver.find_element(*ReviewOrder.YI_TT_B2FSS_PC).is_displayed()

    def YI_delete_TT_B2FSS(self):
        self.driver.find_element(*ReviewOrder.YI_TT_B2FSS_DEL).click()
        sleep(8)

    def decrease_TT_B2FSS(self):
        self.driver.find_element(*ReviewOrder.TT_B2FSS_DEC).click()
        sleep(8)

    def increase_TT_B2FSS(self):
        self.driver.find_element(*ReviewOrder.TT_B2FSS_INC).click()
        sleep(8)

    def get_TT_B2FSS_price(self):
        return self.driver.find_element(*ReviewOrder.TT_B2FSS_PRICE).text

    YI_TT_C1ASS_PC  = (By.XPATH, "//*[@class='product'][contains(.,'C1')]")

    YI_TT_C1ASS_DEL = (By.XPATH, "//*[@class='product'][contains(.,'C1')]//*[contains(@title,'Remove')]")

    TT_C1ASS_PRICE  = (By.XPATH, "//*[@class='product'][contains(.,'C1')]//*[contains(@class,'price')]/strong")

    def verify_YI_TT_C1ASS_is_displayed(self):
        return self.driver.find_element(*ReviewOrder.YI_TT_C1ASS_PC).is_displayed()

    def YI_delete_TT_C1ASS(self):
        self.driver.find_element(*ReviewOrder.YI_TT_C1ASS_DEL).click()
        sleep(8)

    def get_TT_C1ASS_price(self):
        return self.driver.find_element(*ReviewOrder.TT_C1ASS_PRICE).text

    YI_TT_A2KSSS_PC  = (By.XPATH, "//*[@class='product'][contains(.,'A2')]")

    YI_TT_A2KSSS_DEL = (By.XPATH, "//*[@class='product'][contains(.,'A2')]//*[contains(@title,'Remove')]")

    TT_A2KSSS_PRICE  = (By.XPATH, "//*[@class='product'][contains(.,'A2')]//*[contains(@class,'price')]/span")

    def verify_YI_TT_A2KSSS_is_displayed(self):
        return self.driver.find_element(*ReviewOrder.YI_TT_A2KSSS_PC).is_displayed()

    def YI_delete_TT_A2KSSS(self):
        self.driver.find_element(*ReviewOrder.YI_TT_A2KSSS_DEL).click()
        sleep(8)

    def get_TT_A2KSSS_price(self):
        return self.driver.find_element(*ReviewOrder.TT_A2KSSS_PRICE).text

    YI_TP1_PC  = (By.XPATH, "//*[@class='product'][contains(.,'Test Product 1')]")

    TP1_DEC    = (By.XPATH, "//*[@class='product'][contains(.,'Test Product 1')]//*[contains(@class,'subtract')]")

    TP1_INC    = (By.XPATH, "//*[@class='product'][contains(.,'Test Product 1')]//*[contains(@class,'plus')]")

    TP1_QTY    = (By.XPATH, "//*[@class='product'][contains(.,'Test Product 1')]//*[contains(@id,'qty')]")

    TP1_price = (By.XPATH, "//*[@class='product'][contains(.,'Test Product 1')]//*[contains(@class,'price')]/span")

    YI_TP1_DEL = (By.XPATH, "//*[@class='product'][contains(.,'Test Product 1')]//*[contains(@title,'Remove')]")

    def verify_YI_TP1_is_displayed(self):
        return self.driver.find_element(*ReviewOrder.YI_TP1_PC).is_displayed()

    def decrease_TP1(self):
        self.driver.find_element(*ReviewOrder.TP1_DEC).click()
        sleep(8)

    def verify_decrease_TP1_is_enabled(self):
        return self.driver.find_element(*ReviewOrder.TP1_DEC).is_enabled()

    def increase_TP1(self):
        self.driver.find_element(*ReviewOrder.TP1_INC).click()
        sleep(8)

    def verify_increase_TP1_is_enabled(self):
        return self.driver.find_element(*ReviewOrder.TP1_INC).is_enabled()

    def get_TP1_qty(self):
        return self.driver.find_element(*ReviewOrder.TP1_QTY).get_attribute('value')

    def get_TP1_price(self):
        return self.driver.find_element(*ReviewOrder.TP1_price).text

    def YI_delete_TP1(self):
        self.driver.find_element(*ReviewOrder.YI_TP1_DEL).click()
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

    YI_FP1_PC = (By.XPATH, "//*[@class='product'][contains(.,'Free Product 1')]")

    YI_FP1_DEL = (By.XPATH, "//*[@class='product'][contains(.,'Free Product 1')]//*[contains(@title,'Remove')]")

    def verify_YI_FP1_is_displayed(self):
        return self.driver.find_element(*ReviewOrder.YI_FP1_PC).is_displayed()

    def YI_delete_FP1(self):
        self.driver.find_element(*ReviewOrder.YI_FP1_DEL).click()
        sleep(8)


    # PHYSICAL PRODUCT 1

    YI_PP1_PC = (By.XPATH, "//*[@id='collapseAvailableProducts']//*[@class='product'][contains(.,'Physical Product 1')]")

    PP1_DEC = (By.XPATH, "//*[@class='product'][contains(.,'Physical Product 1')]//*[contains(@class,'subtract')]")

    PP1_INC = (By.XPATH, "//*[@class='product'][contains(.,'Physical Product 1')]//*[contains(@class,'plus')]")

    PP1_QTY = (By.XPATH, "//*[@class='product'][contains(.,'Physical Product 1')]//*[contains(@id,'qty')]")

    PP1_price = (By.XPATH, "//*[@class='product'][contains(.,'Physical Product 1')]//*[contains(@class,'price')]/span")

    YI_PP1_DEL = (By.XPATH, "//*[@id='collapseAvailableProducts']//*[@class='product'][contains(.,'Physical Product 1')]//*[contains(@title,'Remove')]")

    PP1_SFL = (By.XPATH, "//*[@class='product'][contains(.,'Physical Product 1')]//*[contains(text(),'Save for later')]")

    PP1_MTB = (By.XPATH, "//*[@id='collapseBookmarkedItems']//*[@class='product'][contains(.,'Physical Product 1')]//*[contains(@title,'Move to basket')]")

    def verify_YI_PP1_is_displayed(self):
        return self.driver.find_element(*ReviewOrder.YI_PP1_PC).is_displayed()

    def decrease_PP1(self):
        self.driver.find_element(*ReviewOrder.PP1_DEC).click()
        sleep(8)

    def verify_decrease_PP1_is_enabled(self):
        return self.driver.find_element(*ReviewOrder.PP1_DEC).is_enabled()

    def increase_PP1(self):
        self.driver.find_element(*ReviewOrder.PP1_INC).click()
        sleep(8)

    def verify_increase_PP1_is_enabled(self):
        return self.driver.find_element(*ReviewOrder.PP1_INC).is_enabled()

    def get_PP1_qty(self):
        return self.driver.find_element(*ReviewOrder.PP1_QTY).get_attribute('value')

    def get_PP1_price(self):
        return self.driver.find_element(*ReviewOrder.PP1_price).text

    def YI_delete_PP1(self):
        self.driver.find_element(*ReviewOrder.YI_PP1_DEL).click()
        sleep(8)

    #-------------------------------------------------------------------------------------------------------------------

    YI_price = (By.XPATH, "//*[contains(@class,'price')]/span")

    def get_YI_price(self):
        return self.driver.find_elements(*ReviewOrder.YI_price)

    def order_total(self):
        prices = [float(price.text.strip('£')) for price in self.get_YI_price()]

        a = sum(prices)
        b = format(a, '.2f')
        c = str(b)

        d = '£' + c

        return d

    def subtotal(self):
        prices = [float(price.text.strip('£')) for price in self.get_YI_price()]

        a = sum(prices)
        b = format(a, '.2f')

        self.subtotal_b = b  # store b as instance variable

        c = str(b)

        d = '£' + c

        return d

    def ordertotal(self):
        return self.subtotal()

    def all_products_discount(self):
        subtotal = self.subtotal_b # access the instance variable

        a = float(subtotal)
        b = a * 0.25

        self.all_products_discount_b = b

        c = round(b + 1e-9,2) # small delta
        d = '£' + str(c)

        return d

    def specific_product_discount(self):
        a = self.get_TT_A2KSSS_price()
        b = a.replace("£","")

        c = float(b)
        d = c * 0.15

        self.specific_product_discount_d = d

        e = round(d + 1e-9,2) # small delta
        f = '£' + str(e)

        return f

    def all_products_discounted_ordertotal(self):
        subtotal = self.subtotal_b
        discount = self.all_products_discount_b

        a = float(subtotal)
        b = float(discount)
        c = a-b

        d = round(c + 1e-9,2)
        e = '£' + str(d)

        return e

    def specific_product_discounted_ordertotal(self):
        subtotal = self.subtotal_b
        discount = self.specific_product_discount_d

        a = float(subtotal)
        b = float(discount)
        c = a-b

        d = round(c + 1e-9,2)
        e = '£' + str(d)

        return e

    #-------------------------------------------------------------------------------------------------------------------

    Y_items = (By.XPATH, "//*[@class='product']//*[contains(@id,'qty-input')]")

    YI_header = (By.XPATH, "//*[@data-target='#collapseAvailableProducts']")

    itemtotal = (By.XPATH, "//*[contains(@class,'order-description')]//*[contains(text(),'item')]")

    def verify_your_items_is_displayed(self):
        return self.driver.find_element(*ReviewOrder.YI_header).is_displayed()

    def your_items(self):
        return self.driver.find_elements(*ReviewOrder.Y_items)

    def your_items_total(self):
        items = [int(item.get_attribute('value')) for item in self.your_items()]

        a = sum(items)
        b = str(a)

        return b

    def get_your_items_total(self):
        return self.driver.find_element(*ReviewOrder.itemtotal).text

    #-------------------------------------------------------------------------------------------------------------------

    cart_total = (By.XPATH, "//*[contains(@class,'oval')]/span")

    def get_cart_total(self):
        return self.driver.find_element(*ReviewOrder.cart_total).text

    #-------------------------------------------------------------------------------------------------------------------

    ordersummary = (By.XPATH, "//*[@class='order-summary']")

    emptybasket = (By.XPATH, "//*[contains(@class,'empty-basket')]")

    def verify_order_summary_is_displayed(self):
        return self.driver.find_element(*ReviewOrder.ordersummary).is_displayed()

    def verify_empty_basket_is_displayed(self):
        return self.driver.find_element(*ReviewOrder.emptybasket).is_displayed()

    #-------------------------------------------------------------------------------------------------------------------

    item1removed = (By.XPATH, "(//*[@class='undo'])[1]")

    item2removed = (By.XPATH, "(//*[@class='undo'])[2]")

    item3removed = (By.XPATH, "(//*[@class='undo'])[3]")

    def verify_item1_removed_is_displayed(self):
        return self.driver.find_element(*ReviewOrder.item1removed).is_displayed()

    def verify_item2_removed_is_displayed(self):
        return self.driver.find_element(*ReviewOrder.item2removed).is_displayed()

    def verify_item3_removed_is_displayed(self):
        return self.driver.find_element(*ReviewOrder.item3removed).is_displayed()





    #-------------------------------------------------------------------------------------------------------------------

    maximumqtylimitmodal = (By.XPATH, "//*[@class='popover-body']//*[contains(text(),'maximum quantity')]")

    def maximum_qty_limit_modal_is_displayed(self):
        return self.driver.find_element(*ReviewOrder.maximumqtylimitmodal).is_displayed()

    def click_maximum_qty_limit_modal(self):
        return self.driver.find_element(*ReviewOrder.maximumqtylimitmodal).click()

    def verify_maximum_qty_limit_is_displayed(self):
        assert self.maximum_qty_limit_modal_is_displayed() == True
        self.click_maximum_qty_limit_modal()

    #-------------------------------------------------------------------------------------------------------------------

    discountvalue        = (By.XPATH, "//*[contains(@class,'order-discount')]/p/span/strong")

    discountedordertotal = (By.XPATH, "(//*[contains(@class,'sub-total')])[3]/span/strong")

    def get_subtotal(self):
        return self.driver.find_element(*ReviewOrder.subtotalvalue).text.strip()

    def get_ordertotal(self):
        return self.driver.find_element(*ReviewOrder.ordertotalvalue).text.strip()

    def get_discount(self):
        return self.driver.find_element(*ReviewOrder.discountvalue).text.strip()

    def get_discounted_ordertotal(self):
        return self.driver.find_element(*ReviewOrder.discountedordertotal).text.strip()

    #-------------------------------------------------------------------------------------------------------------------

    discountcodecheckbox = (By.XPATH, "//*[@class='order-summary']/div[2]")

    entercode            = (By.XPATH, "//*[@id='discount_input']")

    usecode              = (By.XPATH, "//*[text()=' Use code ']")

    deletediscountcode   = (By.XPATH, "//*[contains(@class,'discount')]/button")

    def click_discountcodecheckbox(self):
        self.driver.find_element(*ReviewOrder.discountcodecheckbox).click()
        sleep(3)

    def enter_code(self):
        return self.driver.find_element(*ReviewOrder.entercode)

    def use_code(self):
        self.driver.find_element(*ReviewOrder.usecode).click()
        sleep(5)

    def use_all_products_discount_code(self):

        i = Data (self.driver)

        self.click_discountcodecheckbox()
        self.enter_code().send_keys(i.C001)
        self.use_code()

    def use_specific_product_discount_code(self):

        i = Data (self.driver)

        self.click_discountcodecheckbox()
        self.enter_code().send_keys(i.C002)
        self.use_code()

    def use_invalid_discount_code(self):

        i = Data (self.driver)

        self.click_discountcodecheckbox()
        self.enter_code().send_keys(i.C003)
        self.use_code()
        sleep(8)

    def use_expired_discount_code(self):

        i = Data (self.driver)

        self.click_discountcodecheckbox()
        self.enter_code().send_keys(i.C004)
        self.use_code()

    def delete_discount_code(self):
        self.driver.find_element(*ReviewOrder.deletediscountcode).click()
        sleep(8)

    #-------------------------------------------------------------------------------------------------------------------

    discountcodeerror = (By.XPATH, "//*[@class='order-summary']//*[@id='coupon_code_error']")

    def verify_discount_code_error_is_displayed(self):
        return self.driver.find_element(*ReviewOrder.discountcodeerror).is_displayed()

    def get_discount_code_error(self):
        return self.driver.find_element(*ReviewOrder.discountcodeerror).text

    def verify_invalid_discount_code_error(self):

        i = Data (self.driver)

        assert self.verify_discount_code_error_is_displayed() == True
        assert self.get_discount_code_error() == i.invalid_discount_code_error

    def verify_expired_discount_code_error(self):

        i = Data (self.driver)

        assert self.verify_discount_code_error_is_displayed() == True
        assert self.get_discount_code_error() == i.expired_discount_code_error

    #-------------------------------------------------------------------------------------------------------------------

    SF_L1DSB_QTY  = (By.XPATH, "//*[@class='product'][contains(.,'Shape')]//*[contains(@id,'qty')]")

    SF_L1DSB_DEC  = (By.XPATH, "//*[@class='product'][contains(.,'Shape')]//*[contains(@class,'subtract')]")

    def get_SF_L1DSB_qty(self):
        return self.driver.find_element(*ReviewOrder.SF_L1DSB_QTY).get_attribute('value')

    def decrease_SF_L1DSB(self):
        self.driver.find_element(*ReviewOrder.SF_L1DSB_DEC).click()
        sleep(8)

    def SF_L1DSB_qty_error_handling(self):

        a = int(self.get_SF_L1DSB_qty())

        while a > 1:
            self.decrease_SF_L1DSB()
            a = int(self.get_SF_L1DSB_qty())


    item_qty = (By.XPATH, "//input[contains(@id, 'qty-input')]")

    def get_item_qty(self, input_item):
        return input_item.get_attribute('value')

    def get_item_assets(self):
        return self.driver.find_elements(*ReviewOrder.item_qty)

    def get_item_assets(self):
        return self.driver.find_elements(*ReviewOrder.item_qty)

    def decrease_qty_to_one_handling(self):
        input_items = self.get_item_assets()

        if input_items:
            for input_item in input_items:
                current_qty = int(self.get_item_qty(input_item))
                if current_qty > 1:
                    qty_input = input_item
                    qty_input.clear()
                    qty_input.send_keys("1")


    delete_buttons = (By.XPATH, "//button[@title='Remove product']")

    def remove_item_buttons(self):
        return self.driver.find_elements(*ReviewOrder.delete_buttons)


    def remove_all_items(self):
        sleep(3)
        delete_buttons = self.remove_item_buttons()

        if delete_buttons:
            for button in delete_buttons:
                button.click()
                sleep(3)






    #-------------------------------------------------------------------------------------------------------------------

    delbp1 = (By.XPATH, "//*[@class='product'][contains(.,'Bookable Product 1')]//*[contains(@title,'Remove')]")

    incbp1qty = (By.XPATH, "//*[@class='product'][contains(.,'Bookable Product 1')]//*[contains(@class,'plus')]")

    decbp1qty = (By.XPATH, "//*[@class='product'][contains(.,'Bookable Product 1')]//*[contains(@class,'subtract')]")

    bp1qty = (By.XPATH, "//*[@class='product'][contains(.,'Bookable Product 1')]//*[contains(@id,'qty')]")

    bp1partiallyavailableerror = (By.XPATH, "//*[@class='product'][contains(.,'Bookable Product 1')]//*[contains(@class,'partially-available')]")

    def delete_BP1(self):
        self.driver.find_element(*ReviewOrder.delbp1).click()
        sleep(8)

    def increase_BP1(self):
        self.driver.find_element(*ReviewOrder.incbp1qty).click()
        sleep(8)

    def decrease_BP1(self):
        self.driver.find_element(*ReviewOrder.decbp1qty).click()
        sleep(8)

    def get_BP1_qty(self):
        return self.driver.find_element(*ReviewOrder.bp1qty).get_attribute('value')

    def verify_BP1_partially_available_error(self):
        return self.driver.find_element(*ReviewOrder.bp1partiallyavailableerror).is_displayed()

    #-------------------------------------------------------------------------------------------------------------------

    unavailableproductsheader = (By.XPATH, "//*[@data-target='#collapseUnavailableProducts']")

    def verify_unavailable_products_is_displayed(self):
        return self.driver.find_element(*ReviewOrder.unavailableproductsheader).is_displayed()

    #-------------------------------------------------------------------------------------------------------------------

    payviagratis = (By.XPATH, "//button[contains(@class, 'payment-btn')]")

    def pay_via_gratis(self):
        self.driver.find_element(*ReviewOrder.payviagratis).click()
        sleep(25)

    def pay_via_gratis_margin(self):
        margin = self.driver.find_element(*ReviewOrder.payviagratis).value_of_css_property('margin-bottom')
        return margin

    payviagratis_btn_price = (By.XPATH, "//button[contains(@class, 'payment-btn')]//strong[text()='£0.00']")

    def gratis_btn_price_check(self):
        text = self.driver.find_element(*ReviewOrder.payviagratis_btn_price).text
        price = text.replace('£', '')
        return price


    price_label = (By.XPATH, "//div[contains(@class, 'price-wrapper')]")

    def gratis_label_check(self):
        text = self.driver.find_element(*ReviewOrder.price_label).text
        return text


    basket_products = (By.XPATH, "//div[@class='product']")

    def basketproducts_displayed(self):
        return self.driver.find_element(*ReviewOrder.basket_products).is_displayed()

    product_qty = (By.XPATH, "//*[contains(@id,'qty-input')]")

    def check_product_qty(self):
        value = self.driver.find_element(*ReviewOrder.product_qty).get_attribute("value")
        print("item qty:", value)
        return value


    cancel_btn = (By.XPATH, "//a[@class='btn btn-link cancel-edit-address']")

    def click_cancel_btn(self):
        self.driver.find_element(*ReviewOrder.cancel_btn).click()
        sleep(5)


    # Address labels


    delivery_label = (By.XPATH, "//div[@class='delivery-address']//div[@class='heading mb-3']")
    billing_label = (By.XPATH, "//div[@class='billing-address']//div[@class='heading mb-3']")

    def billing_address_label(self):
        text = self.driver.find_element(*ReviewOrder.billing_label).text
        return text

    def delivery_address_label(self):
        text = self.driver.find_element(*ReviewOrder.delivery_label).text
        return text


    delivery_add_card   = (By.XPATH, "//div[@class='delivery-address']//div[@class='address-card']")

    billing_add_card    = (By.XPATH, "//div[@class='billing-address']//div[@class='address-card']")

    def delivery_address_card(self):
        return self.driver.find_element(*ReviewOrder.delivery_add_card).is_displayed()

    def billing_address_card(self):
        return self.driver.find_element(*ReviewOrder.billing_add_card).is_displayed()


    billing_checkbox = (By.XPATH, "//div[@class='custom-control custom-checkbox']//input[@id='use-same-address']")
    billing_checkbox_clickable_text = (By.XPATH, "//div[@class='custom-control custom-checkbox']//label[@for='use-same-address']")

    def billing_checkbox_display(self):
        return self.driver.find_element(*ReviewOrder.billing_checkbox).is_displayed()

    def billing_checkbox_text_display(self):
        return self.driver.find_element(*ReviewOrder.billing_checkbox_clickable_text).is_displayed()

    def click_billing_checkbox(self):
        self.driver.find_element(*ReviewOrder.billing_checkbox_clickable_text).click()
        sleep(5)


    def billing_checkbox_istrue(self):
        return self.driver.find_element(*ReviewOrder.billing_checkbox).is_selected()

    def billing_checkbox_desc(self):
        text = self.driver.find_element(*ReviewOrder.billing_checkbox_clickable_text).text
        return text




    #-------------------------------------------------------------------------------------------------------------------

    paynowbuttonprice = (By.XPATH, "//*[contains(@class,'payment-btn')]/span/span")

    def get_pay_now_button_price(self):
        return self.driver.find_element(*ReviewOrder.paynowbuttonprice).text


    flex_charge_text = (By.XPATH, "//small[@class='charge-upon-dispatch']")

    def get_flex_charge_text(self):
        return self.driver.find_element(*ReviewOrder.flex_charge_text).text


    paypal_charge_text = (By.XPATH, "//small[@class='charge-upon-dispatch mt-3']")

    def get_paypal_charge_text(self):
        return self.driver.find_element(*ReviewOrder.paypal_charge_text).text



    def verify_physicalproduct_address(self):
        assert "Delivery details" == self.delivery_address_label()
        try:
            assert self.delivery_address_card() == True
        except NoSuchElementException:
            assert False, "NoSuchElementException occurred, test failed"

        assert "Billing details" == self.billing_address_label()
        assert self.billing_checkbox_istrue() == True
        assert self.billing_checkbox_desc() == "My delivery and billing details are the same"
        try:
            assert self.billing_address_card() == False
        except NoSuchElementException:
            pass

    def verify_physicalproduct_address_uncheck(self):
        assert "Delivery details" == self.delivery_address_label()
        try:
            assert self.delivery_address_card() == True
        except NoSuchElementException:
            assert False, "NoSuchElementException occurred, test failed"

        assert "Billing details" == self.billing_address_label()
        assert self.billing_checkbox_istrue() == False
        assert self.billing_checkbox_desc() == "My delivery and billing details are the same"
        try:
            assert self.billing_address_card() == True
        except NoSuchElementException:
            assert False, "NoSuchElementException occurred, test failed"

    def verify_digitalproduct_address(self):
        assert "Billing details" == self.billing_address_label()
        try:
            assert self.billing_address_card() == True
        except NoSuchElementException:
            assert False, "NoSuchElementException occurred, test failed"

        assert not "Delivery details" in self.page_src()
        try:
            assert self.billing_checkbox_text_display() == False
        except NoSuchElementException:
            pass

    def input_test_billing_details_and_proceed2(self):
        self.input_test_firstname2()
        self.input_test_lastname2()
        self.input_test_country2()
        self.select_test_country2()
        self.input_test_billingaddressline12()
        self.input_test_billingaddressline22()
        self.input_test_city2()
        self.input_test_state2()
        self.input_test_postcode2()
        self.click_updateaddress()


    def input_test_firstname2(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.firstname).send_keys(i.test_firstname2)
        sleep(5)

    def input_test_lastname2(self):
        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.lastname).send_keys(i.test_lastname2)
        sleep(5)

    def input_test_country2(self):
        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.country).send_keys(i.test_country2)
        sleep(5)


    phl = (By.XPATH, "//a[text()='Philippines']")
    def select_test_country2(self):
        self.driver.find_element(*ReviewOrder.phl).click()
        sleep(10)

    def input_test_billingaddressline12(self):
        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.billingaddressline1).send_keys(i.test_billingaddressline12)
        sleep(5)

    def input_test_billingaddressline22(self):
        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.billingaddressline2).send_keys(i.test_billingaddressline22)
        sleep(5)


    def input_test_city2(self):
        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.city).send_keys(i.test_city2)
        sleep(5)


    def input_test_state2(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.state).send_keys(i.test_state2)
        sleep(5)


    def input_test_postcode2(self):

        i = Data(self.driver)

        return self.driver.find_element(*ReviewOrder.postcode).send_keys(i.test_postcode2)
        sleep(5)

# -------------
    google_pay = (By.XPATH, "(//*[@class='card-header'])[3]")


    def CLICK_GOOGLE_PAY(self):
        a = wait_for_element(self.driver, *self.google_pay)
        a.click()
        sleep(15)



    open_google_pay = (By.XPATH, "//*[@id='accordionGooglePay']/div/google-pay-button")


    def OPEN_GOOGLE_PAY(self):
        a = wait_for_element(self.driver, *self.open_google_pay)
        a.click()
        sleep(25)



    def PAY_VIA_GOOGLE_PAY(self):
        self.CLICK_GOOGLE_PAY()
        self.OPEN_GOOGLE_PAY()
