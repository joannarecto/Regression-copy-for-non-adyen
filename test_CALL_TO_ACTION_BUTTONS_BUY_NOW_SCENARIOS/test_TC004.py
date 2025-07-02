# USER JOURNEY: SHOPFRONT
# USER TYPE:    EXISTING USER
# SCENARIO:     BUY NOW

from page_OBJECTS.store       import Store
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
from page_OBJECTS.orderstatus import OrderStatus

from time import sleep
from utilities.baseclass import baseclass

class Test_TC004(baseclass):

    def test_TC004(self):

        a = Store       (self.driver)
        b = Login       (self.driver)
        c = ReviewOrder (self.driver)
        d = PayerAuth   (self.driver)
        e = OrderStatus (self.driver)

        a.go_to_the_login_page_from_the_store()

        b.login_existing_user_004()

        a.buy_now_TT_B2FSS()

        sleep(5)

        c.pay_via_card()

        d.authenticate_payment()

        e.view_receipt()

        print("\nTC004 " + e.get_orderid())

        # END
