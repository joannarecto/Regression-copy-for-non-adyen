from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.paypal      import PayPal
from page_OBJECTS.orderstatus import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_ESP(baseclass):

    # @pytestrail.case('')
    def test_ESP(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayPal      (self.driver)
        g = OrderStatus (self.driver)

        a.add_to_cart_TT_B2FSS()

        a.click_cart()

        b.click_gotocheckout()

        c.input_e_esp_emailaddress()

        c.click_continuetocheckout()

        d.input_esp_password()

        d.click_signin()

        e.pay_via_paypal()

        f.login_and_pay()

        g.view_receipt()

        print("\nESP " + g.get_orderid())

        # END
