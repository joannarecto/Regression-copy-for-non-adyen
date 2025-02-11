from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_EUR_I(baseclass):

    # @pytestrail.case('')
    def test_EUR_I(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayerAuth      (self.driver)
        g = OrderStatus    (self.driver)

        a.select_eur_i()

        a.add_to_cart_PP1()

        eur_i_PP1_price = a.get_eur_i_PP1_price()

        eur_i_ordertotal = eur_i_subtotal = eur_i_PP1_price

        a.click_cart()

        assert eur_i_PP1_price == b.get_eur_i_PP1_price()
        assert eur_i_subtotal       == b.get_eur_i_subtotal()

        b.click_gotocheckout()

        c.input_n_eur_i_emailaddress()

        c.click_continuetocheckout()

        assert eur_i_subtotal == d.get_eur_i_subtotal()

        d.input_eur_i_billing_details_and_proceed()

        e.click_card()

        assert eur_i_PP1_price == e.get_eur_i_PP1_price()
        assert eur_i_subtotal       == e.get_eur_i_subtotal()
        assert eur_i_ordertotal     == e.get_eur_i_ordertotal()



        assert eur_i_ordertotal == e.get_pay_now_button_price()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        assert eur_i_PP1_price == g.get_eur_i_PP1_price()
        assert eur_i_ordertotal     == g.get_eur_i_ordertotal()

        print("\nEUR-I " + g.get_orderid())

        # END
