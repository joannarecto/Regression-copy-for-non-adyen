# create an add to basket + buy now with item deletion process through cambridge orders using an existing account

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

    # @pytestrail.case('')
    def test_TC006(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayerAuth   (self.driver)
        g = OrderStatus (self.driver)

        a.add_to_cart_TT_B2FSS()

        a.buy_now_TT_C1ASS()

        c.input_e_test_006_emailaddress()

        c.click_continuetocheckout()

        d.input_test_006_password()

        d.click_signin()

        # check if only the "Buy now item" is on the Review order page

        buynow_item = ['Test & Train C1 Advanced Self-Study']
        basket_item = ['Test & Train C1 Advanced Self-Study', 'Test & Train B2 First Self-Study']

        assert e.revieworder_items_set() == buynow_item

        e.click_chevron()

        # check if both "Add to basket-item" and "Buy now-item" are in the basket page

        assert b.basket_items_set() == basket_item

        b.YI_delete_TT_B2FSS()
        b.YI_delete_TT_C1ASS()

        b.click_continueshopping()

        try:
            assert a.cartoval_displayed() == False
        except NoSuchElementException:
            pass

        a.add_to_cart_TT_B2FSS()

        a.buy_now_TT_C1ASS()

        assert e.revieworder_items_set() == buynow_item

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        print("\nTest_TC006 " + g.get_orderid())

        # END
