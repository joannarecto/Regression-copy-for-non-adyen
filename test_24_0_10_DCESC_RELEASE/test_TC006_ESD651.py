from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus
from page_OBJECTS.createaccount  import CreateAccount
from page_OBJECTS.mailsac        import Mailsac

from selenium.common.exceptions import NoSuchElementException
from utilities.baseclass import baseclass

class Test_TC006(baseclass):


    # @pytestrail.case('')
    def test_TC006(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayerAuth      (self.driver)
        g = OrderStatus    (self.driver)
        h = CreateAccount  (self.driver)
        i = Mailsac        (self.driver)

        a.add_to_cart_TT_B2FSS()

        a.click_cart()

        b.click_gotocheckout()

        c.input_random_emailaddress2()

        c.click_continuetocheckout()

        d.input_test_billing_details_and_proceed()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        print("\ntest_TC005 " + g.get_orderid())

        g.click_registerbutton()

        h.create_a_new_account()

        i.get_verification_code_and_verify_email2()

        # a.add_to_cart_TT_B2FSS()

        # END
