from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.login       import Login
from page_OBJECTS.paypal      import PayPal
from page_OBJECTS.orderstatus import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_USD(baseclass):

    # @pytestrail.case('')
    def test_USD(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayPal      (self.driver)
        g = OrderStatus (self.driver)

        a.select_usd()

        a.click_addtobasket1()

        usd_itemprice1 = a.get_usd_itemprice1()

        usd_ordertotal = usd_subtotal = usd_itemprice1

        a.click_cart()

        assert usd_itemprice1 == b.get_usd_itemprice1()
        assert usd_ordertotal == b.get_usd_ordertotal()

        b.click_gotocheckout()

        c.input_e_usd_emailaddress()

        c.click_continuetocheckout()

        d.input_usd_password()

        d.click_signin()

        assert usd_itemprice1 == e.get_usd_itemprice1()
        assert usd_subtotal   == e.get_usd_subtotal()
        assert usd_ordertotal == e.get_usd_ordertotal()

        e.pay_via_paypal()

        f.login_and_pay()

        g.view_receipt()

        assert usd_itemprice1 == g.get_usd_itemprice1()
        assert usd_ordertotal == g.get_usd_ordertotal()

        print("\nUSD " + g.get_orderid())

        # END
