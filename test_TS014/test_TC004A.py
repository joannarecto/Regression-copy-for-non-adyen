# login an existing account from the shopfront and proceed with an add to cart process

from page_OBJECTS.store       import Store
from page_OBJECTS.login       import Login
from page_OBJECTS.basket      import Basket
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
from page_OBJECTS.orderstatus import OrderStatus

from utilities.baseclass import baseclass
from time import sleep

class Test_TC004(baseclass):

    def test_TC004(self):

        a = Store       (self.driver)
        b = Login       (self.driver)
        c = Basket      (self.driver)
        d = ReviewOrder (self.driver)
        e = PayerAuth   (self.driver)
        f = OrderStatus (self.driver)

        a.go_to_the_login_page_from_the_store()

        b.login_existing_user_004()

        a.add_to_cart_TT_B2FSS()

        a.click_cart()

        c.click_gotocheckout()
        sleep(15)

        d.pay_via_amex_challenge_card()

        e.authenticate_payment()

        f.view_receipt()

        print("\nTC004 " + f.get_orderid())

        # END
