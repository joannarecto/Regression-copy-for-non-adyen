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

class Test_TC002(baseclass):

    def test_TC002(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayerAuth   (self.driver)
        g = OrderStatus (self.driver)

        #1 English
        # a.select_english()
        a.get_access_FP1()
        c.input_e_test_002_emailaddress()
        c.click_continuetocheckout()
        d.input_test_002_password()
        d.click_signin()
        assert "FREE" == e.gratis_label_check()
        e.click_chevron()

        #2 Spanish
        a.select_spanish()
        a.get_access_FP1_spanish()
        assert "GRATIS" == e.gratis_label_check()
        e.click_chevron()

        #3 Italian
        a.select_italian()
        a.get_access_FP1_italian()
        assert "GRATUITO" == e.gratis_label_check()

        e.pay_via_gratis()

        g.view_receipt2()

        print("\nTS003 " + g.get_orderid2())

        # END
