# USER JOURNEY: CAMBRIDGE ORDERS
# USER TYPE:    EXISTING USER
# SCENARIO:     ADD TO CART + GET ACCESS

from page_OBJECTS.store       import Store
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.orderstatus import OrderStatus
from page_OBJECTS.basket      import Basket

from selenium.common.exceptions import NoSuchElementException
from utilities.baseclass        import baseclass

class Test_TC010(baseclass):

    # @pytestrail.case('')
    def test_TC010(self):

        a = Store       (self.driver)
        b = PreLogin    (self.driver)
        c = Login       (self.driver)
        d = ReviewOrder (self.driver)
        e = OrderStatus (self.driver)
        f = Basket      (self.driver)

        a.add_to_cart_TT_B2FSS()

        TT_B2FSS_qty = a.get_TT_B2FSS_qty()

        a.get_access_FP1()

        b.input_e_test_010_emailaddress()

        b.click_continuetocheckout()

        c.input_test_006_password()

        c.click_signin()

        # check if only the "Buy now item" is on the Review order page

        buynow_item = ['Free Product 1']

        abandoned_item = ['Test & Train B2 First Self-Study']

        assert d.revieworder_items_set() == buynow_item

        d.pay_via_gratis()

        e.view_receipt()

        print("\nTC010 " + e.get_orderid())

        e.click_backtoshopping()

        assert TT_B2FSS_qty == a.get_cartcount()

        a.click_cart()

        assert f.basket_items_set() == abandoned_item

        # END
