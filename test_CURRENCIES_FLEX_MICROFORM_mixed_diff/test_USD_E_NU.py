from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
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
        f = PayerAuth      (self.driver)
        g = OrderStatus    (self.driver)

        a.select_usd_e()

        a.add_to_cart_SF_L1DSB()
        a.add_to_cart_OAA_L1TRD()

        usd_e_mixed_price = a.get_usd_e_mixed_price()

        usd_e_ordertotal = usd_e_subtotal = usd_e_mixed_price

        a.click_cart()

        assert usd_e_mixed_price == b.get_usd_e_mixed_price()
        assert usd_e_subtotal       == b.get_usd_e_subtotal()

        b.click_gotocheckout()

        c.input_n_usd_e_emailaddress()

        c.click_continuetocheckout()

        assert usd_e_subtotal == d.get_usd_e_subtotal()

        # d.input_usd_e_billing_details_and_proceed()

        d.input_usd_n_billing_details_and_proceed()

        e.click_card()

        assert usd_e_mixed_price == e.get_usd_e_mixed_price()
        assert usd_e_subtotal       == e.get_usd_e_subtotal()
        assert usd_e_ordertotal     == e.get_usd_e_ordertotal()




        assert usd_e_ordertotal == e.get_pay_now_button_price()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        assert usd_e_mixed_price == g.get_usd_e_mixed_price()
        assert usd_e_ordertotal     == g.get_usd_e_ordertotal()


        print("\nUSD-E " + g.get_orderid())

        # END
