
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

class Test_TC011(baseclass):

    def test_TC011(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayerAuth   (self.driver)
        g = OrderStatus (self.driver)

        #Existing user

        #not signed in
        assert "Get Access" == a.check_text_FP1_btn()

        a.get_access_FP1()

        assert "Back to Basket" == c.page_title()
        assert "Tell us your email address" in c.page_src()

        c.input_e_test_011_emailaddress()

        c.click_continuetocheckout()

        assert "Back to Basket" == c.page_title()
        assert "Sign in" in c.page_src()

        d.input_test_011_password()

        d.click_signin()

        assert "Review order" == e.page_title()

        e.click_backtoshopping()

        # Signed in
        a.get_access_FP1()

        assert "Review order" == e.page_title()

        e.pay_via_gratis()

        g.view_receipt()

        print("\nTS011 " + g.get_orderid())

        # END
