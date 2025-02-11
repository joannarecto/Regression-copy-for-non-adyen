from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
from page_OBJECTS.orderstatus import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_CAD(baseclass):

    # @pytestrail.case('')
    def test_CAD(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayerAuth   (self.driver)
        g = OrderStatus (self.driver)

        a.select_cad()

        a.add_to_cart_TT_B2FSS()

        cad_TT_B2FSS_price = a.get_cad_TT_B2FSS_price()

        cad_ordertotal = cad_subtotal = cad_TT_B2FSS_price

        a.click_cart()

        assert cad_TT_B2FSS_price == b.get_cad_TT_B2FSS_price()
        assert cad_subtotal       == b.get_cad_subtotal()

        b.click_gotocheckout()

        # c.input_e_cad_emailaddress()

        c.input_e_gbp_emailaddress()

        c.click_continuetocheckout()

        d.input_cad_password()

        d.click_signin()

        e.decrease_qty_to_one_handling()

        e.click_card()

        assert cad_TT_B2FSS_price == e.get_cad_TT_B2FSS_price()
        assert cad_subtotal       == e.get_cad_subtotal()
        assert cad_ordertotal     == e.get_cad_ordertotal()



        assert cad_ordertotal == e.get_pay_now_button_price()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        assert cad_TT_B2FSS_price == g.get_cad_TT_B2FSS_price()
        assert cad_ordertotal     == g.get_cad_ordertotal()

        print("\nCAD " + g.get_orderid())

        # END
