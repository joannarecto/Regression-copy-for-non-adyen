#DCESC-595

from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.paypal      import PayPal
from page_OBJECTS.orderstatus    import OrderStatus

from selenium.common.exceptions import NoSuchElementException
from utilities.baseclass import baseclass

class Test_TC009(baseclass):

    def test_TC009(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayPal      (self.driver)
        g = OrderStatus    (self.driver)

        a.add_to_cart_TT_B2FSS()

        a.click_cart()

        b.click_gotocheckout()

        c.input_n_test_009_emailaddress()

        c.click_continuetocheckout()

        d.input_test_billing_details_and_proceed()

        e.pay_via_paypal()

        f.login_and_pay()

        try:
            assert g.cartoval_displayed() == False
        except NoSuchElementException:
            pass

        g.view_receipt()

        print("\nTC009 " + g.get_orderid())

        g.click_backtoshopping()

        try:
            assert a.cartoval_displayed() == False
        except NoSuchElementException:
            pass

        # END
