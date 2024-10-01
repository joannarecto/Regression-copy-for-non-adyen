# AC3 - Abandoned Regular Product Journey Followed by Free Product

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

        a.click_cart()

        b.click_gotocheckout()

        c.input_e_test_006_emailaddress()

        c.click_continuetocheckout()

        d.input_test_006_password()

        d.click_signin()

        e.click_chevron()

        try:
            assert b.basketproducts_displayed() == True
        except NoSuchElementException:
            assert False, "NoSuchElementException occurred, test failed"

        assert not "Your basket is empty" in b.page_src()

        assert not "FREE" == b.gratis_label_check()

        b.click_backtoshopping()

        a.get_access_FP1()

        assert "FREE" == e.gratis_label_check()

        e.pay_via_gratis()

        g.view_receipt()

        print("\nTS006_AC3 " + g.get_orderid())

        # END