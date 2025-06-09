# USER JOURNEY: SHOPFRONT
# USER TYPE:    NEW USER
# SCENARIO:     GET ACCESS

from page_OBJECTS.store          import Store
from page_OBJECTS.login          import Login
from page_OBJECTS.mailsac        import Mailsac
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.orderstatus    import OrderStatus

from utilities.baseclass import baseclass

class Test_TC003(baseclass):

    def test_TC003(self):

        a = Store          (self.driver)
        b = Login          (self.driver)
        c = Mailsac        (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = OrderStatus    (self.driver)

        a.go_to_the_login_page_from_the_store()

        b.create_a_new_account()

        c.get_verification_code_and_verify_email()

        a.get_access_FP1()

        d.input_required_test_billing_details_and_proceed()

        e.pay_via_gratis()

        f.view_receipt()

        print("\nTC003 " + f.get_orderid())

        # END
