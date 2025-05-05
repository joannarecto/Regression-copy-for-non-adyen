# AC4.2 - Abandoned Free Product Journey Followed by “Buy Now” for Regular Product

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

class Test_TC008(baseclass):

    def test_TC008(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayerAuth   (self.driver)
        g = OrderStatus (self.driver)

        a.get_access_FP1()

        c.input_e_test_008_emailaddress()

        c.click_continuetocheckout()

        d.input_test_008_password()

        d.click_signin()

        e.click_chevron()

        a.buy_now_TT_C1ASS()

        sleep(10)

        assert not "FREE" == e.gratis_label_check()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        print("\nTS008 " + g.get_orderid())

        # END
