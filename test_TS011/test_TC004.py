#DCESC-329

from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus

from utilities.baseclass import baseclass
from time import sleep

class Test_TC004(baseclass):

    def test_TC004(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayerAuth      (self.driver)
        g = OrderStatus    (self.driver)

        a.click_addtobasket1()

        a.click_cart()

        b.click_gotocheckout()

        c.input_n_test_004_emailaddress()

        c.click_continuetocheckout()

        d.input_test_billing_details_and_proceed()

        e.go_back()

        assert 'Basket | Cambridge Orders' == self.driver.title

        b.click_gotocheckout()
        sleep(20)

        assert 'Review order | Cambridge Orders' == self.driver.title

        e.click_chevron()

        assert 'Basket | Cambridge Orders' == self.driver.title

        b.click_gotocheckout()
        sleep(20)

        assert 'Review order | Cambridge Orders' == self.driver.title

        e.pay_via_amex_challenge_card()

        f.authenticate_payment()

        g.view_receipt()

        print("\nTC004 " + g.get_orderid())

        # END
