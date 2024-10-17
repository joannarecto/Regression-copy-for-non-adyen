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

class Test_TC003(baseclass):

    def test_TC003(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayerAuth   (self.driver)
        g = OrderStatus (self.driver)

        #4 French
        a.select_french()
        a.get_access_FP1_french()
        c.input_e_test_003_emailaddress()
        c.click_continuetocheckout()
        d.input_test_003_password()
        d.click_signin()
        assert "GRATUIT" == e.gratis_label_check()
        e.click_chevron()

        #5 German
        a.select_german()
        a.get_access_FP1_german()
        assert "KOSTENLOS" == e.gratis_label_check()
        e.click_chevron()

        #6 Portuguese
        a.select_portuguese()
        a.get_access_FP1_port()
        assert "GRÁTIS" == e.gratis_label_check()

        e.pay_via_gratis()

        g.view_receipt2()

        print("\nTS003 " + g.get_orderid3())

        # END
