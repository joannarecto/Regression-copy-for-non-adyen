#DCESC-598-SC2

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

    def test_TC002(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayerAuth      (self.driver)
        g = OrderStatus    (self.driver)

        a.buy_now_TT_B2FSS()

        c.click_cartbtn()

        try:
            assert b.basketproducts_displayed() == True
        except NoSuchElementException:
            assert False, "NoSuchElementException occurred, test failed"

        assert not "Your basket is empty" in b.page_src()

        b.click_gotocheckout()

        c.input_n_test_002_emailaddress()

        c.click_continuetocheckout()

        d.input_test_billing_details_and_proceed()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        print("\nDCESC-598-SC2 " + g.get_orderid())

        # END