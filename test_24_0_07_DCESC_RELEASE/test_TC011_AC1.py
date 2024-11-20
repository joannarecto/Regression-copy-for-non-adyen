#DCESC-582_AC1

from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus
from page_OBJECTS.createaccount    import CreateAccount


from utilities.baseclass import baseclass

class Test_TC011(baseclass):

    def test_TC011(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayerAuth      (self.driver)
        g = OrderStatus    (self.driver)
        h = CreateAccount  (self.driver)

        a.select_eds()

        a.add_to_cart_SF_L1DSB()

        a.click_cart()

        b.click_gotocheckout()

        c.input_n_test_011_emailaddress()

        c.click_continuetocheckout()

        d.input_n_tur_billing_details_and_proceed()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        print("\nDCESC-582_AC1 " + g.get_orderid())

        g.click_registerbutton()

        country_name = "Türkiye"

        assert h.check_tur_country_dropdown_text() == country_name

        assert h.check_country_text() == country_name

        # END
