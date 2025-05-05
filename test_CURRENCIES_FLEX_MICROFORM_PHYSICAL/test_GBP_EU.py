from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
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
        f = PayerAuth   (self.driver)
        g = OrderStatus (self.driver)

        # a.select_gbp()

        a.add_to_cart_PP1()

        gbp_PP1_price = a.get_gbp_PP1_price()

        gbp_ordertotal = gbp_subtotal = gbp_PP1_price

        a.click_cart()

        assert gbp_PP1_price == b.get_gbp_PP1_price()
        assert gbp_subtotal       == b.get_gbp_subtotal()

        b.click_gotocheckout()

        c.input_e_gbp_emailaddress()

        c.click_continuetocheckout()

        d.input_gbp_password()

        d.click_signin()

        e.decrease_qty_to_one_handling()

        e.click_card()

        assert gbp_PP1_price == e.get_gbp_PP1_price()
        assert gbp_subtotal       == e.get_gbp_subtotal()
        assert e.get_gbp_total_with_shipping() == e.get_gbp_ordertotal()

        gbp_ordertotal = e.get_gbp_ordertotal()

        assert gbp_ordertotal == e.get_pay_now_button_price()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        assert gbp_PP1_price == g.get_gbp_PP1_price()
        assert gbp_ordertotal     == g.get_gbp_ordertotal()

        print("\nGBP " + g.get_orderid())

        # END
