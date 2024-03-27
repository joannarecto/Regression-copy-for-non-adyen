from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.paypal import PayPal
from page_OBJECTS.orderstatus    import OrderStatus

from utilities.baseclass import baseclass

class Test_EUR(baseclass):

    def test_EUR(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayPal      (self.driver)
        g = OrderStatus    (self.driver)

        a.select_eur()

        a.click_addtobasket1()

        eur_itemprice1 = a.get_eur_itemprice1()

        eur_ordertotal = eur_subtotal = eur_itemprice1

        a.click_cart()

        assert eur_itemprice1 == b.get_eur_itemprice1()
        assert eur_ordertotal == b.get_eur_ordertotal()

        b.click_gotocheckout()

        c.input_n_eur_emailaddress()

        c.click_continuetocheckout()

        d.input_eur_billing_details_and_proceed()

        assert eur_itemprice1 == e.get_eur_itemprice1()
        assert eur_subtotal   == e.get_eur_subtotal()
        assert eur_ordertotal == e.get_eur_ordertotal()

        e.pay_via_paypal()

        f.login_and_pay()

        g.view_receipt()

        assert eur_itemprice1 == g.get_eur_itemprice1()
        assert eur_ordertotal == g.get_eur_ordertotal()

        print("\nEUR " + g.get_orderid())

        # END
