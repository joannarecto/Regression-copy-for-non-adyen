# USER JOURNEY: SHOPFRONT
# USER TYPE:    NEW USER
# SCENARIO:     ADD TO CART + GET ACCESS & BACK TO SHOPPING

from page_OBJECTS.store          import Store
from page_OBJECTS.login          import Login
from page_OBJECTS.mailsac        import Mailsac
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.orderstatus    import OrderStatus
from page_OBJECTS.basket         import Basket

from selenium.common.exceptions import NoSuchElementException
from utilities.baseclass        import baseclass

class Test_TC007(baseclass):

    def test_TC007(self):

        a = Store          (self.driver)
        b = Login          (self.driver)
        c = Mailsac        (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = OrderStatus    (self.driver)
        g = Basket         (self.driver)

        a.go_to_the_login_page_from_the_store()

        b.create_a_new_account()

        c.get_verification_code_and_verify_email()

        a.add_to_cart_TT_B2FSS()
        TT_B2FSS     = a.get_TT_B2FSS()
        TT_B2FSS_qty = a.get_TT_B2FSS_qty()

        a.clear_product_searchfield()

        FP1 = a.get_access_FP1()

        d.input_required_test_billing_details_and_proceed()

        assert [FP1] == e.get_review_order_items()

        e.pay_via_gratis()

        f.view_receipt()

        assert [FP1] == f.get_order_status_items()

        print("\nTC007 " + f.get_orderid())

        f.click_backtoshopping()

        assert TT_B2FSS_qty == a.get_cartcount()

        a.click_cart()

        assert [TT_B2FSS] == g.get_basket_items()

        # END
