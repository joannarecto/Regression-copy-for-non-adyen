from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.orderstatus import OrderStatus

from utilities.baseclass import baseclass

class Test_TC006(baseclass):

    def test_TC006(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = OrderStatus (self.driver)

        a.click_addtobasket1()

        a.click_cart()

        b.click_gotocheckout()

        c.input_e_test_006_emailaddress()

        c.click_continuetocheckout()

        d.input_test_006_password()

        d.click_signin()

        e.pay_via_visa_frictionless_card()

        f.view_receipt()

        print("\nTC006 " + f.get_orderid())

        # END
