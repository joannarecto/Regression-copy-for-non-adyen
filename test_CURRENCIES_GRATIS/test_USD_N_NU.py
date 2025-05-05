from page_OBJECTS.store          import Store
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.orderstatus    import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_USD_N(baseclass):

    # @pytestrail.case('')
    def test_USD_N(self):

        a = Store          (self.driver)
        b = PreLogin       (self.driver)
        c = BillingDetails (self.driver)
        d = ReviewOrder    (self.driver)
        e = OrderStatus    (self.driver)

        a.select_usd_n()

        usd_n_FP1_price = a.get_usd_n_FP1_price()
        a.get_access_FP1()

        usd_n_ordertotal = usd_n_subtotal = usd_n_FP1_price

        b.input_n_usd_n_emailaddress()

        b.click_continuetocheckout()

        assert usd_n_subtotal == c.get_usd_n_subtotal()

        c.input_usd_n_billing_details_and_proceed()

        assert 'FREE'           == d.get_usd_n_PP1_price()
        assert usd_n_subtotal   == d.get_usd_n_subtotal()
        assert usd_n_ordertotal == d.get_usd_n_ordertotal() == d.get_pay_now_button_price()

        d.pay_via_gratis()

        e.view_receipt()

        assert usd_n_FP1_price == e.get_usd_n_PP1_price()
        assert usd_n_ordertotal   == e.get_usd_n_ordertotal()

        print("\nUSD-N " + e.get_orderid())

        # END
