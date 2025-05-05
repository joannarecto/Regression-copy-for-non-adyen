from page_OBJECTS.store       import Store
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.orderstatus import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_USD_E(baseclass):

    # @pytestrail.case('')
    def test_USD_E(self):

        a = Store       (self.driver)
        b = PreLogin    (self.driver)
        c = Login       (self.driver)
        d = ReviewOrder (self.driver)
        e = OrderStatus (self.driver)

        a.select_usd_e()

        usd_e_FP1_price = a.get_usd_e_FP1_price()
        a.get_access_FP1()

        usd_e_ordertotal = usd_e_subtotal = usd_e_FP1_price

        b.input_e_usd_e_emailaddress()

        b.click_continuetocheckout()

        c.input_usd_e_password()

        c.click_signin()

        assert 'FREE'           == d.get_usd_e_PP1_price()
        assert usd_e_subtotal   == d.get_usd_e_subtotal()
        assert usd_e_ordertotal == d.get_usd_e_ordertotal() == d.get_pay_now_button_price()

        d.pay_via_gratis()

        e.view_receipt()

        assert usd_e_FP1_price == e.get_usd_e_PP1_price()
        assert usd_e_ordertotal   == e.get_usd_e_ordertotal()

        print("\nUSD-E " + e.get_orderid())

        # END
