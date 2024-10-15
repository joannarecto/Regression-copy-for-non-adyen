from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
from page_OBJECTS.orderstatus import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_TC004(baseclass):

    # @pytestrail.case('')
    def test_TC004(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayerAuth   (self.driver)
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

        c.input_e_test_004_emailaddress()

        c.click_continuetocheckout()

        d.input_test_004_password()

        d.click_signin()

        assert TT_B2FSS_price  == b.get_TT_B2FSS_price()
        assert TT_C1ASS_price  == b.get_TT_C1ASS_price()
        assert TT_A2KSSS_price == b.get_TT_A2KSSS_price()

        assert subtotal   == e.get_subtotal()
        assert ordertotal == e.get_ordertotal()

        e.use_expired_discount_code()

        e.verify_expired_discount_code_error()

        assert TT_B2FSS_price  == b.get_TT_B2FSS_price()
        assert TT_C1ASS_price  == b.get_TT_C1ASS_price()
        assert TT_A2KSSS_price == b.get_TT_A2KSSS_price()

        assert e.subtotal()   == e.get_subtotal()
        assert e.ordertotal() == e.get_ordertotal()

        e.click_card()

        assert e.ordertotal() == e.get_pay_now_button_price()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        assert [TT_B2FSS, TT_C1ASS, TT_A2KSSS]                   == g.get_order_status_items()
        assert [TT_B2FSS_qty, TT_C1ASS_qty, TT_A2KSSS_qty]       == g.get_order_status_items_qty()
        assert [TT_B2FSS_price, TT_C1ASS_price, TT_A2KSSS_price] == g.get_order_status_items_price()

        assert [subtotal, ordertotal] == g.get_order_status_subtotal_and_order_total()

        print("\nTC004 " + g.get_orderid())

        # END
