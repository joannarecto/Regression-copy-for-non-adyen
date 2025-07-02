# USER JOURNEY: SHOPFRONT
# USER TYPE:    EXISTING USER
# SCENARIO:     ADD TO CART + GET ACCESS & BACK TO BASKET

from page_OBJECTS.basket      import Basket
from page_OBJECTS.store       import Store
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
from page_OBJECTS.orderstatus import OrderStatus

from selenium.common.exceptions import NoSuchElementException
from utilities.baseclass import baseclass
from time import sleep

class Test_TC016(baseclass):

    def test_TC016(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = Login       (self.driver)
        d = ReviewOrder (self.driver)
        e = OrderStatus (self.driver)

        a.go_to_the_login_page_from_the_store()

        c.login_existing_user_014()

        a.add_to_cart_TT_B2FSS()
        TT_B2FSS     = a.get_TT_B2FSS()
        TT_B2FSS_qty = a.get_TT_B2FSS_qty()

        a.clear_product_searchfield()

        FP1 = a.get_access_FP1()

        assert [FP1] == d.get_review_order_items()

        assert d.back_to_shopping_is_enabled() == True

        d.YI_delete_FP1()

        try:
            assert d.verify_YI_FP1_is_displayed() == False
        except NoSuchElementException:
            pass

        assert d.continue_shopping_is_enabled() == True

        d.click_chevron()

        assert TT_B2FSS_qty == a.get_cartcount()

        a.click_cart()

        assert [TT_B2FSS] == b.get_basket_items()

        assert b.back_to_shopping_is_enabled() == True

        b.YI_delete_TT_B2FSS()

        try:
            assert b.verify_YI_TT_B2FSS_is_displayed() == False
        except NoSuchElementException:
            pass

        assert b.continue_shopping_is_enabled() == True

        b.click_chevron()

        a.get_access_FP1()

        assert [FP1] == d.get_review_order_items()

        d.click_chevron()

        try:
            assert a.cart_oval_is_displayed() == False
        except NoSuchElementException:
            pass

        a.click_cart()

        assert b.empty_basket_is_displayed() == True

        b.click_chevron()

        a.get_access_FP1()

        assert [FP1] == d.get_review_order_items()

        d.pay_via_gratis()

        e.view_receipt()

        assert [FP1] == e.get_order_status_items()

        print("\nTC016 " + e.get_orderid())

        # END
