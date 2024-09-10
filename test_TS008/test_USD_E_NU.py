from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.paypal         import PayPal
from page_OBJECTS.orderstatus    import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_USD_E(baseclass):

    # @pytestrail.case('')
    def test_USD_E(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayPal         (self.driver)
        g = OrderStatus    (self.driver)

        a.select_usd_e()

        a.add_to_cart_SF_L1DSB()

        usd_e_SF_L1DSB_price = a.get_usd_e_SF_L1DSB_price()

        usd_e_ordertotal = usd_e_subtotal = usd_e_SF_L1DSB_price

        a.click_cart()

        assert usd_e_SF_L1DSB_price == b.get_usd_e_SF_L1DSB_price()
        assert usd_e_subtotal       == b.get_usd_e_subtotal()

        b.click_gotocheckout()

        c.input_n_usd_e_emailaddress()

        c.click_continuetocheckout()

        assert usd_e_subtotal == d.get_usd_e_subtotal()

        d.input_usd_e_billing_details_and_proceed()

        assert usd_e_SF_L1DSB_price == e.get_usd_e_SF_L1DSB_price()
        assert usd_e_subtotal       == e.get_usd_e_subtotal()
        assert usd_e_ordertotal     == e.get_usd_e_ordertotal()

        e.pay_via_paypal()

        f.login_and_pay()

        g.view_receipt()

        assert usd_e_SF_L1DSB_price == g.get_usd_e_SF_L1DSB_price()
        assert usd_e_ordertotal     == g.get_usd_e_ordertotal()

        print("\nUSD-E " + g.get_orderid())

        # END
