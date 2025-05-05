#DCESC-342 & DCESC-576

from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus

from utilities.baseclass import baseclass
from time import sleep

class Test_TC003(baseclass):

    def test_TC003(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayerAuth      (self.driver)
        g = OrderStatus    (self.driver)

        a.add_to_cart_TT_B2FSS()

        a.clear_product_searchfield()

        a.add_to_cart_TT_C1ASS()

        a.click_cart()

        b.click_gotocheckout()

        c.input_n_test_003_emailaddress()

        c.click_continuetocheckout()

        d.input_test_billing_details_and_proceed()

        e.delete_item1()

        e.go_back()

        ss_path = ('C:\\Users\\jgabriel\\PycharmProjects\\Checkout_Regression\\saved_screenshots'
                   '\\ts011_tc003_verify_if_the_only_item_in_the_basket_is_b2_first_1.png')
        self.driver.save_screenshot(ss_path)

        b.click_gotocheckout()
        sleep(20)

        ss_path = ('C:\\Users\\jgabriel\\PycharmProjects\\Checkout_Regression\\saved_screenshots'
                   '\\ts011_tc003_verify_if_the_only_item_in_the_basket_is_b2_first_2.png')
        self.driver.save_screenshot(ss_path)

        e.pay_via_visa_challenge_card()

        f.authenticate_payment()

        g.view_receipt()

        print("\nTC003 " + g.get_orderid())

        # END
