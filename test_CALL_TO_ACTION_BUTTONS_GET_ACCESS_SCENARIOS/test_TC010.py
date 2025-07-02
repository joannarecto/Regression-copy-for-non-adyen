# USER JOURNEY: CAMBRIDGE ORDERS
# USER TYPE:    EXISTING USER
# SCENARIO:     ADD TO CART + GET ACCESS & BACK TO BASKET

from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
from page_OBJECTS.orderstatus import OrderStatus

from selenium.common.exceptions import NoSuchElementException
# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass
from time import sleep

class Test_TC010(baseclass):

    # @pytestrail.case('')
    def test_TC010(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayerAuth   (self.driver)
        g = OrderStatus (self.driver)

        a.add_to_cart_TT_B2FSS()
        TT_B2FSS     = a.get_TT_B2FSS()
        TT_B2FSS_qty = a.get_TT_B2FSS_qty()

        a.clear_product_searchfield()

        FP1 = a.get_access_FP1()

        c.input_e_test_010_emailaddress()

        c.click_continuetocheckout()

        d.input_test_010_password()

        d.click_signin()

        assert [FP1] == e.get_review_order_items()

        e.click_chevron()

        assert TT_B2FSS_qty == a.get_cartcount()

        a.click_cart()

        assert [TT_B2FSS] == b.get_basket_items()

        b.click_gotocheckout()
        sleep(10)

        assert [TT_B2FSS] == e.get_review_order_items()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        assert [TT_B2FSS] == g.get_order_status_items()

        print("\nTC010 " + g.get_orderid())

        # END
