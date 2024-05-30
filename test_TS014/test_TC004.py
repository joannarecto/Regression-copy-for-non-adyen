#login an existing account from the shopfront and proceed with the buy now process

from page_OBJECTS.store       import Store
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
from page_OBJECTS.orderstatus import OrderStatus

from utilities.baseclass import baseclass

class Test_TC004(baseclass):

    def test_TC004(self):

        a = Store          (self.driver)
        b = Login          (self.driver)
        c = ReviewOrder    (self.driver)
        d = PayerAuth      (self.driver)
        e = OrderStatus    (self.driver)

        a.go_to_the_login_page_from_the_store()

        b.login_existing_user_004()

        a.click_buynow1()

        c.pay_via_amex_challenge_card()

        d.authenticate_payment()

        e.view_receipt()

        print("\nTC004 " + e.get_orderid())

        # END
