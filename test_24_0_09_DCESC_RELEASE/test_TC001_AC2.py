#DCESC-599-AC1&AC3

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

        a.add_to_cart_TT_B2FSS()

        a.click_cart()

        b.click_gotocheckout()

        c.input_n_test_002_emailaddress()

        c.click_continuetocheckout()

        #BRA

        d.input_bra_billing_details_and_proceed()

        e.use_discountcode()

        error_msg = "This code is not available in your country"

        e.assert_error_discount_code_displayed()
        assert e.check_discount_error_text() == error_msg

        e.click_edit_address()

        #POL

        e.edit_pol_billing_details_and_update()

        e.use_discountcode()

        e.assert_error_discount_code_displayed()
        assert e.check_discount_error_text() == error_msg

        e.click_edit_address()

        #IND

        e.edit_ind_billing_details_and_update()

        e.use_discountcode()

        e.assert_error_discount_code_displayed()
        assert e.check_discount_error_text() == error_msg

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        try:
            assert g.check_discount_row_displayed() == False
        except NoSuchElementException:
            pass


        print("\nDCESC-599-AC1&AC23 " + g.get_orderid())

        # END
