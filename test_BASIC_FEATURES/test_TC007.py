# DELETE, UNDO, & X BUTTONS

from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
from page_OBJECTS.orderstatus import OrderStatus

from selenium.common.exceptions import NoSuchElementException
from utilities.baseclass import baseclass
from time import sleep

class Test_TC007(baseclass):

    def test_TC007(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayerAuth   (self.driver)
        g = OrderStatus (self.driver)

        a.add_to_cart_TT_B2FSS()

        a.clear_product_searchfield()

        a.add_to_cart_TT_C1ASS()

        a.clear_product_searchfield()

        a.add_to_cart_TT_A2KSSS()

        a.click_cart()

        assert b.your_items_total() == b.get_cart_total() in b.get_your_items_total()
        assert b.subtotal()         == b.get_subtotal()

        # your items

        # delete one product and undo

        b.YI_delete_TT_C1ASS()

        try:
            assert b.verify_YI_TT_C1ASS_is_displayed() == False
        except NoSuchElementException:
            pass

        assert b.your_items_total() == b.get_cart_total() in b.get_your_items_total()
        assert b.subtotal()         == b.get_subtotal()

        b.undo_item1() # C1

        assert b.verify_YI_TT_C1ASS_is_displayed() == True

        assert b.your_items_total() == b.get_cart_total() in b.get_your_items_total()
        assert b.subtotal()         == b.get_subtotal()

        # delete multiple products and undo

        b.YI_delete_TT_A2KSSS()

        try:
            assert b.verify_YI_TT_A2KSSS_is_displayed() == False
        except NoSuchElementException:
            pass

        assert b.your_items_total() == b.get_cart_total() in b.get_your_items_total()
        assert b.subtotal()         == b.get_subtotal()

        b.YI_delete_TT_B2FSS()

        try:
            assert b.verify_YI_TT_B2FSS_is_displayed() == False
        except NoSuchElementException:
            pass

        assert b.your_items_total() == b.get_cart_total() in b.get_your_items_total()
        assert b.subtotal()         == b.get_subtotal()

        b.undo_item1() # A2

        assert b.verify_YI_TT_A2KSSS_is_displayed() == True

        assert b.your_items_total() == b.get_cart_total() in b.get_your_items_total()
        assert b.subtotal()         == b.get_subtotal()

        b.undo_item1() # B2

        assert b.verify_YI_TT_B2FSS_is_displayed() == True

        assert b.your_items_total() == b.get_cart_total() in b.get_your_items_total()
        assert b.subtotal()         == b.get_subtotal()

        # delete all products and undo

        b.YI_delete_TT_C1ASS()

        try:
            assert b.verify_YI_TT_C1ASS_is_displayed() == False
        except NoSuchElementException:
            pass

        assert b.your_items_total() == b.get_cart_total() in b.get_your_items_total()
        assert b.subtotal()         == b.get_subtotal()

        b.YI_delete_TT_A2KSSS()

        try:
            assert b.verify_YI_TT_A2KSSS_is_displayed() == False
        except NoSuchElementException:
            pass

        assert b.your_items_total() == b.get_cart_total() in b.get_your_items_total()
        assert b.subtotal()         == b.get_subtotal()

        b.YI_delete_TT_B2FSS()

        try:
            assert b.verify_YI_TT_B2FSS_is_displayed() == False
        except NoSuchElementException:
            pass

        try:
            assert b.verify_order_summary_is_displayed() == False
        except NoSuchElementException:
            pass

        assert b.verify_empty_basket_is_displayed() == True

        b.undo_item1() # A2

        assert b.verify_YI_TT_A2KSSS_is_displayed() == True

        assert b.your_items_total() == b.get_cart_total() in b.get_your_items_total()
        assert b.subtotal()         == b.get_subtotal()

        b.undo_item1() # C1

        assert b.verify_YI_TT_C1ASS_is_displayed() == True

        assert b.your_items_total() == b.get_cart_total() in b.get_your_items_total()
        assert b.subtotal()         == b.get_subtotal()

        b.undo_item1() # B2

        assert b.verify_YI_TT_B2FSS_is_displayed() == True

        assert b.your_items_total() == b.get_cart_total() in b.get_your_items_total()
        assert b.subtotal()         == b.get_subtotal()

        # save for later items

        # given there is an item under your items, delete an item leaving another item

        b.saveforlater_TT_A2KSSS()

        b.saveforlater_TT_C1ASS()

        b.SFLI_delete_TT_A2KSSS()

        try:
            assert b.verify_SFLI_TT_A2KSSS_is_displayed() == False
        except NoSuchElementException:
            pass

        assert b.verify_SFLI_TT_C1ASS_is_displayed() == True

        assert b.save_for_later_items() in b.get_save_for_later_items()
        assert b.your_items_total()     == b.get_cart_total() in b.get_your_items_total()

        # given there is an item under your items, delete the remaining item

        b.SFLI_delete_TT_C1ASS()

        try:
            assert b.verify_SFLI_TT_C1ASS_is_displayed() and b.verify_save_for_later_items_is_displayed() == False
        except NoSuchElementException:
            pass

        assert b.your_items_total() == b.get_cart_total() in b.get_your_items_total()

        # given there is no item under your items, delete the remaining item

        b.saveforlater_TT_B2FSS()

        try:
            assert b.verify_order_summary_is_displayed() == False
        except NoSuchElementException:
            pass

        assert b.verify_empty_basket_is_displayed() == True

        b.SFLI_delete_TT_B2FSS()

        try:
            assert b.verify_SFLI_TT_B2FSS_is_displayed() and b.verify_save_for_later_items_is_displayed() == False
        except NoSuchElementException:
            pass

        assert b.verify_empty_basket_is_displayed() == True

        b.click_continueshopping()

        a.add_to_cart_TT_B2FSS()

        a.add_to_cart_TT_C1ASS()

        a.add_to_cart_TT_A2KSSS()

        a.click_cart()

        # single item

        b.YI_delete_TT_C1ASS()

        b.x_item1()

        try:
            assert b.verify_item1_removed_is_displayed() == False
        except NoSuchElementException:
            pass

        assert b.your_items_total() == b.get_cart_total() in b.get_your_items_total()
        assert b.subtotal()         == b.get_subtotal()

        # multiple items

        b.YI_delete_TT_A2KSSS()

        b.YI_delete_TT_B2FSS()

        b.x_item1()

        b.x_item1()

        try:
            assert b.verify_item1_removed_is_displayed() and b.verify_item2_removed_is_displayed() == False
        except NoSuchElementException:
            pass

        try:
            assert b.verify_your_items_is_displayed()    == False
            assert b.verify_order_summary_is_displayed() == False
        except NoSuchElementException:
            pass

        assert b.verify_empty_basket_is_displayed() == True

        b.click_continueshopping()

        a.add_to_cart_TT_B2FSS()

        a.add_to_cart_TT_C1ASS()

        a.add_to_cart_TT_A2KSSS()

        a.click_cart()

        b.click_gotocheckout()

        c.input_e_test_007_emailaddress()

        c.click_continuetocheckout()

        d.input_test_007_password()

        d.click_signin()

        assert e.your_items_total() == e.get_cart_total() in e.get_your_items_total()
        assert e.order_total()      == e.get_ordertotal()

        # your items

        # delete one product and undo

        e.YI_delete_TT_C1ASS()

        try:
            assert e.verify_YI_TT_C1ASS_is_displayed() == False
        except NoSuchElementException:
            pass

        assert e.your_items_total() == e.get_cart_total() in e.get_your_items_total()
        assert e.order_total()      == e.get_ordertotal()

        e.undo_item1() # C1

        assert e.verify_YI_TT_C1ASS_is_displayed() == True

        assert e.your_items_total() == e.get_cart_total() in e.get_your_items_total()
        assert e.order_total()      == e.get_ordertotal()

        # delete multiple products and undo

        e.YI_delete_TT_A2KSSS()

        try:
            assert e.verify_YI_TT_A2KSSS_is_displayed() == False
        except NoSuchElementException:
            pass

        assert e.your_items_total() == e.get_cart_total() in e.get_your_items_total()
        assert e.order_total()      == e.get_ordertotal()

        e.YI_delete_TT_B2FSS()

        try:
            assert e.verify_YI_TT_B2FSS_is_displayed() == False
        except NoSuchElementException:
            pass

        assert e.your_items_total() == e.get_cart_total() in e.get_your_items_total()
        assert e.order_total()      == e.get_ordertotal()

        e.undo_item1() # A2

        assert e.verify_YI_TT_A2KSSS_is_displayed() == True

        assert e.your_items_total() == e.get_cart_total() in e.get_your_items_total()
        assert e.order_total()      == e.get_ordertotal()

        e.undo_item1() # B2

        assert e.verify_YI_TT_B2FSS_is_displayed() == True

        assert e.your_items_total() == e.get_cart_total() in e.get_your_items_total()
        assert e.order_total()      == e.get_ordertotal()

        # delete all products and undo

        e.YI_delete_TT_C1ASS()

        try:
            assert e.verify_YI_TT_C1ASS_is_displayed() == False
        except NoSuchElementException:
            pass

        assert e.your_items_total() == e.get_cart_total() in e.get_your_items_total()
        assert e.order_total()      == e.get_ordertotal()

        e.YI_delete_TT_A2KSSS()

        try:
            assert e.verify_YI_TT_A2KSSS_is_displayed() == False
        except NoSuchElementException:
            pass

        assert e.your_items_total() == e.get_cart_total() in e.get_your_items_total()
        assert e.order_total()      == e.get_ordertotal()

        e.YI_delete_TT_B2FSS()

        try:
            assert e.verify_YI_TT_B2FSS_is_displayed() == False
        except NoSuchElementException:
            pass

        try:
            assert e.verify_order_summary_is_displayed() == False
        except NoSuchElementException:
            pass

        assert e.verify_empty_basket_is_displayed() == True

        e.undo_item1() # A2

        assert e.verify_YI_TT_A2KSSS_is_displayed() == True

        assert e.your_items_total() == e.get_cart_total() in e.get_your_items_total()
        assert e.order_total()      == e.get_ordertotal()

        e.undo_item1() # C1

        assert e.verify_YI_TT_C1ASS_is_displayed() == True

        assert e.your_items_total() == e.get_cart_total() in e.get_your_items_total()
        assert e.order_total()      == e.get_ordertotal()

        e.undo_item1() # B2

        assert e.verify_YI_TT_B2FSS_is_displayed() == True

        assert e.your_items_total() == e.get_cart_total() in e.get_your_items_total()
        assert e.order_total()      == e.get_ordertotal()

        # single item

        e.YI_delete_TT_C1ASS()

        e.x_item1()

        try:
            assert e.verify_item1_removed_is_displayed() == False
        except NoSuchElementException:
            pass

        assert e.your_items_total() == e.get_cart_total() in e.get_your_items_total()
        assert e.order_total()      == e.get_ordertotal()

        # multiple items

        e.YI_delete_TT_A2KSSS()

        e.YI_delete_TT_B2FSS()

        e.x_item1()

        e.x_item1()

        try:
            assert e.verify_item1_removed_is_displayed() and e.verify_item2_removed_is_displayed() == False
        except NoSuchElementException:
            pass

        try:
            assert e.verify_your_items_is_displayed()    == False
            assert e.verify_order_summary_is_displayed() == False
        except NoSuchElementException:
            pass

        assert e.verify_empty_basket_is_displayed() == True

        e.click_continueshopping()

        a.add_to_cart_TT_B2FSS()

        a.add_to_cart_TT_C1ASS()

        a.add_to_cart_TT_A2KSSS()

        a.click_cart()

        b.click_gotocheckout()
        sleep(20)

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        print("\nTC007 " + g.get_orderid())

        # END
