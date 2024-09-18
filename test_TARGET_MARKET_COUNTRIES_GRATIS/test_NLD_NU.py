from page_OBJECTS.store          import Store
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.orderstatus    import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_NLD(baseclass):

    # @pytestrail.case('')
    def test_NLD(self):

        a = Store          (self.driver)
        b = PreLogin       (self.driver)
        c = BillingDetails (self.driver)
        d = ReviewOrder    (self.driver)
        e = OrderStatus    (self.driver)

        a.get_access_FP1()

        b.input_n_nld_emailaddress()

        b.click_continuetocheckout()

        c.input_nld_billing_details_and_proceed()

        d.pay_via_gratis()

        e.view_receipt()

        print("\nNLD " + e.get_orderid())

        # END
