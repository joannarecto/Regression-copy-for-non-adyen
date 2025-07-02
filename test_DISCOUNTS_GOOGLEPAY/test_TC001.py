from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.paypal      import PayPal
from page_OBJECTS.orderstatus import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_TC001(baseclass):

    # @pytestrail.case('')
    def test_TC001(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayPal      (self.driver)
        g = OrderStatus (self.driver)

        a.add_to_cart_TT_B2FSS()
        TT_B2FSS       = a.get_TT_B2FSS()
        TT_B2FSS_qty   = a.get_TT_B2FSS_qty()
        TT_B2FSS_price = a.get_TT_B2FSS_price()

        a.add_to_cart_TT_C1ASS()
        TT_C1ASS       = a.get_TT_C1ASS()
        TT_C1ASS_qty   = a.get_TT_C1ASS_qty()
        TT_C1ASS_price = a.get_TT_C1ASS_price()

        a.add_to_cart_TT_A2KSSS()
        TT_A2KSSS       = a.get_TT_A2KSSS()
        TT_A2KSSS_qty   = a.get_TT_A2KSSS_qty()
        TT_A2KSSS_price = a.get_TT_A2KSSS_price()

        ordertotal = subtotal = a.get_subtotal()

        a.click_cart()

        assert TT_B2FSS_price  == b.get_TT_B2FSS_price()
        assert TT_C1ASS_price  == b.get_TT_C1ASS_price()
        assert TT_A2KSSS_price == b.get_TT_A2KSSS_price()

        assert subtotal == b.get_subtotal()

        b.click_gotocheckout()

        c.input_e_test_001_emailaddress()

        c.click_continuetocheckout()

        d.input_test_001_password()

        d.click_signin()

        assert TT_B2FSS_price  == b.get_TT_B2FSS_price()
        assert TT_C1ASS_price  == b.get_TT_C1ASS_price()
        assert TT_A2KSSS_price == b.get_TT_A2KSSS_price()

        assert subtotal   == e.get_subtotal()
        assert ordertotal == e.get_ordertotal()

        e.use_all_products_discount_code()

        assert TT_B2FSS_price  == b.get_TT_B2FSS_price()
        assert TT_C1ASS_price  == b.get_TT_C1ASS_price()
        assert TT_A2KSSS_price == b.get_TT_A2KSSS_price()

        assert e.subtotal()                           == e.get_subtotal()
        assert e.all_products_discount()              == e.get_discount()
        assert e.all_products_discounted_ordertotal() == e.get_discounted_ordertotal()

        discount   = e.get_discount()
        ordertotal = e.get_discounted_ordertotal()

        e.PAY_VIA_GOOGLE_PAY()

        f.LOGIN_AND_PAY()

        g.view_receipt()

        assert [TT_B2FSS, TT_C1ASS, TT_A2KSSS]                   == g.get_order_status_items()
        assert [TT_B2FSS_qty, TT_C1ASS_qty, TT_A2KSSS_qty]       == g.get_order_status_items_qty()
        assert [TT_B2FSS_price, TT_C1ASS_price, TT_A2KSSS_price] == g.get_order_status_items_price()

        assert discount               == g.get_discount()
        assert [subtotal, ordertotal] == g.get_order_status_subtotal_and_order_total()

        print("\nTC001 " + g.get_orderid())

        # END
