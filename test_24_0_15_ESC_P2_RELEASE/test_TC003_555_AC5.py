from time import sleep

from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
from page_OBJECTS.orderstatus import OrderStatus
from selenium.common import NoSuchElementException

from utilities.baseclass import baseclass

class Test_TC003(baseclass):

    def test_TC003(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayerAuth   (self.driver)
        g = OrderStatus (self.driver)

        # AC5 - Existing Customers with Physical Products

        a.add_to_cart_PP1()

        a.click_cart()

        b.click_gotocheckout()

        c.input_e_test_003_emailaddress()

        c.click_continuetocheckout()

        d.input_test_003_password()

        d.click_signin()

        e.verify_physicalproduct_address()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        print("\nTEST003 " + g.get_orderid())

        # END
