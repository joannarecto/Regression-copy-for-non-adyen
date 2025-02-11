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

        #Compass
        TT_B2FSS = a.get_TT_B2FSS()
        a.clear_product_searchfield()
        a.buy_now_TT_B2FSS()

        c.input_e_test_010_emailaddress()

        c.click_continuetocheckout()

        d.input_test_010_password()

        d.click_signin()

        assert [TT_B2FSS] == e.revieworder_items_set()

        e.click_chevron()

        b.click_chevron()

        #EDS
        a.select_eds()

        TT_C1ASS = a.get_TT_C1ASS()
        a.clear_product_searchfield()
        a.buy_now_TT_C1ASS()

        assert [TT_C1ASS] == e.revieworder_items_set()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        print("\nTS010 " + g.get_orderid())

        # END
