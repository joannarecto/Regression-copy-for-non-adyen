# USER JOURNEY: CAMBRIDGE ORDERS
# USER TYPE:    EXISTING USER
# SCENARIO:     ADD TO CART + BUY NOW & DELETE

from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
from page_OBJECTS.orderstatus import OrderStatus
from selenium.common.exceptions import NoSuchElementException

from selenium.common.exceptions import NoSuchElementException
# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass
from time import sleep

class Test_TC014(baseclass):

    # @pytestrail.case('')
    def test_TC014(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayerAuth   (self.driver)
        g = OrderStatus (self.driver)

        a.go_to_page2()

        TT_B2FSS = a.get_TT_B2FSS()
        a.add_to_cart_TT_B2FSS()

        TT_C1ASS = a.get_TT_C1ASS()
        a.buy_now_TT_C1ASS()

        c.input_e_test_014_emailaddress()

        c.click_continuetocheckout()

        d.input_test_014_password()

        d.click_signin()

        assert [TT_C1ASS] == e.get_review_order_items()

        assert e.back_to_shopping_is_enabled() == True

        e.YI_delete_TT_C1ASS()

        try:
            assert e.verify_YI_TT_C1ASS_is_displayed() == False
        except NoSuchElementException:
            pass

        assert e.continue_shopping_is_enabled() == True

        e.click_chevron()

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

        assert [TT_B2FSS] == e.get_review_order_items()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        assert [TT_B2FSS] == g.get_order_status_items()

        print("\nTC014 " + g.get_orderid())

        # END
