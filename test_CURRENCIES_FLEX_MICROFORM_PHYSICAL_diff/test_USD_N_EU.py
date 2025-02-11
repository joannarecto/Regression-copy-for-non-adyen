from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
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
        f = PayerAuth   (self.driver)
        g = OrderStatus (self.driver)

        a.select_usd_n()

        a.add_to_cart_PP1()

        usd_n_PP1_price = a.get_usd_n_PP1_price()

        usd_n_ordertotal = usd_n_subtotal = usd_n_PP1_price

        a.click_cart()

        assert usd_n_PP1_price == b.get_usd_n_PP1_price()
        assert usd_n_subtotal       == b.get_usd_n_subtotal()

        b.click_gotocheckout()

        # c.input_e_usd_n_emailaddress()

        c.input_e_eur_c_emailaddress()

        c.click_continuetocheckout()

        d.input_usd_n_password()

        d.click_signin()

        e.decrease_qty_to_one_handling()

        e.click_card()

        assert usd_n_PP1_price == e.get_usd_n_PP1_price()
        assert usd_n_subtotal       == e.get_usd_n_subtotal()
        assert usd_n_ordertotal     == e.get_usd_n_ordertotal()



        assert usd_n_ordertotal == e.get_pay_now_button_price()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        assert usd_n_PP1_price == g.get_usd_n_PP1_price()
        assert usd_n_ordertotal     == g.get_usd_n_ordertotal()

        print("\nUSD-N " + g.get_orderid())

        # END
