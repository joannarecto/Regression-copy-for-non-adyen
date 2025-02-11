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

class Test_TC008(baseclass):

    # @pytestrail.case('')
    def test_TC008(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayerAuth(self.driver)
        g = OrderStatus    (self.driver)

        # Gratis

        a.get_access_FP1()

        c.input_n_test_008_emailaddress()

        c.click_continuetocheckout()

        d.input_test_billing_details_and_proceed()

        e.verify_digitalproduct_address()

        e.pay_via_gratis()

        g.view_receipt()

        print("\nTEST008 " + g.get_orderid())


        # END
