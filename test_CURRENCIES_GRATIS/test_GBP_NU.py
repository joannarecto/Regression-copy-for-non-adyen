from page_OBJECTS.store          import Store
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.orderstatus    import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_GBP(baseclass):

    # @pytestrail.case('')
    def test_GBP(self):

        a = Store          (self.driver)
        b = PreLogin       (self.driver)
        c = BillingDetails (self.driver)
        d = ReviewOrder    (self.driver)
        e = OrderStatus    (self.driver)

        # a.select_gbp()

        gbp_FP1_price = a.get_gbp_FP1_price()
        a.get_access_FP1()

        gbp_ordertotal = gbp_subtotal = gbp_FP1_price

        b.input_n_gbp_emailaddress()

        b.click_continuetocheckout()

        assert gbp_subtotal == c.get_gbp_subtotal()

        c.input_gbp_billing_details_and_proceed()

        assert 'FREE'         == d.get_gbp_FP1_price()
        assert gbp_subtotal   == d.get_gbp_subtotal()
        assert gbp_ordertotal == d.get_gbp_ordertotal() == d.get_pay_now_button_price()

        d.pay_via_gratis()

        e.view_receipt()

        assert gbp_FP1_price  == e.get_gbp_FP1_price()
        assert gbp_ordertotal == e.get_gbp_ordertotal()

        print("\nGBP " + e.get_orderid())

        # END
