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

    receipt2 = (By.XPATH, "//div[@class='purchase-receipt']")
    def view_receipt2(self):
        self.driver.find_element(*OrderStatus.receipt2).click()
        sleep(5)


    yourinformation = (By.XPATH, "//div[@class='customer-information']")
    def view_customer_information(self):
        self.driver.find_element(*OrderStatus.yourinformation).click()
        sleep(5)

    def view_customer_information_available(self):
        self.driver.find_element(*OrderStatus.yourinformation).is_displayed()
        sleep(5)

    #-------------------------------------------------------------------------------------------------------------------

    orderid = (By.XPATH, "//*[contains(text(),'Order number')]")

    orderid2 = (By.XPATH, "//*[contains(text(),'Numero dell')]")

    orderid3 = (By.XPATH, "//*[contains(text(),'Número de encomenda')]")

    def get_orderid(self):
        return self.driver.find_element(*OrderStatus.orderid).text
        sleep(5)

    def get_orderid2(self):
        return self.driver.find_element(*OrderStatus.orderid2).text
        sleep(5)

    def get_orderid3(self):
        return self.driver.find_element(*OrderStatus.orderid3).text
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
        return self.driver.find_element(*OrderStatus.itemprice1).text.replace("\n", "")

    def get_itemprice1_without_whitespace(self):
        return self.driver.find_element(*OrderStatus.itemprice1).text.strip()

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

    #-------------------------------------------------------------------------------------------------------------------
    def get_aud_FP1_price(self):
        return self.get_itemprice1_with_whitespace()

    def get_cad_FP1_price(self):
        return self.get_itemprice1_with_whitespace()

    def get_eur_c_FP1_price(self):
        return self.get_itemprice1_with_whitespace()

    def get_eur_i_FP1_price(self):
        return self.get_itemprice1_with_whitespace()

    def get_eur_FP1_price(self):
        return self.get_itemprice1_with_whitespace()

    def get_gbp_FP1_price(self):
        return self.get_itemprice1_with_whitespace()

    def get_nzd_FP1_price(self):
        return self.get_itemprice1_with_whitespace()

    def get_usd_FP1_price(self):
        return self.get_itemprice1_with_whitespace()

    def get_usd_e_FP1_price(self):
        return self.get_itemprice1_with_whitespace()

    def get_usd_n_FP1_price(self):
        return self.get_itemprice1_with_whitespace()

    #-------------------------------------------------------------------------------------------------------------------

    subtotalvalue = (By.XPATH, "//p[contains(text(),'Subtotal')]/following-sibling::span/strong")

    def get_subtotal_with_whitespace(self):
        return self.driver.find_element(*OrderStatus.subtotalvalue).text.replace(" \n", " ")

    def get_subtotal_without_whitespace(self):
        return self.driver.find_element(*OrderStatus.subtotalvalue).text.strip()

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

    # -------------------------------------------------------------------------------------------------------------------
    ordertotalvalue = (By.XPATH, "//p[contains(text(),'Order Total')]/following-sibling::span")

    def get_ordertotal_with_whitespace(self):
        return self.driver.find_element(*OrderStatus.ordertotalvalue).text.replace(" \n", " ")

    def get_ordertotal_without_whitespace(self):
        return self.driver.find_element(*OrderStatus.ordertotalvalue).text.strip()

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

    # -------------------------------------------------------------------------------------------------------------------
    deliverycharge = (By.XPATH, "//p[contains(text(),'Delivery')]/following-sibling::p/span")

    def get_deliverycharge_with_whitespace(self):
        return self.driver.find_element(*OrderStatus.deliverycharge).text.replace(" \n", " ")

    def get_deliverycharge_without_whitespace(self):
        return self.driver.find_element(*OrderStatus.deliverycharge).text.strip()

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
        return self.driver.find_element(*OrderStatus.shippingcharge).text.replace(" \n", " ")

    def get_shippingcharge_without_whitespace(self):
        return self.driver.find_element(*OrderStatus.shippingcharge).text.strip()

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
        return self.driver.find_element(*OrderStatus.delivery_date).text

    delivery_days =  (By.XPATH, "(//div[@class='shipping-details']//div//span)[last()]")
    def estimate_delivery_days(self):
        return self.driver.find_element(*OrderStatus.delivery_days).text

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

    #------------------------------------------------------------------------------------------------------------------

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

    items                 = (By.XPATH, "//*[contains(text(),'Item')]/span")

    itemsqty              = (By.XPATH, "//*[contains(text(),'Qty')]/span")

    itemsprice            = (By.XPATH, "//*[contains(@class,'my-2')]/div[2]/span")

    subtotalandordertotal = (By.XPATH, "//*[@class='col-3 text-right m-0']/strong")

    def orderstatus_items(self):
        return self.driver.find_elements(*OrderStatus.items)

    def orderstatus_items_qty(self):
        return self.driver.find_elements(*OrderStatus.itemsqty)

    def orderstatus_items_price(self):
        return self.driver.find_elements(*OrderStatus.itemsprice)

    def orderstatus_subtotal_and_order_total(self):
        return self.driver.find_elements(*OrderStatus.subtotalandordertotal)

    def orderstatus_items_set(self):
        sleep(5)
        basket_items = [item.text for item in self.orderstatus_items()]
        print("\nNumber of items in Review order page:", len(basket_items))
        print("List of items in Review order page:", basket_items)
        return basket_items

    def get_order_status_items(self):
        basket_items = [item.text for item in self.orderstatus_items()]
        return basket_items

    def get_order_status_items_qty(self):
        basket_items = [item.text for item in self.orderstatus_items_qty()]
        return basket_items

    def get_order_status_items_price(self):
        basket_items = [item.text for item in self.orderstatus_items_price()]
        return basket_items

    def get_order_status_subtotal_and_order_total(self):
        basket_items = [item.text for item in self.orderstatus_subtotal_and_order_total()]
        return basket_items

    #-------------------------------------------------------------------------------------------------------------------

    fail_subheader = (By.XPATH, "//label[@for='street_2']")
    def fail_subheader_msg(self):
        text = self.driver.find_element(*OrderStatus.fail_subheader).text
        return text

    #-------------------------------------------------------------------------------------------------------------------

    discount = (By.XPATH, "//*[contains(@class,'discount')]/p[2]/span/strong")

    def get_discount(self):
        return self.driver.find_element(*OrderStatus.discount).text



    #-------------------------------------------------------------------------------------------------------------------

    bill_fullname           = (By.XPATH, "//div[@class='billing-address mb-3']/span[1]")
    bill_addressline1       = (By.XPATH, "//div[@class='billing-address mb-3']/span[2]")
    bill_addressline2       = (By.XPATH, "//div[@class='billing-address mb-3']/span[3]")
    bill_city               = (By.XPATH, "//div[@class='billing-address mb-3']/span[4]")
    bill_state              = (By.XPATH, "//div[@class='billing-address mb-3']/span[5]")
    bill_postcode           = (By.XPATH, "//div[@class='billing-address mb-3']/span[6]")
    bill_country            = (By.XPATH, "//div[@class='billing-address mb-3']/span[7]")

    def get_billing_fullname(self):
        text = self.driver.find_element(*OrderStatus.bill_fullname).text
        value = text.strip().replace(",", "")
        return value

    def get_billing_country(self):
        text = self.driver.find_element(*OrderStatus.bill_country).text
        value = text.strip().replace(",", "")
        return value

    def get_billing_addressline1(self):
        text = self.driver.find_element(*OrderStatus.bill_addressline1).text
        value = text.strip().replace(",", "")
        return value

    def get_billing_addressline2(self):
        text = self.driver.find_element(*OrderStatus.bill_addressline2).text
        value = text.strip().replace(",", "")
        return value

    def get_billing_city(self):
        text = self.driver.find_element(*OrderStatus.bill_city).text
        value = text.strip().replace(",", "")
        return value

    def get_billing_state(self):
        text = self.driver.find_element(*OrderStatus.bill_state).text
        value = text.strip().replace(",", "")
        return value

    def get_billing_postcode(self):
        text = self.driver.find_element(*OrderStatus.bill_postcode).text
        value = text.strip().replace(",", "")
        return value

    del_fullname        = (By.XPATH, "//div[@class='delivery-address mb-3']/span[1]")
    del_addressline1    = (By.XPATH, "//div[@class='delivery-address mb-3']/span[2]")
    del_addressline2    = (By.XPATH, "//div[@class='delivery-address mb-3']/span[3]")
    del_city            = (By.XPATH, "//div[@class='delivery-address mb-3']/span[4]")
    del_state           = (By.XPATH, "//div[@class='delivery-address mb-3']/span[5]")
    del_postcode        = (By.XPATH, "//div[@class='delivery-address mb-3']/span[6]")
    del_country         = (By.XPATH, "//div[@class='delivery-address mb-3']/span[7]")

    def get_delivery_fullname(self):
        text = self.driver.find_element(*OrderStatus.del_fullname).text
        value = text.strip().replace(",", "")
        return value

    def get_delivery_country(self):
        text = self.driver.find_element(*OrderStatus.del_country).text
        value = text.strip().replace(",", "")
        return value

    def get_delivery_addressline1(self):
        text = self.driver.find_element(*OrderStatus.del_addressline1).text
        value = text.strip().replace(",", "")
        return value

    def get_delivery_addressline2(self):
        text = self.driver.find_element(*OrderStatus.del_addressline2).text
        value = text.strip().replace(",", "")
        return value

    def get_delivery_city(self):
        text = self.driver.find_element(*OrderStatus.del_city).text
        value = text.strip().replace(",", "")
        return value

    def get_delivery_state(self):
        text = self.driver.find_element(*OrderStatus.del_state).text
        value = text.strip().replace(",", "")
        return value

    def get_delivery_postcode(self):
        text = self.driver.find_element(*OrderStatus.del_postcode).text
        value = text.strip().replace(",", "")
        return value



