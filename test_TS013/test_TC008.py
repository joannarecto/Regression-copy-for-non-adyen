# DECREASE & INCREASE BUTTONS

from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
from page_OBJECTS.orderstatus import OrderStatus

from utilities.baseclass import baseclass

class Test_TC008(baseclass):

    def test_TC008(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayerAuth   (self.driver)
        g = OrderStatus (self.driver)

        a.add_to_cart_TT_B2FSS()

        a.add_to_cart_TP1()

        a.click_cart()

        b.decrease_TT_B2FSS()

        assert b.your_items_total() == b.get_cart_total() in b.get_your_items_total()
        assert b.order_total()      == b.get_gbp_ordertotal()

        b.undo_item1()

        assert b.your_items_total() == b.get_cart_total() in b.get_your_items_total()
        assert b.order_total()      == b.get_gbp_ordertotal()

        b.decrease_TP1()

        assert b.your_items_total() == b.get_cart_total() in b.get_your_items_total()
        assert b.order_total()      == b.get_gbp_ordertotal()

        b.undo_item1()

        assert b.your_items_total() == b.get_cart_total() in b.get_your_items_total()
        assert b.order_total()      == b.get_gbp_ordertotal()

        b.increase_TT_B2FSS()

        b.verify_maximum_qty_limit_is_displayed()

        assert b.your_items_total() == b.get_cart_total() in b.get_your_items_total()
        assert b.order_total()      == b.get_gbp_ordertotal()

        b.verify_TP1_increments_by_1()

        b.increase_TP1()

        b.verify_maximum_qty_limit_is_displayed()

        b.verify_TP1_qty_remains_unchanged_when_deleted_and_undone()

        b.verify_TP1_qty_remains_unchanged_when_saved_for_later_and_moved_to_basket()

        b.verify_TP1_decrements_by_1()

        b.click_gotocheckout()

        c.input_e_test_008_emailaddress()

        c.click_continuetocheckout()

        d.input_test_008_password()

        d.click_signin()

        e.decrease_TT_B2FSS()

        assert e.your_items_total() == e.get_cart_total() in e.get_your_items_total()
        assert e.order_total()      == e.get_gbp_ordertotal()

        e.undo_item1()

        assert e.your_items_total() == e.get_cart_total() in e.get_your_items_total()
        assert e.order_total()      == e.get_gbp_ordertotal()

        e.decrease_TP1()

        assert e.your_items_total() == e.get_cart_total() in e.get_your_items_total()
        assert e.order_total()      == e.get_gbp_ordertotal()

        e.undo_item1()

        assert e.your_items_total() == e.get_cart_total() in e.get_your_items_total()
        assert e.order_total()      == e.get_gbp_ordertotal()

        e.increase_TT_B2FSS()

        e.verify_maximum_qty_limit_is_displayed()

        assert e.your_items_total() == e.get_cart_total() in e.get_your_items_total()
        assert e.order_total()      == e.get_gbp_ordertotal()

        e.verify_TP1_increments_by_1()

        e.increase_TP1()

        e.verify_maximum_qty_limit_is_displayed()

        e.verify_TP1_qty_remains_unchanged_when_deleted_and_undone()

        e.verify_TP1_decrements_by_1()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        print("\nTC008 " + g.get_orderid())

        # END
