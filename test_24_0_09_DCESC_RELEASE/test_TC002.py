#DCESC-615

from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
from page_OBJECTS.orderstatus import OrderStatus

from utilities.baseclass import baseclass

class Test_TC002(baseclass):

    def test_TC002(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayerAuth   (self.driver)
        g = OrderStatus (self.driver)

        a.add_to_cart_TT_B2FSS()

        a.click_cart()

        b.click_gotocheckout()

        c.input_e_test_002_emailaddress()

        c.click_continuetocheckout()

        d.input_test_002_password()

        d.click_signin()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        assert "Your order's confirmed" == g.order_text1()
        assert not "Your payment's approved" == g.order_text1()

        assert "Your receipt" == g.order_text2()
        assert not "Your purchase receipt" == g.order_text2()


        print("\nDCESC-615 " + g.get_orderid())

        # END
