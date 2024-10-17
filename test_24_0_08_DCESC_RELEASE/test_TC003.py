#DCESC-523

from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus
from page_OBJECTS.createaccount    import CreateAccount

from time import sleep


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


        a.add_to_cart_TT_B2FSS()

        a.click_cart()

        b.click_gotocheckout()

        c.input_n_test_004_emailaddress()

        c.click_continuetocheckout()

        sleep(10)
        assert not "Save billing address" in d.page_src()
        print(d.page_src(),"\n======================================================================================================")

        d.input_test_billing_details_and_proceed()

        e.click_edit_address()

        sleep(10)
        assert not "Save billing address" in e.page_src()
        print(e.page_src(),"\n======================================================================================================")

        e.click_cancel_btn()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        print("\nDCESC-523 " + g.get_orderid())

        g.click_registerbutton()

        sleep(10)
        assert not "Save billing address" in h.page_src()
        print(h.page_src())

        # END
