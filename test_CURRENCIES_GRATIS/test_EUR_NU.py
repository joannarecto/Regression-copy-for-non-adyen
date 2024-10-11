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

        a.select_eur()

        eur_FP1_price = a.get_eur_FP1_price()
        a.get_access_FP1()

        eur_ordertotal = eur_subtotal = eur_FP1_price

        b.input_n_eur_emailaddress()

        b.click_continuetocheckout()

        assert eur_subtotal == c.get_eur_subtotal()

        c.input_eur_billing_details_and_proceed()

        assert 'FREE'         == d.get_eur_FP1_price()
        assert eur_subtotal   == d.get_eur_subtotal()
        assert eur_ordertotal == d.get_eur_ordertotal() == d.get_pay_now_button_price()

        d.pay_via_gratis()

        e.view_receipt()

        assert eur_FP1_price  == e.get_eur_FP1_price()
        assert eur_ordertotal == e.get_eur_ordertotal()

        print("\nEUR " + e.get_orderid())

        # END
