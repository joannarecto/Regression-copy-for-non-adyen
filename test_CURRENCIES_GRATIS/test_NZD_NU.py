from page_OBJECTS.store          import Store
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.orderstatus    import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_NZD(baseclass):

    # @pytestrail.case('')
    def test_NZD(self):

        a = Store          (self.driver)
        b = PreLogin       (self.driver)
        c = BillingDetails (self.driver)
        d = ReviewOrder    (self.driver)
        e = OrderStatus    (self.driver)

        a.select_nzd()

        nzd_FP1_price = a.get_nzd_FP1_price()
        a.get_access_FP1()

        nzd_ordertotal = nzd_subtotal = nzd_FP1_price

        b.input_n_nzd_emailaddress()

        b.click_continuetocheckout()

        assert nzd_subtotal == c.get_nzd_subtotal()

        c.input_nzd_billing_details_and_proceed()

        assert 'FREE'         == d.get_nzd_FP1_price()
        assert nzd_subtotal   == d.get_nzd_subtotal()
        assert nzd_ordertotal == d.get_nzd_ordertotal() == d.get_pay_now_button_price()

        d.pay_via_gratis()

        e.view_receipt()

        assert nzd_FP1_price  == e.get_nzd_FP1_price()
        assert nzd_ordertotal == e.get_nzd_ordertotal()

        print("\nNZD " + e.get_orderid())

        # END
