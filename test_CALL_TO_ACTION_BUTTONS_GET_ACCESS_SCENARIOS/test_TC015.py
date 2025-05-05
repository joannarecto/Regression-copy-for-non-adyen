# USER JOURNEY: SHOPFRONT
# USER TYPE:    NEW USER
# SCENARIO:     ADD TO CART + GET ACCESS & BACK TO BASKET

from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.login          import Login
from page_OBJECTS.mailsac        import Mailsac
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.orderstatus    import OrderStatus

from selenium.common.exceptions import NoSuchElementException
from utilities.baseclass import baseclass
from time import sleep

class Test_TC015(baseclass):

    def test_TC015(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = Login          (self.driver)
        d = Mailsac        (self.driver)
        e = BillingDetails (self.driver)
        f = ReviewOrder    (self.driver)
        g = OrderStatus    (self.driver)

        a.go_to_the_login_page_from_the_store()

        c.create_a_new_account()

        d.get_verification_code_and_verify_email()


        TT_B2FSS     = a.get_TT_B2FSS()
        TT_B2FSS_qty = a.get_TT_B2FSS_qty()
        a.add_to_cart_TT_B2FSS()

        FP1 = a.get_FP1()
        a.get_access_FP1()

        e.input_required_test_billing_details_and_proceed()

        assert [FP1] == f.get_review_order_items()

        assert f.back_to_shopping_is_enabled() == True

        f.YI_delete_FP1()

        try:
            assert f.verify_YI_FP1_is_displayed() == False
        except NoSuchElementException:
            pass

        assert f.continue_shopping_is_enabled() == True

        f.click_chevron()

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

        assert [FP1] == f.get_review_order_items()

        f.click_chevron()

        try:
            assert a.cart_oval_is_displayed() == False
        except NoSuchElementException:
            pass

        a.click_cart()

        assert b.empty_basket_is_displayed() == True

        b.click_chevron()

        a.get_access_FP1()

        assert [FP1] == f.get_review_order_items()

        f.pay_via_gratis()

        g.view_receipt()

        assert [FP1] == g.get_order_status_items()

        print("\nTC015 " + g.get_orderid())

        # END
