from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
from page_OBJECTS.failorderstatus import FailOrderStatus

from utilities.baseclass import baseclass

class Test_TC007(baseclass):

    def test_TC007(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayerAuth   (self.driver)
        g = FailOrderStatus (self.driver)

        a.add_to_cart_TT_B2FSS()

        a.click_cart()

        b.click_gotocheckout()

        c.input_e_test_007_emailaddress()

        c.click_continuetocheckout()

        d.input_test_007_password()

        d.click_signin()

        e.pay_failed_securitycode_via_card()

        f.authenticate_payment()

        # AC1 - TC011 - ESD677

        assert "There was a problem completing your order." == g.fail_subheader_msg()
        assert not "We couldn't complete the card payment" == g.fail_subheader_msg()

        # AC1 -TC008 - ESD654 - Update message on 'Thank You' page

        assert "You have NOT been charged for this transaction." in g.fail_body_msg()
        assert not "Your card has NOT been charged for this transaction" in g.fail_body_msg()

        # AC2 -TC008 - ESD654 - Successful transaction

        # END
