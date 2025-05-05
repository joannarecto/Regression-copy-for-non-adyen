from page_OBJECTS.store       import Store
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.orderstatus import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_USD(baseclass):

    # @pytestrail.case('')
    def test_USD(self):

        a = Store       (self.driver)
        b = PreLogin    (self.driver)
        c = Login       (self.driver)
        d = ReviewOrder (self.driver)
        e = OrderStatus (self.driver)

        a.select_usd()

        usd_FP1_price = a.get_usd_FP1_price()
        a.get_access_FP1()

        usd_ordertotal = usd_subtotal = usd_FP1_price

        b.input_e_usd_emailaddress()

        b.click_continuetocheckout()

        c.input_usd_password()

        c.click_signin()

        assert 'FREE'         == d.get_usd_PP1_price()
        assert usd_subtotal   == d.get_usd_subtotal()
        assert usd_ordertotal == d.get_usd_ordertotal() == d.get_pay_now_button_price()

        d.pay_via_gratis()

        e.view_receipt()

        assert usd_FP1_price  == e.get_usd_PP1_price()
        assert usd_ordertotal == e.get_usd_ordertotal()

        print("\nUSD " + e.get_orderid())

        # END
