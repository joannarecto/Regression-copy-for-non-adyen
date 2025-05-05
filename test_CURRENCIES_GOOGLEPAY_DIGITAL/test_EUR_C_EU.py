from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.login       import Login
from page_OBJECTS.google_pay_page      import GooglePay
from page_OBJECTS.orderstatus import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_EUR_C(baseclass):

    # @pytestrail.case('')
    def test_EUR_C(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = GooglePay   (self.driver)
        g = OrderStatus (self.driver)

        a.select_eur_c()

        a.add_to_cart_TT_B2FSS()

        eur_c_TT_B2FSS_price = a.get_eur_c_TT_B2FSS_price()

        eur_c_ordertotal = eur_c_subtotal = eur_c_TT_B2FSS_price

        a.click_cart()

        assert eur_c_TT_B2FSS_price == b.get_eur_c_TT_B2FSS_price()
        assert eur_c_subtotal       == b.get_eur_c_subtotal()

        b.click_gotocheckout()

        c.input_e_eur_c_emailaddress()

        c.click_continuetocheckout()

        d.input_eur_c_password()

        d.click_signin()

        assert eur_c_TT_B2FSS_price == e.get_eur_c_TT_B2FSS_price()
        assert eur_c_subtotal       == e.get_eur_c_subtotal()
        assert eur_c_ordertotal     == e.get_eur_c_ordertotal()

        e.PAY_VIA_GOOGLE_PAY()

        f.LOGIN_AND_PAY()

        g.view_receipt()

        assert eur_c_TT_B2FSS_price == g.get_eur_c_TT_B2FSS_price()
        assert eur_c_ordertotal     == g.get_eur_c_ordertotal()

        print("\nEUR-C " + g.get_orderid())

        # END
