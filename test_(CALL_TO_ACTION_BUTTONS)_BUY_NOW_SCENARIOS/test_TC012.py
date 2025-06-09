# USER JOURNEY: SHOPFRONT
# USER TYPE:    EXISTING USER
# SCENARIO:     ADD TO CART + BUY NOW & BACK TO BASKET

from page_OBJECTS.basket      import Basket
from page_OBJECTS.store       import Store
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
from page_OBJECTS.orderstatus import OrderStatus
from selenium.common.exceptions import NoSuchElementException

from utilities.baseclass import baseclass
from time import sleep

class Test_TC012(baseclass):

    def test_TC012(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = Login       (self.driver)
        d = ReviewOrder (self.driver)
        e = PayerAuth   (self.driver)
        f = OrderStatus (self.driver)

        a.go_to_the_login_page_from_the_store()

        c.login_existing_user_012()

        TT_B2FSS = a.get_TT_B2FSS()
        a.add_to_cart_TT_B2FSS()

        TT_C1ASS = a.get_TT_C1ASS()
        a.buy_now_TT_C1ASS()

        assert [TT_C1ASS] == d.get_review_order_items()

        d.click_chevron()

        assert [TT_C1ASS, TT_B2FSS] == b.get_basket_items()

        b.click_gotocheckout()
        sleep(10)

        assert [TT_C1ASS, TT_B2FSS] == d.get_review_order_items()

        d.pay_via_card()

        e.authenticate_payment()

        f.view_receipt()

        assert [TT_B2FSS, TT_C1ASS] == f.get_order_status_items()

        print("\nTC012 " + f.get_orderid())

        # END
