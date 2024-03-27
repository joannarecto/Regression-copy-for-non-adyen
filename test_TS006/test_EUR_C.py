from page_OBJECTS.paypal import PayPal
from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.orderstatus import OrderStatus

from utilities.baseclass import baseclass

class Test_EUR_C(baseclass):

    def test_EUR_C(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayPal      (self.driver)
        g = OrderStatus (self.driver)

        a.select_eur_c()

        a.click_addtobasket1()

        eur_c_itemprice1 = a.get_eur_c_itemprice1()

        eur_c_ordertotal = eur_c_subtotal = eur_c_itemprice1

        a.click_cart()

        assert eur_c_itemprice1 == b.get_eur_c_itemprice1()
        assert eur_c_ordertotal == b.get_eur_c_ordertotal()

        b.click_gotocheckout()

        c.input_e_eur_c_emailaddress()

        c.click_continuetocheckout()

        d.input_eur_c_password()

        d.click_signin()

        assert eur_c_itemprice1 == e.get_eur_c_itemprice1()
        assert eur_c_subtotal   == e.get_eur_c_subtotal()
        assert eur_c_ordertotal == e.get_eur_c_ordertotal()

        e.pay_via_paypal()

        f.login_and_pay()

        g.view_receipt()

        assert eur_c_itemprice1 == g.get_eur_c_itemprice1()
        assert eur_c_ordertotal == g.get_eur_c_ordertotal()

        print("\nEUR-C " + g.get_orderid())

        # END
