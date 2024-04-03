from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.paypal         import PayPal
from page_OBJECTS.orderstatus    import OrderStatus

from utilities.baseclass import baseclass

class Test_CAD(baseclass):

    def test_CAD(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayPal         (self.driver)
        g = OrderStatus    (self.driver)

        a.select_cad()

        a.click_addtobasket1()

        cad_itemprice1 = a.get_cad_itemprice1()

        cad_ordertotal = cad_subtotal = cad_itemprice1

        a.click_cart()

        assert cad_itemprice1 == b.get_cad_itemprice1()
        assert cad_ordertotal == b.get_cad_ordertotal()

        b.click_gotocheckout()

        c.input_n_cad_emailaddress()

        c.click_continuetocheckout()

        assert cad_subtotal == d.get_cad_subtotal()

        d.input_cad_billing_details_and_proceed()

        assert cad_itemprice1 == e.get_cad_itemprice1()
        assert cad_subtotal   == e.get_cad_subtotal()
        assert cad_ordertotal == e.get_cad_ordertotal()

        e.pay_via_paypal()

        f.login_and_pay()

        g.view_receipt()

        assert cad_itemprice1 == g.get_cad_itemprice1()
        assert cad_ordertotal == g.get_cad_ordertotal()

        print("\nCAD " + g.get_orderid())

        # END
