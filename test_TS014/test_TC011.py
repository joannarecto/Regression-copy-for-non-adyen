#create a new account from the shopfront and proceed with the add to basket + buy now process

from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.login          import Login
from page_OBJECTS.mailsac        import Mailsac
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus
from selenium.common.exceptions import NoSuchElementException

from utilities.baseclass import baseclass

class Test_TC011(baseclass):

    def test_TC011(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = Login          (self.driver)
        d = Mailsac        (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayerAuth      (self.driver)
        g = OrderStatus    (self.driver)

        a.go_to_the_login_page_from_the_store()

        c.create_a_new_account()

        d.get_verification_code_and_verify_email()

        a.click_addtobasket1()

        a.click_buynow2()

        # check if only the "Buy now item" is on the Review order page

        # QA
        buynow_item = ['Test & Train C1 Advanced Self-Study']
        basket_item = ['Test & Train C1 Advanced Self-Study', 'Test & Train Self-Study B2 First']

        # STG
        # buynow_item = ['Test & Train A2 Key for Schools Self-Study']
        # basket_item = ['Test & Train A2 Key for Schools Self-Study', 'Test & Train Self-Study B2 First']

        assert e.revieworder_items_set() == buynow_item

        e.click_chevron()

        # check if both "Add to basket-item" and "Buy now-item" are in the basket page

        assert b.basket_items_set() == basket_item

        b.click_gotocheckout()

        assert e.revieworder_items_set() == basket_item

        e.pay_via_mastercard_challenge_card()

        f.authenticate_payment()

        g.view_receipt()

        print("\nTC011 " + g.get_orderid())

        # END

