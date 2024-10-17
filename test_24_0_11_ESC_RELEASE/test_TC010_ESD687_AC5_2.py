# AC4.1 - Abandoned Regular Product Journey Followed by “Buy Now” for Regular Product

from time import sleep

from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
from page_OBJECTS.orderstatus import OrderStatus
from selenium.common import NoSuchElementException

from utilities.baseclass import baseclass

class Test_TC010(baseclass):

    def test_TC010(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayerAuth   (self.driver)
        g = OrderStatus (self.driver)

        a.get_access_FP1()

        c.input_e_test_010_emailaddress()

        c.click_continuetocheckout()

        d.input_test_010_password()

        d.click_signin()

        assert e.revieworder_items_set() == ["Free Product 1"]
        assert "1" == e.check_product_qty()

        e.click_chevron()

        a.get_access_FP2()

        assert e.revieworder_items_set() == ["Free Product 2"]
        assert "1" == e.check_product_qty()
        assert "FREE" == e.gratis_label_check()

        e.pay_via_gratis()

        g.view_receipt()

        print("\nTS010 " + g.get_orderid())

        # END
