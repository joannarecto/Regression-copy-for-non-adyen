import pytest
from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
from page_OBJECTS.orderstatus import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_USD(baseclass):

    # @pytestrail.case('')
    @pytest.mark.skip
    def test_USD(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayerAuth   (self.driver)
        g = OrderStatus (self.driver)

        a.select_usd()

        a.add_to_cart_TT_B2FSS()

        usd_PS1_price = a.get_usd_PS1_price()

        usd_ordertotal = usd_subtotal = usd_PS1_price

        a.click_cart()

        assert usd_PS1_price == b.get_usd_PS1_price()
        assert usd_subtotal       == b.get_usd_subtotal()

        b.click_gotocheckout()

        c.input_e_usd_emailaddress()

        c.click_continuetocheckout()

        d.input_usd_password()

        d.click_signin()

        e.decrease_qty_to_one_handling()

        e.click_card()

        assert usd_PS1_price == e.get_usd_PS1_price()
        assert usd_subtotal       == e.get_usd_subtotal()
        assert usd_ordertotal     == e.get_usd_ordertotal()



        assert usd_ordertotal == e.get_pay_now_button_price()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        assert usd_PS1_price == g.get_usd_PS1_price()
        assert usd_ordertotal     == g.get_usd_ordertotal()

        print("\nUSD " + g.get_orderid())

        # END
