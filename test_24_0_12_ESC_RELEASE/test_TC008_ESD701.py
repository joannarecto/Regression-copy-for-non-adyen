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

        #Compass
        FP1 = a.get_FP1()
        a.get_access_FP1()

        c.input_e_test_008_emailaddress()

        c.click_continuetocheckout()

        d.input_test_008_password()

        d.click_signin()

        assert [FP1] == e.revieworder_items_set()

        e.click_chevron()


        #EDS
        a.select_eds()

        MB2RPR = a.get_MB2RPR()
        a.get_access_MB2RPR()

        assert [MB2RPR] == e.revieworder_items_set()

        e.pay_via_gratis()

        g.view_receipt()

        print("\nTS008 " + g.get_orderid())

        # END
