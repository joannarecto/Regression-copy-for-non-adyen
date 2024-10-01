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

        a.add_to_cart_TT_B2FSS()

        a.click_cart()

        b.click_gotocheckout()

        c.input_n_test_001_emailaddress()

        c.click_continuetocheckout()

        d.input_test_billing_details_and_proceed()

        #UK

        e.use_discountcode()

        e.assert_discount_code_displayed()

        e.click_edit_address()

        #USA

        e.edit_usa_billing_details_and_update()

        e.use_discountcode()

        e.assert_discount_code_displayed()

        e.remove_discountcode()

        e.click_edit_address()

        #PH

        e.edit_phl_billing_details_and_update()

        e.use_discountcode()

        e.assert_discount_code_displayed()

        e.click_card()
        time.sleep(5)

        assert e.get_cardbutton_totalorder() == "£14.78"

        e.pay_via_card_no_clickcard()

        f.authenticate_payment()

        g.view_receipt()

        try:
            assert g.check_discount_row_displayed() == True
        except NoSuchElementException:
            assert False, "NoSuchElementException occurred, test failed"

        assert g.get_totalorder() == "£14.78"


        print("\nDCESC-599-AC1&AC2 " + g.get_orderid())

        # END
