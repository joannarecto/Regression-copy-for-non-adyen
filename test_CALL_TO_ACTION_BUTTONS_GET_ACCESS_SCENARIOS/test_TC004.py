# USER JOURNEY: SHOPFRONT
# USER TYPE:    EXISTING USER
# SCENARIO:     GET ACCESS
import time

from page_OBJECTS.store       import Store
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.orderstatus import OrderStatus

from utilities.baseclass import baseclass

class Test_TC004(baseclass):

    def test_TC004(self):

        a = Store       (self.driver)
        b = Login       (self.driver)
        c = ReviewOrder (self.driver)
        d = OrderStatus (self.driver)

        a.go_to_the_login_page_from_the_store()

        b.login_existing_user_004()

        a.get_access_FP1()

        time.sleep(10)

        c.pay_via_gratis()

        d.view_receipt()

        print("\nTC004 " + d.get_orderid())

        # END
