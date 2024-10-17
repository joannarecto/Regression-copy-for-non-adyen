from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus
from selenium.common import NoSuchElementException

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_TC001(baseclass):

    # @pytestrail.case('')
    def test_TC001(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayerAuth(self.driver)
        g = OrderStatus    (self.driver)

        def toPurchase(e):
            a.buy_now_TT_B2FSS()

            c.input_n_test_001_emailaddress()

            c.click_continuetocheckout()

        toPurchase(e)

        d.click_chevron()

        b.YI_delete_TT_B2FSS()

        b.click_continueshopping()

        try:
            assert a.cartoval_displayed() == False
        except NoSuchElementException:
            pass

        a.click_cart()

        try:
            assert b.basketproducts_displayed() == False
        except NoSuchElementException:
            pass

        assert b.empty_basket_label() == "Your basket is empty"

        b.click_continueshopping()

        toPurchase(e)

        d.input_test_billing_details_and_proceed()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        print("\ntest_TC001_ESD693" + g.get_orderid())

        # END
