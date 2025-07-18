#DCESC-598-SC1

from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus
from selenium.common.exceptions import NoSuchElementException


from utilities.baseclass import baseclass

class Test_TC003(baseclass):

    def test_TC003(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayerAuth      (self.driver)
        g = OrderStatus    (self.driver)

        a.add_to_cart_TT_B2FSS()

        a.click_cart()

        b.click_chevron()

        a.buy_now_TT_C1ASS()

        c.click_cartbtn()

        try:
            assert b.basketproducts_displayed() == True
        except NoSuchElementException:
            assert False, "NoSuchElementException occurred, test failed"

        assert not "Your basket is empty" in b.page_src()

        b.click_gotocheckout()

        c.input_n_test_003_emailaddress()

        c.click_continuetocheckout()

        d.input_test_billing_details_and_proceed()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        print("\nDCESC-598 " + g.get_orderid())

        # END