# USER JOURNEY: SHOPFRONT
# USER TYPE:    EXISTING USER
# SCENARIO:     ADD TO CART + GET ACCESS

from page_OBJECTS.store       import Store
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.orderstatus import OrderStatus
from page_OBJECTS.basket      import Basket

from selenium.common.exceptions import NoSuchElementException
from utilities.baseclass        import baseclass

class Test_TC012(baseclass):

    def test_TC012(self):

        a = Store       (self.driver)
        b = Login       (self.driver)
        c = ReviewOrder (self.driver)
        d = OrderStatus (self.driver)
        e = Basket      (self.driver)

        a.go_to_the_login_page_from_the_store()

        b.login_existing_user_012()

        a.add_to_cart_TT_B2FSS()

        TT_B2FSS_qty = a.get_TT_B2FSS_qty()

        a.get_access_FP1()

        # check if only the "Buy now item" is on the Review order page

        buynow_item = ['Free Product 1']

        abandoned_item = ['Test & Train B2 First Self-Study']

        assert c.revieworder_items_set() == buynow_item

        c.pay_via_gratis()

        d.view_receipt()

        print("\nTC012 " + d.get_orderid())

        d.click_backtoshopping()

        assert TT_B2FSS_qty == a.get_cartcount()

        a.click_cart()

        assert e.basket_items_set() == abandoned_item

        # END
