# create a new account from the shopfront and proceed with the add to basket + buy now process

from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.login          import Login
from page_OBJECTS.mailsac        import Mailsac
from page_OBJECTS.billingdetails import BillingDetails
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
        e = BillingDetails (self.driver)
        f = ReviewOrder    (self.driver)
        g = PayerAuth      (self.driver)
        h = OrderStatus    (self.driver)

        a.go_to_the_login_page_from_the_store()

        c.create_a_new_account()

        d.get_verification_code_and_verify_email()

        a.add_to_cart_TT_B2FSS()

        a.buy_now_TT_C1ASS()

        e.input_required_test_billing_details_and_proceed()

        # check if only the "Buy now item" is on the Review order page

        buynow_item = ['Test & Train C1 Advanced Self-Study']
        basket_item = ['Test & Train C1 Advanced Self-Study', 'Test & Train B2 First Self-Study']

        assert f.revieworder_items_set() == buynow_item

        f.click_chevron()

        # check if both "Add to basket-item" and "Buy now-item" are in the basket page

        assert b.basket_items_set() == basket_item

        b.click_gotocheckout()

        assert f.revieworder_items_set() == basket_item

        f.pay_via_mastercard_challenge_card()

        g.authenticate_payment()

        h.view_receipt()

        print("\nTC011 " + h.get_orderid())

        # END
