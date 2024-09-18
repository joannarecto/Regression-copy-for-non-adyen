from page_OBJECTS.store          import Store
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.orderstatus    import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_USD(baseclass):

    # @pytestrail.case('')
    def test_USD(self):

        a = Store          (self.driver)
        b = PreLogin       (self.driver)
        c = BillingDetails (self.driver)
        d = ReviewOrder    (self.driver)
        e = OrderStatus    (self.driver)

        a.select_usd()

        usd_FP1_price = a.get_usd_FP1_price()
        a.get_access_FP1()

        usd_ordertotal = usd_subtotal = usd_FP1_price

        b.input_n_usd_emailaddress()

        b.click_continuetocheckout()

        assert usd_subtotal == c.get_usd_subtotal()

        c.input_usd_billing_details_and_proceed()

        assert 'FREE'         == d.get_usd_FP1_price()
        assert usd_subtotal   == d.get_usd_subtotal()
        assert usd_ordertotal == d.get_usd_ordertotal()

        d.pay_via_gratis()

        e.view_receipt()

        assert usd_FP1_price  == e.get_usd_FP1_price()
        assert usd_ordertotal == e.get_usd_ordertotal()

        print("\nUSD " + e.get_orderid())

        # END
