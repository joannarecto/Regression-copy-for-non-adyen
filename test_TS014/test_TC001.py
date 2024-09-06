# create a buy now process through cambridge orders using a new account

from page_OBJECTS.store          import Store
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_TC001(baseclass):

    # @pytestrail.case('')
    def test_TC001(self):

        a = Store          (self.driver)
        b = PreLogin       (self.driver)
        c = BillingDetails (self.driver)
        d = ReviewOrder    (self.driver)
        e = PayerAuth      (self.driver)
        f = OrderStatus    (self.driver)

        a.buy_now_TT_B2FSS()

        b.input_n_test_001_emailaddress()

        b.click_continuetocheckout()

        c.input_test_billing_details_and_proceed()

        d.pay_via_card()

        e.authenticate_payment()

        f.view_receipt()

        print("\ntest_TC001 " + f.get_orderid())

        # END
