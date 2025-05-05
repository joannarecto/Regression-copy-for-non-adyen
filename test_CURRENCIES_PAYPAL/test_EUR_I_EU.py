from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.login       import Login
from page_OBJECTS.paypal      import PayPal
from page_OBJECTS.orderstatus import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_EUR_I(baseclass):

    # @pytestrail.case('')
    def test_EUR_I(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayPal      (self.driver)
        g = OrderStatus (self.driver)

        a.select_eur_i()

        a.add_to_cart_TT_B2FSS()

        eur_i_TT_B2FSS_price = a.get_eur_i_TT_B2FSS_price()

        eur_i_ordertotal = eur_i_subtotal = eur_i_TT_B2FSS_price

        a.click_cart()

        assert eur_i_TT_B2FSS_price == b.get_eur_i_TT_B2FSS_price()
        assert eur_i_subtotal       == b.get_eur_i_subtotal()

        b.click_gotocheckout()

        c.input_e_eur_i_emailaddress()

        c.click_continuetocheckout()

        d.input_eur_i_password()

        d.click_signin()

        assert eur_i_TT_B2FSS_price == e.get_eur_i_TT_B2FSS_price()
        assert eur_i_subtotal       == e.get_eur_i_subtotal()
        assert eur_i_ordertotal     == e.get_eur_i_ordertotal()

        e.pay_via_paypal()

        f.login_and_pay()

        g.view_receipt()

        assert eur_i_TT_B2FSS_price == g.get_eur_i_TT_B2FSS_price()
        assert eur_i_ordertotal     == g.get_eur_i_ordertotal()

        print("\nEUR-I " + g.get_orderid())

        # END
