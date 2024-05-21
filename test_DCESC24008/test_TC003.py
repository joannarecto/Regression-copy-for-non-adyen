#DCESC-523

from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus
from page_OBJECTS.createaccount    import CreateAccount


from utilities.baseclass import baseclass

class Test_TC003(baseclass):

    def test_TC003(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayerAuth      (self.driver)
        g = OrderStatus    (self.driver)
        h = CreateAccount  (self.driver)


        a.click_addtobasket1()

        a.click_cart()

        b.click_gotocheckout()

        c.input_n_test_004_emailaddress()

        c.click_continuetocheckout()

        assert not "Save billing address" in d.page_src()

        d.input_test_billing_details_and_proceed()

        e.click_edit_address()

        assert not "Save billing address" in e.page_src()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        print("\nDCESC-523 " + g.get_orderid())

        g.click_registerbutton()

        assert not "Save billing address" in h.page_src()

        # END
