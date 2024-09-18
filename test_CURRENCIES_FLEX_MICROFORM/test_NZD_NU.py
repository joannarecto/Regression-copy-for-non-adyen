from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_NZD(baseclass):

    # @pytestrail.case('')
    def test_NZD(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayerAuth      (self.driver)
        g = OrderStatus    (self.driver)

        a.select_nzd()

        a.add_to_cart_TT_B2FSS()

        nzd_TT_B2FSS_price = a.get_nzd_TT_B2FSS_price()

        nzd_ordertotal = nzd_subtotal = nzd_TT_B2FSS_price

        a.click_cart()

        assert nzd_TT_B2FSS_price == b.get_nzd_TT_B2FSS_price()
        assert nzd_subtotal       == b.get_nzd_subtotal()

        b.click_gotocheckout()

        c.input_n_nzd_emailaddress()

        c.click_continuetocheckout()

        assert nzd_subtotal == d.get_nzd_subtotal()

        d.input_nzd_billing_details_and_proceed()

        assert nzd_TT_B2FSS_price == e.get_nzd_TT_B2FSS_price()
        assert nzd_subtotal       == e.get_nzd_subtotal()
        assert nzd_ordertotal     == e.get_nzd_ordertotal()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        assert nzd_TT_B2FSS_price == g.get_nzd_TT_B2FSS_price()
        assert nzd_ordertotal     == g.get_nzd_ordertotal()

        print("\nNZD " + g.get_orderid())

        # END
