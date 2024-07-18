#create an add to basket + buy now process through cambridge orders using a new account

from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus
from selenium.common.exceptions import NoSuchElementException


# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_TC009(baseclass):

    # @pytestrail.case('')
    def test_TC009(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayerAuth      (self.driver)
        g = OrderStatus    (self.driver)

        a.click_addtobasket1()

        a.click_buynow2()

        c.input_n_test_009_emailaddress()

        c.click_continuetocheckout()

        d.input_test_billing_details_and_proceed()

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

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        print("\ntest_TC009 " + g.get_orderid())

        # END
