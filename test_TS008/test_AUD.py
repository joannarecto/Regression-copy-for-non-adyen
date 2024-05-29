from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.paypal         import PayPal
from page_OBJECTS.orderstatus    import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_AUD(baseclass):

    # @pytestrail.case('')
    def test_AUD(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayPal         (self.driver)
        g = OrderStatus    (self.driver)

        a.select_aud()

        a.click_addtobasket1()

        aud_itemprice1 = a.get_aud_itemprice1()

        aud_ordertotal = aud_subtotal = aud_itemprice1

        a.click_cart()

        assert aud_itemprice1 == b.get_aud_itemprice1()
        assert aud_ordertotal == b.get_aud_ordertotal()

        b.click_gotocheckout()

        c.input_n_aud_emailaddress()

        c.click_continuetocheckout()

        assert aud_subtotal == d.get_aud_subtotal()

        d.input_aud_billing_details_and_proceed()

        assert aud_itemprice1 == e.get_aud_itemprice1()
        assert aud_subtotal   == e.get_aud_subtotal()
        assert aud_ordertotal == e.get_aud_ordertotal()

        e.pay_via_paypal()

        f.login_and_pay()

        g.view_receipt()

        assert aud_itemprice1 == g.get_aud_itemprice1()
        assert aud_ordertotal == g.get_aud_ordertotal()

        print("\nAUD " + g.get_orderid())

        # END
