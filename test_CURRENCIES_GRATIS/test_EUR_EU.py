from page_OBJECTS.store       import Store
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.orderstatus import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_EUR(baseclass):

    # @pytestrail.case('')
    def test_EUR(self):

        a = Store       (self.driver)
        b = PreLogin    (self.driver)
        c = Login       (self.driver)
        d = ReviewOrder (self.driver)
        e = OrderStatus (self.driver)

        a.select_eur()

        eur_FP1_price = a.get_eur_FP1_price()
        a.get_access_FP1()

        eur_ordertotal = eur_subtotal = eur_FP1_price

        b.input_e_eur_emailaddress()

        b.click_continuetocheckout()

        c.input_eur_password()

        c.click_signin()

        assert 'FREE'         == d.get_eur_PP1_price()
        assert eur_subtotal   == d.get_eur_subtotal()
        assert eur_ordertotal == d.get_eur_ordertotal() == d.get_pay_now_button_price()

        d.pay_via_gratis()

        e.view_receipt()

        assert eur_FP1_price  == e.get_eur_PP1_price()
        assert eur_ordertotal == e.get_eur_ordertotal()

        print("\nEUR " + e.get_orderid())

        # END
