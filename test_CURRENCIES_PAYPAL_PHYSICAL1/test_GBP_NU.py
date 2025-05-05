from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.paypal      import PayPal
from page_OBJECTS.orderstatus    import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_GBP(baseclass):

    # @pytestrail.case('')
    def test_GBP(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayPal   (self.driver)
        g = OrderStatus    (self.driver)

        a.add_to_cart_PP1()

        gbp_PP1_price = a.get_gbp_PP1_price()

        gbp_ordertotal = gbp_subtotal = gbp_PP1_price

        a.click_cart()

        assert gbp_PP1_price == b.get_gbp_PP1_price()
        assert gbp_subtotal == b.get_gbp_subtotal()

        b.click_gotocheckout()

        c.input_n_gbp_emailaddress()

        c.click_continuetocheckout()

        assert gbp_subtotal == d.get_gbp_subtotal()

        d.input_gbp_billing_details_and_proceed()

        assert gbp_PP1_price == e.get_gbp_PP1_price()
        assert gbp_subtotal == e.get_gbp_subtotal()
        assert e.get_gbp_total_with_shipping() == e.get_gbp_ordertotal()

        gbp_ordertotal = e.get_gbp_ordertotal()

        e.pay_via_paypal()

        f.login_and_pay()

        g.view_receipt()

        assert gbp_PP1_price == g.get_gbp_PP1_price()
        assert gbp_ordertotal == g.get_gbp_ordertotal()

        print("\nGBP " + g.get_orderid())

        # END
