from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.paypal         import PayPal
from page_OBJECTS.orderstatus    import OrderStatus

from utilities.baseclass import baseclass

class Test_NZD(baseclass):

    def test_NZD(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayPal         (self.driver)
        g = OrderStatus    (self.driver)

        a.select_nzd()

        a.click_addtobasket1()

        nzd_itemprice1 = a.get_nzd_itemprice1()

        nzd_ordertotal = nzd_subtotal = nzd_itemprice1

        a.click_cart()

        assert nzd_itemprice1 == b.get_nzd_itemprice1()
        assert nzd_ordertotal == b.get_nzd_ordertotal()

        b.click_gotocheckout()

        c.input_n_nzd_emailaddress()

        c.click_continuetocheckout()

        assert nzd_subtotal == d.get_nzd_subtotal()

        d.input_nzd_billing_details_and_proceed()

        assert nzd_itemprice1 == e.get_nzd_itemprice1()
        assert nzd_subtotal   == e.get_nzd_subtotal()
        assert nzd_ordertotal == e.get_nzd_ordertotal()

        e.pay_via_paypal()

        f.login_and_pay()

        g.view_receipt()

        assert nzd_itemprice1 == g.get_nzd_itemprice1()
        assert nzd_ordertotal == g.get_nzd_ordertotal()

        print("\nNZD " + g.get_orderid())

        # END
