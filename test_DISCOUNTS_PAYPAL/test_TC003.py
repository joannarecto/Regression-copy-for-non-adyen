from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.paypal      import PayPal
from page_OBJECTS.orderstatus import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_TC003(baseclass):

    # @pytestrail.case('')
    def test_TC003(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayPal      (self.driver)
        g = OrderStatus (self.driver)

        a.add_to_cart_TT_B2FSS()
        TT_B2FSS_price  = a.get_TT_B2FSS_price()

        a.add_to_cart_TT_C1ASS()
        TT_C1ASS_price  = a.get_TT_C1ASS_price()

        a.add_to_cart_TT_A2KSSS()
        TT_A2KSSS_price = a.get_TT_A2KSSS_price()

        ordertotal = subtotal = a.get_subtotal()

        a.click_cart()

        assert TT_B2FSS_price  == b.get_TT_B2FSS_price()
        assert TT_C1ASS_price  == b.get_TT_C1ASS_price()
        assert TT_A2KSSS_price == b.get_TT_A2KSSS_price()

        assert subtotal == b.get_subtotal()

        b.click_gotocheckout()

        c.input_e_test_003_emailaddress()

        c.click_continuetocheckout()

        d.input_test_003_password()

        d.click_signin()

        assert TT_B2FSS_price  == b.get_TT_B2FSS_price()
        assert TT_C1ASS_price  == b.get_TT_C1ASS_price()
        assert TT_A2KSSS_price == b.get_TT_A2KSSS_price()

        assert subtotal   == e.get_subtotal()
        assert ordertotal == e.get_ordertotal()

        e.use_invalid_discount_code()

        e.verify_invalid_discount_code_error()

        assert TT_B2FSS_price  == b.get_TT_B2FSS_price()
        assert TT_C1ASS_price  == b.get_TT_C1ASS_price()
        assert TT_A2KSSS_price == b.get_TT_A2KSSS_price()

        assert e.subtotal()   == e.get_subtotal()
        assert e.ordertotal() == e.get_ordertotal()

        e.pay_via_paypal()

        f.login_and_pay()

        g.view_receipt()

        print("\nTC003 " + g.get_orderid())

        # END
