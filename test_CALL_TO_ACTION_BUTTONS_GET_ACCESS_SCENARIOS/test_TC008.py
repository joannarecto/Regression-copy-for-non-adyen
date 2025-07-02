# USER JOURNEY: SHOPFRONT
# USER TYPE:    EXISTING USER
# SCENARIO:     ADD TO CART + GET ACCESS & BACK TO SHOPPING

from page_OBJECTS.store       import Store
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.orderstatus import OrderStatus
from page_OBJECTS.basket      import Basket

from selenium.common.exceptions import NoSuchElementException
from utilities.baseclass        import baseclass

class Test_TC008(baseclass):

    def test_TC008(self):

        a = Store       (self.driver)
        b = Login       (self.driver)
        c = ReviewOrder (self.driver)
        d = OrderStatus (self.driver)
        e = Basket      (self.driver)

        a.go_to_the_login_page_from_the_store()

        b.login_existing_user_008()

        a.add_to_cart_TT_B2FSS()
        TT_B2FSS     = a.get_TT_B2FSS()
        TT_B2FSS_qty = a.get_TT_B2FSS_qty()

        a.clear_product_searchfield()

        FP1 = a.get_access_FP1()

        assert [FP1] == c.get_review_order_items()

        c.pay_via_gratis()

        d.view_receipt()

        assert [FP1] == d.get_order_status_items()

        print("\nTC008 " + d.get_orderid())

        d.click_backtoshopping()

        assert TT_B2FSS_qty == a.get_cartcount()

        a.click_cart()

        assert [TT_B2FSS] == e.get_basket_items()

        # END
