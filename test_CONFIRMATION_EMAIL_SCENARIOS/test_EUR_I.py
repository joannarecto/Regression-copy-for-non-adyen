from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
from page_OBJECTS.orderstatus import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_EUR_I(baseclass):

    # @pytestrail.case('')
    def test_EUR_I(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayerAuth   (self.driver)
        g = OrderStatus (self.driver)

        a.select_eur_i()

        a.add_to_cart_SF_L1DSB()

        a.click_cart()

        b.click_gotocheckout()

        c.input_confirmation_emailaddress()

        c.click_continuetocheckout()

        d.input_confirmation_password()

        d.click_signin()

        e.SF_L1DSB_qty_error_handling()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        print("\nEUR-I " + g.get_orderid())

        # END
