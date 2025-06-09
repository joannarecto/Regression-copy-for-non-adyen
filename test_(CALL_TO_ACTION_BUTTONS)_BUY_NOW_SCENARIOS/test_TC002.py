# USER JOURNEY: CAMBRIDGE ORDERS
# USER TYPE:    EXISTING USER
# SCENARIO:     BUY NOW

from page_OBJECTS.store       import Store
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
from page_OBJECTS.orderstatus import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_TC002(baseclass):

    # @pytestrail.case('')
    def test_TC002(self):

        a = Store       (self.driver)
        b = PreLogin    (self.driver)
        c = Login       (self.driver)
        d = ReviewOrder (self.driver)
        e = PayerAuth   (self.driver)
        f = OrderStatus (self.driver)

        a.buy_now_TT_B2FSS()

        b.input_e_test_002_emailaddress()

        b.click_continuetocheckout()

        c.input_test_002_password()

        c.click_signin()

        d.pay_via_card()

        e.authenticate_payment()

        f.view_receipt()

        print("\nTC002 " + f.get_orderid())

        # END
