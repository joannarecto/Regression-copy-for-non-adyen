from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
from page_OBJECTS.orderstatus import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_NZD(baseclass):

    # @pytestrail.case('')
    def test_NZD(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayerAuth   (self.driver)
        g = OrderStatus (self.driver)

        a.select_nzd()

        a.add_to_cart_TT_B2FSS()

        a.click_cart()

        b.click_gotocheckout()

        c.input_confirmation_emailaddress2()

        c.click_continuetocheckout()

        d.input_confirmation_password2()

        d.click_signin()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        print("\nNZD " + g.get_orderid())

        # END
