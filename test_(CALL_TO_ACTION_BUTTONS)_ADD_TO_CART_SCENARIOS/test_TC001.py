# USER JOURNEY: CAMBRIDGE ORDERS
# USER TYPE:    GUEST USER
# SCENARIO:     ADD TO CART

from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus
from selenium.common.exceptions import NoSuchElementException

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass
from time import sleep

class Test_TC001(baseclass):

    # @pytestrail.case('')
    def test_TC001(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayerAuth      (self.driver)
        g = OrderStatus    (self.driver)

        TT_B2FSS = a.get_TT_B2FSS()
        a.add_to_cart_TT_B2FSS()

        a.click_cart()

        assert [TT_B2FSS] == b.get_basket_items()

        b.click_gotocheckout()

        c.input_n_test_001_emailaddress()

        c.click_continuetocheckout()

        d.input_test_billing_details_and_proceed()

        assert [TT_B2FSS] == e.get_review_order_items()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        assert [TT_B2FSS] == g.get_order_status_items()

        print("\nTC001 " + g.get_orderid())

        # END
