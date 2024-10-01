#DCESC-554 (AC1 & AC3)

from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus

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

        a.add_to_cart_TT_B2FSS()

        a.click_cart()

        b.click_gotocheckout()

        c.input_n_test_003_emailaddress()

        c.click_continuetocheckout()

        d.input_tur_billing_details_searchaddress_only_p1()

        country_name = "Türkiye"

        #AC1
        assert d.check_country_searchbox_value() == country_name

        assert d.check_tur_country_searchdropdown_text() == country_name

        #AC3
        assert d.check_tur_country_dropdown_code() == "tur" and "tr"

        d.input_tur_billing_details_searchaddress_only_p2()

        assert d.check_country_value() == country_name

        d.click_gotorevieworder()

        e.click_edit_address()

        assert e.check_country_value() == country_name

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        print("\nDCESC-554 " + g.get_orderid())

        # END
