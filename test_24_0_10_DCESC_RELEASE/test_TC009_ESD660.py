# create a new account from the shopfront and proceed with an add to cart process

from page_OBJECTS.store          import Store
from page_OBJECTS.login          import Login
from page_OBJECTS.mailsac        import Mailsac
from page_OBJECTS.basket         import Basket
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus

from utilities.baseclass import baseclass

class Test_TC009(baseclass):

    def test_TC009(self):

        a = Store          (self.driver)
        b = Login          (self.driver)
        c = Mailsac        (self.driver)
        d = Basket         (self.driver)
        e = BillingDetails (self.driver)
        f = ReviewOrder    (self.driver)
        g = PayerAuth      (self.driver)
        h = OrderStatus    (self.driver)

        a.go_to_the_login_page_from_the_store()

        b.create_a_new_account()

        c.get_verification_code_and_verify_email()

        a.add_to_cart_TT_B2FSS()

        a.click_cart()

        d.click_gotocheckout()

        e.input_required_test_billing_details_and_proceed()

        f.pay_via_mastercard_challenge_card()

        g.authenticate_payment()

        h.view_receipt()

        print("\nTC009 " + h.get_orderid())

        # END
