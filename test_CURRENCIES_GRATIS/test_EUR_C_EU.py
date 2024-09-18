from page_OBJECTS.store       import Store
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.orderstatus import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_EUR_C(baseclass):

    # @pytestrail.case('')
    def test_EUR_C(self):

        a = Store       (self.driver)
        b = PreLogin    (self.driver)
        c = Login       (self.driver)
        d = ReviewOrder (self.driver)
        e = OrderStatus (self.driver)

        a.select_eur_c()

        eur_c_MB2RPR_price = a.get_eur_c_MB2RPR_price()
        a.get_access_MB2RPR()

        eur_c_ordertotal = eur_c_subtotal = eur_c_MB2RPR_price

        b.input_e_eur_c_emailaddress()

        b.click_continuetocheckout()

        c.input_eur_c_password()

        c.click_signin()

        assert 'FREE'           == d.get_eur_c_MB2RPR_price()
        assert eur_c_subtotal   == d.get_eur_c_subtotal()
        assert eur_c_ordertotal == d.get_eur_c_ordertotal()

        d.pay_via_gratis()

        e.view_receipt()

        assert eur_c_MB2RPR_price == e.get_eur_c_MB2RPR_price()
        assert eur_c_ordertotal   == e.get_eur_c_ordertotal()

        print("\nEUR-C " + e.get_orderid())

        # END
