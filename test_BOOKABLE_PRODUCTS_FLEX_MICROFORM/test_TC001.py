# less than

from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
from page_OBJECTS.orderstatus import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_TC001(baseclass):

    # @pytestrail.case('')
    def test_TC001(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayerAuth   (self.driver)
        g = OrderStatus (self.driver)

        for x in range(1):
            a.increase_BP1()

        a.add_to_cart_BP1()

        a.click_cart()

        b.click_gotocheckout()

        c.input_e_test_001_emailaddress()

        c.click_continuetocheckout()

        d.input_test_001_password()

        d.click_signin()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()
