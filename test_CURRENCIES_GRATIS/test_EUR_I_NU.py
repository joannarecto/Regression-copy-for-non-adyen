from page_OBJECTS.store          import Store
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.orderstatus    import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_EUR_I(baseclass):

    # @pytestrail.case('')
    def test_EUR_I(self):

        a = Store          (self.driver)
        b = PreLogin       (self.driver)
        c = BillingDetails (self.driver)
        d = ReviewOrder    (self.driver)
        e = OrderStatus    (self.driver)

        a.select_eur_i()

        eur_i_MB2RPR_price = a.get_eur_i_MB2RPR_price()
        a.get_access_MB2RPR()

        eur_i_ordertotal = eur_i_subtotal = eur_i_MB2RPR_price

        b.input_n_eur_i_emailaddress()

        b.click_continuetocheckout()

        assert eur_i_subtotal == c.get_eur_i_subtotal()

        c.input_eur_i_billing_details_and_proceed()

        assert 'FREE'           == d.get_eur_i_MB2RPR_price()
        assert eur_i_subtotal   == d.get_eur_i_subtotal()
        assert eur_i_ordertotal == d.get_eur_i_ordertotal()

        d.pay_via_gratis()

        e.view_receipt()

        assert eur_i_MB2RPR_price == e.get_eur_i_MB2RPR_price()
        assert eur_i_ordertotal   == e.get_eur_i_ordertotal()

        print("\nEUR-I " + e.get_orderid())

        # END
