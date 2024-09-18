from page_OBJECTS.store       import Store
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.orderstatus import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_CAD(baseclass):

    # @pytestrail.case('')
    def test_CAD(self):

        a = Store       (self.driver)
        b = PreLogin    (self.driver)
        c = Login       (self.driver)
        d = ReviewOrder (self.driver)
        e = OrderStatus (self.driver)

        a.select_cad()

        cad_FP1_price = a.get_cad_FP1_price()
        a.get_access_FP1()

        cad_ordertotal = cad_subtotal = cad_FP1_price

        b.input_e_cad_emailaddress()

        b.click_continuetocheckout()

        c.input_cad_password()

        c.click_signin()

        assert 'FREE'         == d.get_cad_FP1_price()
        assert cad_subtotal   == d.get_cad_subtotal()
        assert cad_ordertotal == d.get_cad_ordertotal()

        d.pay_via_gratis()

        e.view_receipt()

        assert cad_FP1_price  == e.get_cad_FP1_price()
        assert cad_ordertotal == e.get_cad_ordertotal()

        print("\nCAD " + e.get_orderid())

        # END
