# SAVE FOR LATER & MOVE TO BASKET BUTTONS

from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
from page_OBJECTS.orderstatus import OrderStatus

from selenium.common.exceptions import NoSuchElementException
from utilities.baseclass import baseclass

class Test_TC006(baseclass):

    def test_TC006(self):

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

        b.saveforlater_TT_C1ASS()

        assert b.save_for_later_items() in b.get_save_for_later_items()

        try:
            assert b.verify_YI_TT_C1ASS_is_displayed() == False
        except NoSuchElementException:
            pass

        assert b.verify_SFLI_TT_C1ASS_is_displayed() == True

        assert b.your_items_total() == b.get_cart_total() in b.get_your_items_total()
        assert b.subtotal()         == b.get_subtotal()

        b.saveforlater_TT_A2KSSS()

        assert b.save_for_later_items() in b.get_save_for_later_items()

        try:
            assert b.verify_YI_TT_A2KSSS_is_displayed() == False
        except NoSuchElementException:
            pass

        assert b.verify_SFLI_TT_A2KSSS_is_displayed() == True

        assert b.your_items_total() == b.get_cart_total() in b.get_your_items_total()
        assert b.subtotal()         == b.get_subtotal()

        b.saveforlater_TT_B2FSS()

        assert b.save_for_later_items() in b.get_save_for_later_items()

        try:
            assert b.verify_YI_TT_B2FSS_is_displayed() == False
        except NoSuchElementException:
            pass

        assert b.verify_SFLI_TT_B2FSS_is_displayed() == True

        try:
            assert b.verify_order_summary_is_displayed() == False
        except NoSuchElementException:
            pass

        assert b.verify_empty_basket_is_displayed() == True

        b.movetobasket_TT_C1ASS()

        assert b.save_for_later_items() in b.get_save_for_later_items()

        try:
            assert b.verify_SFLI_TT_C1ASS_is_displayed() == False
        except NoSuchElementException:
            pass

        assert b.verify_YI_TT_C1ASS_is_displayed() == True

        assert b.your_items_total() == b.get_cart_total() in b.get_your_items_total()
        assert b.subtotal()         == b.get_subtotal()

        b.movetobasket_TT_A2KSSS()

        assert b.save_for_later_items() in b.get_save_for_later_items()

        try:
            assert b.verify_SFLI_TT_A2KSSS_is_displayed() == False
        except NoSuchElementException:
            pass

        assert b.verify_YI_TT_A2KSSS_is_displayed() == True

        assert b.your_items_total() == b.get_cart_total() in b.get_your_items_total()
        assert b.subtotal()         == b.get_subtotal()

        b.movetobasket_TT_B2FSS()

        try:
            assert b.verify_SFLI_TT_B2FSS_is_displayed() == False
        except NoSuchElementException:
            pass

        assert b.verify_YI_TT_B2FSS_is_displayed() == True

        assert b.your_items_total() == b.get_cart_total() in b.get_your_items_total()
        assert b.subtotal()         == b.get_subtotal()

        b.click_gotocheckout()

        c.input_e_test_006_emailaddress()

        c.click_continuetocheckout()

        d.input_test_006_password()

        d.click_signin()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        print("\nTC006 " + g.get_orderid())

        # END
