from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_GBP(baseclass):

    # @pytestrail.case('')
    def test_GBP(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayerAuth      (self.driver)
        g = OrderStatus    (self.driver)

        # a.select_gbp()
        a.add_to_cart_PS1()

        a.go_to_page2()

        a.add_to_cart_TT_B2FSS()

        a.get_gbp_TT_B2FSS_price()

        gbp_mixed_price = a.get_gbp_mixed_price()

        gbp_ordertotal = gbp_subtotal = gbp_mixed_price

        a.click_cart()

        assert gbp_mixed_price == b.get_gbp_mixed_price()
        assert gbp_subtotal       == b.get_gbp_subtotal()

        b.click_gotocheckout()

        c.input_n_gbp_emailaddress()

        c.click_continuetocheckout()

        assert gbp_subtotal == d.get_gbp_subtotal()

        # d.input_gbp_billing_details_and_proceed()

        d.input_nzd_billing_details_and_proceed()

        e.click_card()

        assert gbp_mixed_price == e.get_gbp_mixed_price()
        assert gbp_subtotal       == e.get_gbp_subtotal()
        assert gbp_ordertotal     == e.get_gbp_ordertotal()



        assert gbp_ordertotal == e.get_pay_now_button_price()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        assert gbp_mixed_price == g.get_gbp_mixed_price()
        assert gbp_ordertotal     == g.get_gbp_ordertotal()

        print("\nGBP " + g.get_orderid())

        # END
