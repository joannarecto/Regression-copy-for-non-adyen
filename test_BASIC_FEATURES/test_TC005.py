#PRODUCT IMAGE

from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
from page_OBJECTS.orderstatus import OrderStatus

from utilities.baseclass import baseclass

class Test_TC005(baseclass):

    def test_TC005(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayerAuth   (self.driver)
        g = OrderStatus (self.driver)

        a.add_to_cart_TT_B2FSS()

        a.add_to_cart_TT_C1ASS()

        a.click_cart()

        b.verify_TT_B2FSS_is_accessible()

        b.verify_TT_C1ASS_is_accessible()

        b.click_gotocheckout()

        c.input_e_test_005_emailaddress()

        c.click_continuetocheckout()

        d.input_test_005_password()

        d.click_signin()

        e.verify_TT_B2FSS_is_accessible()

        e.verify_TT_C1ASS_is_accessible()

        e.pay_via_mastercard_challenge_card()

        f.authenticate_payment()

        g.verify_TT_B2FSS_is_accessible()

        g.verify_TT_C1ASS_is_accessible()

        g.view_receipt()

        print("\nTC005 " + g.get_orderid())

        # END
