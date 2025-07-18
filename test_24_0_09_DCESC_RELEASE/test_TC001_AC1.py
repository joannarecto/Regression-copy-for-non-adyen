#DCESC-599-AC1&AC2
import time

from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus

from selenium.common.exceptions import NoSuchElementException



from utilities.baseclass import baseclass

class Test_TC001(baseclass):

    def test_TC001(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayerAuth      (self.driver)
        g = OrderStatus    (self.driver)


        # qa
        # uk_price_after_discount = "£15.00"
        # usa_price_after_discount = "US $17.25"
        # ph_price_after_discount = "US $17.25"

        # stg
        uk_price_after_discount = "£14.78"
        usa_price_after_discount = "US $49.50"
        ph_price_after_discount = "US $33.00"


        a.add_to_cart_TT_B2FSS()

        a.click_cart()

        b.click_gotocheckout()

        c.input_n_test_001_emailaddress()

        c.click_continuetocheckout()

        d.input_test_billing_details_and_proceed()

        #UK

        e.use_discountcode()

        e.assert_discountcode_section_displayed()

        assert e.get_gbp_ordertotal() == uk_price_after_discount

        e.click_edit_billingaddress()

        #USA

        e.edit_usa_billing_details_and_update()

        e.use_discountcode()

        e.assert_discountcode_section_displayed()

        assert e.get_usd_n_ordertotal() == usa_price_after_discount

        e.remove_discountcode()

        e.click_edit_billingaddress()

        #PH

        e.edit_phl_billing_details_and_update()

        e.use_discountcode()

        e.assert_discountcode_section_displayed()

        assert e.get_usd_e_ordertotal() == ph_price_after_discount

        e.click_card()

        assert e.get_pay_now_button_price() == ph_price_after_discount

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        try:
            assert g.check_discount_row_displayed() == True
        except NoSuchElementException:
            assert False, "NoSuchElementException occurred, test failed"

        assert g.get_usd_e_ordertotal() == ph_price_after_discount

        print(g.get_usd_e_ordertotal())
        print(ph_price_after_discount)


        print("\nDCESC-599-AC1&AC2 " + g.get_orderid())

        # END
