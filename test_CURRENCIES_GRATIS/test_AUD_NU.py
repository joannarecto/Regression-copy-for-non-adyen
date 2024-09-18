from page_OBJECTS.store          import Store
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.orderstatus    import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_AUD(baseclass):

    # @pytestrail.case('')
    def test_AUD(self):

        a = Store          (self.driver)
        b = PreLogin       (self.driver)
        c = BillingDetails (self.driver)
        d = ReviewOrder    (self.driver)
        e = OrderStatus    (self.driver)

        a.select_aud()

        aud_FP1_price = a.get_aud_FP1_price()
        a.get_access_FP1()

        aud_ordertotal = aud_subtotal = aud_FP1_price

        b.input_n_aud_emailaddress()

        b.click_continuetocheckout()

        assert aud_subtotal == c.get_aud_subtotal()

        c.input_aud_billing_details_and_proceed()

        assert 'FREE'         == d.get_aud_FP1_price()
        assert aud_subtotal   == d.get_aud_subtotal()
        assert aud_ordertotal == d.get_aud_ordertotal()

        d.pay_via_gratis()

        e.view_receipt()

        assert aud_FP1_price  == e.get_aud_FP1_price()
        assert aud_ordertotal == e.get_aud_ordertotal()

        print("\nAUD " + e.get_orderid())

        # END
