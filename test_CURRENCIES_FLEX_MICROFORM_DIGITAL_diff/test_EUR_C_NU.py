from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_EUR_C(baseclass):

    # @pytestrail.case('')
    def test_EUR_C(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayerAuth      (self.driver)
        g = OrderStatus    (self.driver)

        a.select_eur_c()

        a.add_to_cart_TT_B2FSS()

        eur_c_TT_B2FSS_price = a.get_eur_c_TT_B2FSS_price()

        eur_c_ordertotal = eur_c_subtotal = eur_c_TT_B2FSS_price

        a.click_cart()

        assert eur_c_TT_B2FSS_price == b.get_eur_c_TT_B2FSS_price()
        assert eur_c_subtotal == b.get_eur_c_subtotal()

        b.click_gotocheckout()

        c.input_n_eur_c_emailaddress()

        c.click_continuetocheckout()

        assert eur_c_subtotal == d.get_eur_c_subtotal()

        # d.input_eur_c_billing_details_and_proceed()

        d.input_usd_n_billing_details_and_proceed()

        e.click_card()

        assert eur_c_TT_B2FSS_price == e.get_eur_c_TT_B2FSS_price()
        assert eur_c_subtotal == e.get_eur_c_subtotal()
        assert eur_c_ordertotal == e.get_eur_c_ordertotal()

        assert eur_c_ordertotal == e.get_pay_now_button_price()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        assert eur_c_TT_B2FSS_price == g.get_eur_c_TT_B2FSS_price()
        assert eur_c_ordertotal == g.get_eur_c_ordertotal()

        print("\nEUR-C " + g.get_orderid())

        # END
