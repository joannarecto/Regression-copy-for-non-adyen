#create a new account from the shopfront and proceed with the buy now process

from page_OBJECTS.store          import Store
from page_OBJECTS.login          import Login
from page_OBJECTS.mailsac        import Mailsac
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus

from utilities.baseclass import baseclass

class Test_TC003(baseclass):

    def test_TC003(self):

        a = Store          (self.driver)
        b = Login          (self.driver)
        c = Mailsac        (self.driver)
        d = ReviewOrder    (self.driver)
        e = PayerAuth      (self.driver)
        f = OrderStatus    (self.driver)

        a.go_to_the_login_page_from_the_store()

        b.create_a_new_account()

        c.get_verification_code_and_verify_email()

        a.click_buynow1()

        d.pay_via_mastercard_challenge_card()

        e.authenticate_payment()

        f.view_receipt()

        print("\nTC003 " + f.get_orderid())

        # END
