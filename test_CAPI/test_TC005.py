#DCESC-554 (AC1 & AC3)

from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus
from selenium.webdriver.common.by import By

from utilities.baseclass import baseclass

class Test_TC005(baseclass):

    def test_TC005(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayerAuth      (self.driver)
        g = OrderStatus    (self.driver)


        a.add_to_cart_PP1()

        a.click_cart()

        b.click_gotocheckout()

        c.input_n_test_001_emailaddress()

        c.click_continuetocheckout()




        # def input_tur_billing_details_searchaddress_only_p1(self):
        d.input_test_firstname()
        d.input_test_lastname()
        d.click_searchaddress()
        d.click_change_country_btn()
        d.driver.find_element(*BillingDetails.search_address).send_keys(d.countryname)

        # d.input_tur_billing_details_searchaddress_only_p2()
        d.driver.find_element(d.country_search).click()
        d.driver.find_element(d.search_address).send_keys(1)
        d.driver.find_element(d.country_address_search).click()



        d.click_gotorevieworder()
        #
        # e.click_edit_billingaddress()
        #
        #
        # e.click_updateaddress()
        #
        # e.pay_via_card()
        #
        # f.authenticate_payment()
        #
        # g.view_receipt()
        #
        # print("\nDCESC-554 " + g.get_orderid())
        #
        # # END
