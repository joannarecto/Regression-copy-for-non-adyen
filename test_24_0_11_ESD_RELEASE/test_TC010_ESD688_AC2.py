

from time import sleep

from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus
from page_OBJECTS.createaccount    import CreateAccount
from selenium.common import NoSuchElementException

from utilities.baseclass import baseclass

class Test_TC005(baseclass):

    def test_TC005(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayerAuth      (self.driver)
        g = OrderStatus    (self.driver)
        h = CreateAccount  (self.driver)

        assert "Get Access" == a.check_text_FP1_btn()

        a.get_access_FP1()

        assert "Back to Basket" == c.page_title()
        assert "Tell us your email address" in c.page_src()

        c.input_n_test_010_emailaddress()

        c.click_continuetocheckout()

        assert "Address details" == d.page_title()

        d.input_test_billing_details_and_proceed()

        assert "Review order" == e.page_title()

        e.pay_via_gratis()

        g.view_receipt()

        print("\nTS006_AC3 " + g.get_orderid())

        # END
