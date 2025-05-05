from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.login       import Login
from page_OBJECTS.paypal      import PayPal
from page_OBJECTS.orderstatus import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_NZD(baseclass):

    # @pytestrail.case('')
    def test_NZD(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayPal   (self.driver)
        g = OrderStatus (self.driver)

        a.select_nzd()

        a.add_to_cart_PP1()

        nzd_PP1_price = a.get_nzd_PP1_price()

        nzd_ordertotal = nzd_subtotal = nzd_PP1_price

        a.click_cart()

        assert nzd_PP1_price == b.get_nzd_PP1_price()
        assert nzd_subtotal == b.get_nzd_subtotal()

        b.click_gotocheckout()

        c.input_e_nzd_emailaddress()

        c.click_continuetocheckout()

        d.input_nzd_password()

        d.click_signin()

        e.decrease_qty_to_one_handling()

        assert nzd_PP1_price == e.get_nzd_PP1_price()
        assert nzd_subtotal == e.get_nzd_subtotal()
        assert e.get_nzd_total_with_shipping() == e.get_nzd_ordertotal()

        nzd_ordertotal = e.get_nzd_ordertotal()

        e.pay_via_paypal()

        f.login_and_pay()

        g.view_receipt()

        assert nzd_PP1_price == g.get_nzd_PP1_price()
        assert nzd_ordertotal == g.get_nzd_ordertotal()

        print("\nNZD " + g.get_orderid())

        # END
