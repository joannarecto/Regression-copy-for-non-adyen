from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus

from utilities.baseclass import baseclass

class Test_USD_N(baseclass):

    def test_USD_N(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayerAuth      (self.driver)
        g = OrderStatus    (self.driver)

        a.select_usd_n()

        a.click_addtobasket1()

        usd_n_itemprice1 = a.get_usd_n_itemprice1()

        usd_n_ordertotal = usd_n_subtotal = usd_n_itemprice1

        a.click_cart()

        assert usd_n_itemprice1 == b.get_usd_n_itemprice1()
        assert usd_n_ordertotal == b.get_usd_n_ordertotal()

        b.click_gotocheckout()

        c.input_n_usd_n_emailaddress()

        c.click_continuetocheckout()

        d.input_usd_n_billing_details_and_proceed()

        assert usd_n_itemprice1 == e.get_usd_n_itemprice1()
        assert usd_n_subtotal   == e.get_usd_n_subtotal()
        assert usd_n_ordertotal == e.get_usd_n_ordertotal()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        assert usd_n_itemprice1 == g.get_usd_n_itemprice1()
        assert usd_n_ordertotal == g.get_usd_n_ordertotal()

        print("\nUSD-N " + g.get_orderid())

        # END
