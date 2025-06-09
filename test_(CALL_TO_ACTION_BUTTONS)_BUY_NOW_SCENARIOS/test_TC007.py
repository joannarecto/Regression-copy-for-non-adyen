# USER JOURNEY: SHOPFRONT
# USER TYPE:    NEW USER
# SCENARIO:     ADD TO CART + BUY NOW & BACK TO SHOPPING

from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.login          import Login
from page_OBJECTS.mailsac        import Mailsac
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus

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

        TT_B2FSS     = a.get_TT_B2FSS()
        TT_B2FSS_qty = a.get_TT_B2FSS_qty()
        a.add_to_cart_TT_B2FSS()

        TT_C1ASS = a.get_TT_C1ASS()
        a.buy_now_TT_C1ASS()

        e.input_required_test_billing_details_and_proceed()

        assert [TT_C1ASS] == f.get_review_order_items()

        f.pay_via_card()

        g.authenticate_payment()

        h.view_receipt()

        assert [TT_C1ASS] == h.get_order_status_items()

        print("\nTC007 " + h.get_orderid())

        h.click_backtoshopping()

        assert TT_B2FSS_qty == a.get_cartcount()

        a.click_cart()

        assert [TT_B2FSS] == b.get_basket_items()

        # END
