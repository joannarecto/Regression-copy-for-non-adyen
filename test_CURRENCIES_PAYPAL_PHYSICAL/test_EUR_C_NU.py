from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.paypal      import PayPal
from page_OBJECTS.orderstatus    import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_EUR_C(baseclass):

    # @pytestrail.case('')
    def test_EUR_C(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayPal   (self.driver)
        g = OrderStatus    (self.driver)

        a.select_eur_c()

        a.add_to_cart_PP1()

        eur_c_PP1_price = a.get_eur_c_PP1_price()

        eur_c_ordertotal = eur_c_subtotal = eur_c_PP1_price

        a.click_cart()

        assert eur_c_PP1_price == b.get_eur_c_PP1_price()
        assert eur_c_subtotal == b.get_eur_c_subtotal()

        b.click_gotocheckout()

        c.input_n_eur_c_emailaddress()

        c.click_continuetocheckout()

        assert eur_c_subtotal == d.get_eur_c_subtotal()

        d.input_eur_c_billing_details_and_proceed()

        assert eur_c_PP1_price == e.get_eur_c_PP1_price()
        assert eur_c_subtotal == e.get_eur_c_subtotal()
        assert e.get_eur_c_total_with_shipping() == e.get_eur_c_ordertotal()

        eur_c_ordertotal = e.get_eur_c_ordertotal()

        e.pay_via_paypal()

        f.login_and_pay()

        g.view_receipt()

        assert eur_c_PP1_price == g.get_eur_c_PP1_price()
        assert eur_c_ordertotal == g.get_eur_c_ordertotal()

        print("\nEUR-C " + g.get_orderid())

        # END
