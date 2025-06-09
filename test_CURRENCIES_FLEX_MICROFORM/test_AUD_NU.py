from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
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
        f = PayerAuth      (self.driver)
        g = OrderStatus    (self.driver)

        a.select_aud()

        a.add_to_cart_TT_B2FSS()

        aud_TT_B2FSS_price = a.get_aud_TT_B2FSS_price()

        aud_ordertotal = aud_subtotal = aud_TT_B2FSS_price

        a.click_cart()

        assert aud_TT_B2FSS_price == b.get_aud_TT_B2FSS_price()
        assert aud_subtotal       == b.get_aud_subtotal()

        b.click_gotocheckout()

        c.input_n_aud_emailaddress()

        c.click_continuetocheckout()

        assert aud_subtotal == d.get_aud_subtotal()

        d.input_aud_billing_details_and_proceed()

        assert aud_TT_B2FSS_price == e.get_aud_TT_B2FSS_price()
        assert aud_subtotal       == e.get_aud_subtotal()
        assert aud_ordertotal     == e.get_aud_ordertotal()

        e.click_card()

        assert aud_ordertotal == e.get_pay_now_button_price()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        assert aud_TT_B2FSS_price == g.get_aud_TT_B2FSS_price()
        assert aud_ordertotal     == g.get_aud_ordertotal()

        print("\nAUD " + g.get_orderid())

        # END
