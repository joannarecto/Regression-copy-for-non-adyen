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

class Test_TC004(baseclass):

    def test_TC004(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayerAuth   (self.driver)
        g = OrderStatus (self.driver)

        a.get_access_FP1()

        c.input_e_test_004_emailaddress()

        c.click_continuetocheckout()

        d.input_test_004_password()

        d.click_signin()

        assert "24px" == e.pay_via_gratis_margin()
        print(e.pay_via_gratis_margin())

        e.pay_via_gratis()

        g.view_receipt()

        print("\nTS004 " + g.get_orderid())

        # END
