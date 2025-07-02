from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.login       import Login
from page_OBJECTS.google_pay_page      import GooglePay
from page_OBJECTS.orderstatus import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_GBP(baseclass):

    # @pytestrail.case('')
    def test_GBP(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = GooglePay   (self.driver)
        g = OrderStatus (self.driver)


        a.add_to_cart_TT_B2FSS()

        gbp_TT_B2FSS_price = a.get_gbp_TT_B2FSS_price()

        gbp_ordertotal = gbp_subtotal = gbp_TT_B2FSS_price

        a.click_cart()

        assert gbp_TT_B2FSS_price == b.get_gbp_TT_B2FSS_price()
        assert gbp_subtotal       == b.get_gbp_subtotal()

        b.click_gotocheckout()

        c.input_e_gbp_emailaddress()

        c.click_continuetocheckout()

        d.input_gbp_password()

        d.click_signin()

        e.decrease_qty_to_one_handling()

        assert gbp_TT_B2FSS_price == e.get_gbp_TT_B2FSS_price()
        assert gbp_subtotal       == e.get_gbp_subtotal()
        assert gbp_ordertotal     == e.get_gbp_ordertotal()

        e.PAY_VIA_GOOGLE_PAY()

        f.LOGIN_AND_PAY()

        g.view_receipt()

        assert gbp_TT_B2FSS_price == g.get_gbp_TT_B2FSS_price()
        assert gbp_ordertotal     == g.get_gbp_ordertotal()

        print("\nGBP " + g.get_orderid())

        # END
