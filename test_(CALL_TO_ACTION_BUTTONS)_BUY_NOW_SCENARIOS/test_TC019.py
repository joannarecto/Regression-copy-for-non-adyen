# USER JOURNEY: SHOPFRONT
# USER TYPE:    NEW USER
# SCENARIO:     ADD TO CART + BUY NOW & DELETE

from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.login          import Login
from page_OBJECTS.mailsac        import Mailsac
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus

from selenium.common.exceptions import NoSuchElementException
# from pytest_testrail.plugin import pytestrail
from utilities.baseclass import baseclass
from time import sleep

class Test_TC007(baseclass):

    def test_TC007(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = Login          (self.driver)
        d = Mailsac        (self.driver)
        e = BillingDetails (self.driver)
        f = ReviewOrder    (self.driver)
        g = PayerAuth      (self.driver)
        h = OrderStatus    (self.driver)

        a.go_to_the_login_page_from_the_store()

        c.create_a_new_account()

        d.get_verification_code_and_verify_email()

        TT_B2FSS = a.get_TT_B2FSS()
        a.add_to_cart_TT_B2FSS()

        TT_C1ASS = a.get_TT_C1ASS()
        a.buy_now_TT_C1ASS()

        e.input_required_test_billing_details_and_proceed()

        assert [TT_C1ASS] == f.get_review_order_items()

        assert f.back_to_shopping_is_enabled() == True

        f.YI_delete_TT_C1ASS()

        try:
            assert f.verify_YI_TT_C1ASS_is_displayed() == False
        except NoSuchElementException:
            pass

        assert f.continue_shopping_is_enabled() == True

        f.click_chevron()

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

        a.buy_now_TT_B2FSS()

        assert [TT_B2FSS] == f.get_review_order_items()

        f.pay_via_card()

        g.authenticate_payment()

        h.view_receipt()

        assert [TT_B2FSS] == h.get_order_status_items()

        print("\nTC005 " + h.get_orderid())

        # END
