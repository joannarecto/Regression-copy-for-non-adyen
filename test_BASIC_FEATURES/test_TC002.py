#CART BUTTONS

from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.login          import Login
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus
from page_OBJECTS.data           import Data

from utilities.baseclass import baseclass
from time import sleep

class Test_TC002(baseclass):

    def test_TC002(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = Login          (self.driver)
        f = ReviewOrder    (self.driver)
        g = PayerAuth      (self.driver)
        h = OrderStatus    (self.driver)
        i = Data           (self.driver)

        a.add_to_cart_TT_B2FSS()

        a.click_cart()

        b.click_gotocheckout()

        # prelogin page

        c.click_cart()

        b.click_gotocheckout()

        c.input_n_test_002_emailaddress()

        c.click_continuetocheckout()

        # billing details page

        d.click_cart()

        b.click_gotocheckout()

        c.input_e_test_002_emailaddress()

        c.click_continuetocheckout()

        # login page

        e.click_cart()

        b.click_gotocheckout()

        c.input_e_test_002_emailaddress()

        c.click_continuetocheckout()

        e.input_test_002_password()

        e.click_signin()

        # review order page

        f.click_cart()

        b.click_gotocheckout()
        sleep(20)

        f.pay_via_failed_challenge_card()

        g.authenticate_payment()

        # order status (failed) page

        h.click_cart()

        b.click_gotocheckout()
        sleep(20)

        f.pay_via_mastercard_challenge_card()

        g.authenticate_payment()

        h.view_receipt()

        print("\nTC002 " + h.get_orderid())

        # order status (successful) page

        h.click_cart()

        assert i.basket_page_title == self.driver.title

        # END
