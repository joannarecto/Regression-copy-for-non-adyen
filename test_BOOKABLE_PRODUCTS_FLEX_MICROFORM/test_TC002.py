# greater than

from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
from page_OBJECTS.orderstatus import OrderStatus

from selenium.common.exceptions import NoSuchElementException
# from pytest_testrail.plugin import pytestrail
from utilities.baseclass import baseclass
from time import sleep

class Test_TC002(baseclass):

    # @pytestrail.case('')
    def test_TC002(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayerAuth   (self.driver)
        g = OrderStatus (self.driver)

        a.get_BP1_searchfield()

        for x in range(5):
            a.increase_BP1()

        a.clear_product_searchfield()
        a.add_to_cart_BP1()

        a.click_cart()

        b.click_gotocheckout()

        c.input_e_test_002_emailaddress()

        c.click_continuetocheckout()

        d.input_test_001_password()

        d.click_signin()

        # subtract and plus scenario

        assert e.verify_BP1_partially_available_error() == True

        e.increase_BP1()

        e.verify_maximum_qty_limit_is_displayed()

        for y in range(3):
            e.decrease_BP1()
            if y == 2:
                break
            try:
                assert e.verify_BP1_partially_available_error() == False
            except NoSuchElementException:
                pass

        e.undo_item1()

        for y in range(3):
            e.increase_BP1()
            try:
                assert e.verify_BP1_partially_available_error() == False
            except NoSuchElementException:
                pass
            if y == 3:
                e.verify_maximum_qty_limit_is_displayed()

        e.delete_BP1()

        e.click_continueshopping()

        for x in range(4):
            a.increase_BP1()

        a.add_to_cart_BP1()

        a.click_cart()

        b.click_gotocheckout()
        sleep(20)

        # delete and undo scenario

        assert e.verify_BP1_partially_available_error() == True

        e.delete_BP1()

        e.undo_item1()

        try:
            assert e.verify_BP1_partially_available_error() == False
        except NoSuchElementException:
            pass

        e.increase_BP1()

        e.verify_maximum_qty_limit_is_displayed()

        e.delete_BP1()

        e.click_continueshopping()

        for x in range(4):
            a.increase_BP1()

        a.add_to_cart_BP1()

        a.click_cart()

        b.click_gotocheckout()
        sleep(20)

        # back to basket scenario

        assert e.verify_BP1_partially_available_error() == True

        BP1_qty = e.get_BP1_qty()

        e.click_chevron()

        assert BP1_qty == b.get_BP1_qty()

        b.click_gotocheckout()
        sleep(20)

        try:
            assert e.verify_BP1_partially_available_error() == False
        except NoSuchElementException:
            pass

        assert BP1_qty == e.get_BP1_qty()

        e.delete_BP1()

        e.click_continueshopping()

        for x in range(4):
            a.increase_BP1()

        a.add_to_cart_BP1()

        a.click_cart()

        b.click_gotocheckout()
        sleep(20)

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        print("\nTC002 " + g.get_orderid())

        # END
