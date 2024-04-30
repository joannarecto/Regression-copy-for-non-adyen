#DCESC-583

from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus

from utilities.baseclass import baseclass
from time import sleep

class Test_TC007(baseclass):

    def test_TC007(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayerAuth      (self.driver)
        g = OrderStatus    (self.driver)

        a.click_addtobasket1()

        a.click_addtobasket2()

        a.click_addtobasket3()

        a.click_cart()

        # items = b.get_items()

        # for item1, item2, item3 in b.get_items():
        #     print(item1)

        # b.click_gotocheckout()
        #
        # c.input_n_test_006_emailaddress()
        #
        # c.click_continuetocheckout()
        #
        # d.input_test_billing_details_and_proceed()

        # items = b.get_items()
        #
        # for item in items:
        #     print(item.text)
        #
        # for item in items:
        #     item1 = item.text
        #     item2 = item.text
        #     print(item1, item2)
        #
        # b.delete_item1()

        # items = b.get_items()

        # for item in items:
        #     print(item.text)

        # for item in items:
        #     assert 'Test & Train Self-Study B2 First' == item.text

        # b.click_gotocheckout()
        # sleep(20)
