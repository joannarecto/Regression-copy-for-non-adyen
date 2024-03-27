from page_OBJECTS.paypal import PayPal
from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.orderstatus import OrderStatus

from utilities.baseclass import baseclass

class Test_GBP(baseclass):

    def test_GBP(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayPal      (self.driver)
        g = OrderStatus (self.driver)

        a.select_gbp()

        a.click_addtobasket1()

        gbp_itemprice1 = a.get_gbp_itemprice1()

        gbp_ordertotal = gbp_subtotal = gbp_itemprice1

        a.click_cart()

        assert gbp_itemprice1 == b.get_gbp_itemprice1()
        assert gbp_ordertotal == b.get_gbp_ordertotal()

        b.click_gotocheckout()

        c.input_e_gbp_emailaddress()

        c.click_continuetocheckout()

        d.input_gbp_password()

        d.click_signin()

        assert gbp_itemprice1 == e.get_gbp_itemprice1()
        assert gbp_subtotal   == e.get_gbp_subtotal()
        assert gbp_ordertotal == e.get_gbp_ordertotal()

        e.pay_via_paypal()

        f.login_and_pay()

        g.view_receipt()

        assert gbp_itemprice1 == g.get_gbp_itemprice1()
        assert gbp_ordertotal == g.get_gbp_ordertotal()

        print("\nGBP " + g.get_orderid())

        # END
