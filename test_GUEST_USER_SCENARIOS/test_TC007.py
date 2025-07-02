#DCESC-583, DCESC-584[AC2]

from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.paypal      import PayPal
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
        f = PayPal      (self.driver)
        g = OrderStatus    (self.driver)

        a.add_to_cart_TT_B2FSS()

        a.clear_product_searchfield()

        a.add_to_cart_TT_C1ASS()

        a.clear_product_searchfield()

        a.add_to_cart_TT_A2KSSS()

        a.click_cart()

        b.click_gotocheckout()

        c.input_n_test_010_emailaddress()

        c.click_continuetocheckout()

        d.input_test_billing_details_and_proceed()

        e.go_back()

        b.delete_item1()

        ss_path = ('C:\\Users\\jgabriel\\PycharmProjects\\Checkout_Regression\\saved_screenshots'
                   '\\ts011_tc007_verify_if_a2(qa)_c1(stg)_is_removed_in_the_basket_page.png')
        self.driver.save_screenshot(ss_path)

        b.click_gotocheckout()
        sleep(20)

        ss_path = ('C:\\Users\\jgabriel\\PycharmProjects\\Checkout_Regression\\saved_screenshots'
                   '\\ts011_tc007_verify_if_a2(qa)_c1(stg)_is_removed_in_the_review_order_page_1.png')
        self.driver.save_screenshot(ss_path)

        e.go_back()

        b.saveforlater_item1()

        ss_path = ('C:\\Users\\jgabriel\\PycharmProjects\\Checkout_Regression\\saved_screenshots'
                   '\\ts011_tc007_verify_if_a2(qa)_c1(stg)_is_under_the_save_for_later_in_the_basket_page.png')
        self.driver.save_screenshot(ss_path)

        b.click_gotocheckout()
        sleep(20)

        ss_path = ('C:\\Users\\jgabriel\\PycharmProjects\\Checkout_Regression\\saved_screenshots'
                   '\\ts011_tc007_verify_if_a2(qa)_c1(stg)_is_removed_in_the_review_order_page_2.png')
        self.driver.save_screenshot(ss_path)

        e.pay_via_paypal()

        f.login_and_pay()

        g.view_receipt()

        print("\nTC007 " + g.get_orderid())

        # END
