#DCESC-534

from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus

from utilities.baseclass import baseclass

class Test_TC010(baseclass):

    def test_TC010(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayerAuth      (self.driver)
        g = OrderStatus    (self.driver)

        a.click_addtobasket1()

        a.click_addtobasket2()

        a.click_cart()

        b.saveforlater_item1()

        b.click_gotocheckout()

        c.input_n_test_010_emailaddress()

        c.click_continuetocheckout()

        d.input_test_billing_details_and_proceed()

        e.pay_via_amex_challenge_card()

        f.authenticate_payment()

        g.view_receipt()

        print("\nTC010 " + g.get_orderid())

        g.click_backtoshopping()

        a.click_addtobasket1()

        assert '1' == a.get_cartcount()

        a.click_addtobasket2()

        assert '2' == a.get_cartcount()

        a.click_cart()

        ss_path = ('C:\\Users\\jgabriel\\PycharmProjects\\Checkout_Regression\\saved_screenshots'
                   '\\ts011_tc010_verify_if_two_items_are_present_in_the_basket.png')
        self.driver.save_screenshot(ss_path)

        # END
