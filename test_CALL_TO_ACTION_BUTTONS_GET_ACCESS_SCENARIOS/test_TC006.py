# USER JOURNEY: CAMBRIDGE ORDERS
# USER TYPE:    EXISTING USER
# SCENARIO:     ADD TO CART + GET ACCESS & BACK TO SHOPPING

from page_OBJECTS.store       import Store
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.orderstatus import OrderStatus
from page_OBJECTS.basket      import Basket

from selenium.common.exceptions import NoSuchElementException
from utilities.baseclass        import baseclass

class Test_TC006(baseclass):

    # @pytestrail.case('')
    def test_TC006(self):

        a = Store       (self.driver)
        b = PreLogin    (self.driver)
        c = Login       (self.driver)
        d = ReviewOrder (self.driver)
        e = OrderStatus (self.driver)
        f = Basket      (self.driver)

        a.add_to_cart_TT_B2FSS()
        TT_B2FSS     = a.get_TT_B2FSS()
        TT_B2FSS_qty = a.get_TT_B2FSS_qty()

        a.clear_product_searchfield()

        FP1 = a.get_access_FP1()
        # FP1 = a.get_FP1()

        b.input_e_test_006_emailaddress()

        b.click_continuetocheckout()

        c.input_test_006_password()

        c.click_signin()

        assert [FP1] == d.get_review_order_items()

        d.pay_via_gratis()

        e.view_receipt()

        print("\nTC006 " + e.get_orderid())

        assert [FP1] == e.get_order_status_items()

        e.click_backtoshopping()

        assert TT_B2FSS_qty == a.get_cartcount()

        a.click_cart()

        assert [TT_B2FSS] == f.get_basket_items()

        # END
