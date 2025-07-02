from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.login       import Login
from page_OBJECTS.google_pay_page      import GooglePay
from page_OBJECTS.orderstatus import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_AUD(baseclass):

    # @pytestrail.case('')
    def test_AUD(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = GooglePay   (self.driver)
        g = OrderStatus (self.driver)

        a.select_aud()

        a.add_to_cart_TT_B2FSS()

        aud_TT_B2FSS_price = a.get_aud_TT_B2FSS_price()

        aud_ordertotal = aud_subtotal = aud_TT_B2FSS_price

        a.click_cart()

        assert aud_TT_B2FSS_price == b.get_aud_TT_B2FSS_price()
        assert aud_subtotal       == b.get_aud_subtotal()

        b.click_gotocheckout()

        c.input_e_aud_emailaddress()

        c.click_continuetocheckout()

        d.input_aud_password()

        d.click_signin()

        e.decrease_qty_to_one_handling()

        assert aud_TT_B2FSS_price == e.get_aud_TT_B2FSS_price()
        assert aud_subtotal       == e.get_aud_subtotal()
        assert aud_ordertotal     == e.get_aud_ordertotal()

        e.PAY_VIA_GOOGLE_PAY()

        f.LOGIN_AND_PAY()

        g.view_receipt()

        assert aud_TT_B2FSS_price == g.get_aud_TT_B2FSS_price()
        assert aud_ordertotal     == g.get_aud_ordertotal()

        print("\nAUD " + g.get_orderid())

        # END
