from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.login       import Login
from page_OBJECTS.google_pay_page      import GooglePay
from page_OBJECTS.orderstatus import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_USD_N(baseclass):

    # @pytestrail.case('')
    def test_USD_N(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = GooglePay   (self.driver)
        g = OrderStatus (self.driver)

        a.select_usd_n()

        a.add_to_cart_TT_B2FSS()

        usd_n_TT_B2FSS_price = a.get_usd_n_TT_B2FSS_price()

        usd_n_ordertotal = usd_n_subtotal = usd_n_TT_B2FSS_price

        a.click_cart()

        assert usd_n_TT_B2FSS_price == b.get_usd_n_TT_B2FSS_price()
        assert usd_n_subtotal       == b.get_usd_n_subtotal()

        b.click_gotocheckout()

        c.input_e_usd_n_emailaddress()

        c.click_continuetocheckout()

        d.input_usd_n_password()

        d.click_signin()

        assert usd_n_TT_B2FSS_price == e.get_usd_n_TT_B2FSS_price()
        assert usd_n_subtotal       == e.get_usd_n_subtotal()
        assert usd_n_ordertotal     == e.get_usd_n_ordertotal()

        e.PAY_VIA_GOOGLE_PAY()

        f.LOGIN_AND_PAY()

        g.view_receipt()

        assert usd_n_TT_B2FSS_price == g.get_usd_n_TT_B2FSS_price()
        assert usd_n_ordertotal     == g.get_usd_n_ordertotal()

        print("\nUSD-N " + g.get_orderid())

        # END
