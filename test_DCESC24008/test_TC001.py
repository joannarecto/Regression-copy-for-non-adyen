#DCESC-607

from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus
from selenium.common.exceptions import NoSuchElementException

from utilities.baseclass import baseclass

class Test_TC001(baseclass):

    def test_TC001(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayerAuth      (self.driver)
        g = OrderStatus    (self.driver)

        a.click_buynow1()

        c.input_n_test_001_emailaddress()

        c.click_continuetocheckout()

        d.input_test_billing_details_and_proceed()

        e.pay_via_card()

        f.authenticate_payment()

        try:
            assert g.cartoval_displayed() == False
        except NoSuchElementException:
            pass

        g.view_receipt()

        print("\nDCESC-607 " + g.get_orderid())

        g.click_shopfrontbtn()

        try:
            assert a.cartoval_displayed() == False
        except NoSuchElementException:
            pass

        a.click_cart()

        try:
            assert b.basketproducts_displayed() == False
        except NoSuchElementException:
            pass

        assert b.empty_basket_label() == "Your basket is empty"


        # END
