#DCESC-580, DCESC-584[AC1]

from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.paypal      import PayPal
from page_OBJECTS.orderstatus    import OrderStatus

from utilities.baseclass import baseclass
from time import sleep

class Test_TC006(baseclass):

    def test_TC006(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayPal      (self.driver)
        g = OrderStatus    (self.driver)

        a.add_to_cart_TP1()

        a.click_cart()

        b.click_gotocheckout()

        c.input_n_test_006_emailaddress()

        c.click_continuetocheckout()

        d.input_test_billing_details_and_proceed()

        # update qty in review order page

        e.increase_item1_qty()

        item1_qty = e.get_item1_qty()

        e.go_back()

        assert item1_qty == b.get_item1_qty()

        b.click_gotocheckout()
        sleep(20)

        assert item1_qty == e.get_item1_qty()

        e.go_back()

        # update qty in basket page

        b.increase_item1_qty()

        item1_qty = b.get_item1_qty()

        b.click_gotocheckout()
        sleep(20)

        assert item1_qty == e.get_item1_qty()

        e.go_back()

        assert item1_qty == b.get_item1_qty()

        b.click_gotocheckout()
        sleep(20)

        e.pay_via_paypal()

        f.login_and_pay()

        g.view_receipt()

        print("\nTC006 " + g.get_orderid())

        # END
