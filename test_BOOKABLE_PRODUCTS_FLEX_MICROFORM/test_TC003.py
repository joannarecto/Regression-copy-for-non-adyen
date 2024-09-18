# = 0

from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
from page_OBJECTS.orderstatus import OrderStatus

from selenium.common.exceptions import NoSuchElementException
# from pytest_testrail.plugin import pytestrail
from utilities.baseclass import baseclass
from time import sleep

class Test_TC003(baseclass):

    # @pytestrail.case('')
    def test_TC003(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayerAuth   (self.driver)
        g = OrderStatus (self.driver)

        a.add_to_cart_BP1()

        a.click_cart()

        b.click_gotocheckout()

        c.input_e_test_001_emailaddress()

        c.click_continuetocheckout()

        d.input_test_001_password()

        d.click_signin()

