# USER JOURNEY: SHOPFRONT
# USER TYPE:    EXISTING USER
# SCENARIO:     ADD TO CART + BUY NOW & DELETE

from page_OBJECTS.basket      import Basket
from page_OBJECTS.store       import Store
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
from page_OBJECTS.orderstatus import OrderStatus
from selenium.common.exceptions import NoSuchElementException

from selenium.common.exceptions import NoSuchElementException
# from pytest_testrail.plugin import pytestrail
from utilities.baseclass import baseclass
from time import sleep

class Test_TC016(baseclass):

    def test_TC016(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = Login       (self.driver)
        d = ReviewOrder (self.driver)
        e = PayerAuth   (self.driver)
        f = OrderStatus (self.driver)

        a.go_to_the_login_page_from_the_store()

        c.login_existing_user_014()

        a.go_to_page2()

        TT_B2FSS = a.get_TT_B2FSS()
        a.add_to_cart_TT_B2FSS()

        TT_C1ASS = a.get_TT_C1ASS()
        a.buy_now_TT_C1ASS()

        assert [TT_C1ASS] == d.get_review_order_items()

        assert d.back_to_shopping_is_enabled() == True

        d.YI_delete_TT_C1ASS()

        try:
            assert d.verify_YI_TT_C1ASS_is_displayed() == False
        except NoSuchElementException:
            pass

        assert d.continue_shopping_is_enabled() == True

        d.click_chevron()

        assert [TT_B2FSS] == b.get_basket_items()

        assert b.back_to_shopping_is_enabled() == True

        b.YI_delete_TT_B2FSS()

        try:
            assert b.verify_YI_TT_B2FSS_is_displayed() == False
        except NoSuchElementException:
            pass

        assert b.continue_shopping_is_enabled() == True

        b.click_chevron()

        try:
            assert a.cart_oval_is_displayed() == False
        except NoSuchElementException:
            pass

        a.click_cart()

        assert b.empty_basket_is_displayed() == True

        b.click_chevron()

        a.go_to_page2()

        a.buy_now_TT_B2FSS()

        assert [TT_B2FSS] == d.get_review_order_items()

        d.pay_via_card()

        e.authenticate_payment()

        f.view_receipt()

        assert [TT_B2FSS] == f.get_order_status_items()

        print("\nTC016 " + f.get_orderid())

        # END
