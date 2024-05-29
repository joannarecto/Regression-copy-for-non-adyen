from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
from page_OBJECTS.orderstatus import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_EUR(baseclass):

    # @pytestrail.case('')
    def test_EUR(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayerAuth   (self.driver)
        g = OrderStatus (self.driver)

        a.select_eur()

        a.click_addtobasket1()

        eur_itemprice1 = a.get_eur_itemprice1()

        eur_ordertotal = eur_subtotal = eur_itemprice1

        a.click_cart()

        assert eur_itemprice1 == b.get_eur_itemprice1()
        assert eur_ordertotal == b.get_eur_ordertotal()

        b.click_gotocheckout()

        c.input_e_eur_emailaddress()

        c.click_continuetocheckout()

        d.input_eur_password()

        d.click_signin()

        assert eur_itemprice1 == e.get_eur_itemprice1()
        assert eur_subtotal   == e.get_eur_subtotal()
        assert eur_ordertotal == e.get_eur_ordertotal()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        assert eur_itemprice1 == g.get_eur_itemprice1()
        assert eur_ordertotal == g.get_eur_ordertotal()

        print("\nEUR " + g.get_orderid())

        # END
