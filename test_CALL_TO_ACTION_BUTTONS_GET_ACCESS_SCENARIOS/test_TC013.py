# USER JOURNEY: CAMBRIDGE ORDERS
# USER TYPE:    GUEST USER
# SCENARIO:     ADD TO CART + GET ACCESS & BACK TO BASKET

from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.orderstatus    import OrderStatus

from selenium.common.exceptions import NoSuchElementException
# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass
from time import sleep

class Test_TC013(baseclass):

    # @pytestrail.case('')
    def test_TC013(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = OrderStatus    (self.driver)

        TT_B2FSS     = a.get_TT_B2FSS()
        TT_B2FSS_qty = a.get_TT_B2FSS_qty()
        a.add_to_cart_TT_B2FSS()

        FP1 = a.get_FP1()
        a.get_access_FP1()

        c.input_n_test_013_emailaddress()

        c.click_continuetocheckout()

        assert d.chevron_is_enabled() == True

        assert d.back_to_shopping_is_enabled() == True

        d.input_test_billing_details_and_proceed()

        assert [FP1] == e.get_review_order_items()

        assert e.back_to_shopping_is_enabled() == True

        e.YI_delete_FP1()

        try:
            assert e.verify_YI_FP1_is_displayed() == False
        except NoSuchElementException:
            pass

        assert e.continue_shopping_is_enabled() == True

        e.click_chevron()

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

        c.input_n_test_013_emailaddress()

        c.click_continuetocheckout()

        d.input_test_billing_details_and_proceed()

        assert [FP1] == e.get_review_order_items()

        e.click_chevron()

        try:
            assert a.cart_oval_is_displayed() == False
        except NoSuchElementException:
            pass

        a.click_cart()

        assert b.empty_basket_is_displayed() == True

        b.click_chevron()

        a.get_access_FP1()

        c.input_n_test_013_emailaddress()

        c.click_continuetocheckout()

        d.input_test_billing_details_and_proceed()

        assert [FP1] == e.get_review_order_items()

        e.pay_via_gratis()

        f.view_receipt()

        assert [FP1] == f.get_order_status_items()

        print("\nTC013 " + f.get_orderid())

        # END
