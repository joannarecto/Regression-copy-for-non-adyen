from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
from page_OBJECTS.orderstatus import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_TC003(baseclass):

    # @pytestrail.case('')
    def test_TC003(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayerAuth   (self.driver)
        g = OrderStatus (self.driver)

        a.add_to_cart_TP1()
        TP1       = a.get_TP1()
        TP1_qty   = a.get_TP1_qty()
        TP1_price = a.get_TP1_price()

        ordertotal = subtotal = TP1_price

        a.click_cart()

        assert TP1_price == b.get_TP1_price()

        assert subtotal == b.get_subtotal()

        b.click_gotocheckout()

        c.input_e_test_003_emailaddress()

        c.click_continuetocheckout()

        d.input_test_003_password()

        d.click_signin()

        assert TP1_price == e.get_TP1_price()

        assert subtotal   == e.get_subtotal()
        assert ordertotal == e.get_ordertotal()

        e.use_specific_product_discount_code()

        assert TP1_price == e.get_TP1_price()

        assert subtotal   == e.get_subtotal()
        assert ordertotal == e.get_ordertotal()

        e.click_card()

        assert ordertotal == e.get_pay_now_button_price()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        assert [TP1]       == g.get_order_status_items()
        assert [TP1_qty]   == g.get_order_status_items_qty()
        assert [TP1_price] == g.get_order_status_items_price()

        assert [ordertotal] == g.get_order_status_subtotal_and_order_total()

        print("\nTC003 " + g.get_orderid())

        # END
