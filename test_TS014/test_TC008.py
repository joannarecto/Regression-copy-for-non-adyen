# login an existing account from the shopfront and proceed with the add to basket + buy now with item deletion process

from page_OBJECTS.basket      import Basket
from page_OBJECTS.store       import Store
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
from page_OBJECTS.orderstatus import OrderStatus
from selenium.common.exceptions import NoSuchElementException


from utilities.baseclass import baseclass

class Test_TC008(baseclass):

    def test_TC008(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = Login       (self.driver)
        d = ReviewOrder (self.driver)
        e = PayerAuth   (self.driver)
        f = OrderStatus (self.driver)

        a.go_to_the_login_page_from_the_store()

        c.login_existing_user_008()

        a.add_to_cart_TT_B2FSS()

        a.buy_now_TT_C1ASS()

        # check if only the "Buy now item" is on the Review order page

        buynow_item = ['Test & Train C1 Advanced Self-Study']
        basket_item = ['Test & Train C1 Advanced Self-Study', 'Test & Train B2 First Self-Study']

        assert d.revieworder_items_set() == buynow_item

        d.click_chevron()

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

        assert d.revieworder_items_set() == buynow_item

        d.pay_via_amex_challenge_card()

        e.authenticate_payment()

        f.view_receipt()

        print("\nTC008 " + f.get_orderid())

        # END
