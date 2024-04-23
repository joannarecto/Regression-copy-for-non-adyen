#DCESC-579_4

from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.orderstatus    import OrderStatus

from page_OBJECTS.paypal         import PayPal


from utilities.baseclass import baseclass

class Test_TC004(baseclass):

    def test_TC004(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayPal         (self.driver)
        g = OrderStatus    (self.driver)


        a.click_addtobasket1()

        a.click_cart()

        b.click_gotocheckout()

        c.input_n_test_004_emailaddress()

        c.click_continuetocheckout()

        d.input_tur_billing_details_searchaddress_and_proceed()

        e.pay_via_paypal()

        f.login_and_pay()

        g.view_receipt()

        print("\nDCESC-579_4 " + g.get_orderid())

        # END
