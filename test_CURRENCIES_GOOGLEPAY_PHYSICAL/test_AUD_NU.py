from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.google_pay_page      import GooglePay
from page_OBJECTS.orderstatus    import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_AUD(baseclass):

    # @pytestrail.case('')
    def test_AUD(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = GooglePay   (self.driver)
        g = OrderStatus    (self.driver)

        a.select_aud()

        a.add_to_cart_PP1()

        aud_PP1_price = a.get_aud_PP1_price()

        aud_ordertotal = aud_subtotal = aud_PP1_price

        a.click_cart()

        assert aud_PP1_price == b.get_aud_PP1_price()
        assert aud_subtotal == b.get_aud_subtotal()

        b.click_gotocheckout()

        c.input_n_aud_emailaddress()

        c.click_continuetocheckout()

        assert aud_subtotal == d.get_aud_subtotal()

        d.input_aud_billing_details_and_proceed()

        assert aud_PP1_price == e.get_aud_PP1_price()
        assert aud_subtotal == e.get_aud_subtotal()
        assert e.get_aud_total_with_shipping() == e.get_aud_ordertotal()

        aud_ordertotal = e.get_aud_ordertotal()

        e.PAY_VIA_GOOGLE_PAY()

        f.LOGIN_AND_PAY()

        g.view_receipt()

        assert aud_PP1_price == g.get_aud_PP1_price()
        assert aud_ordertotal == g.get_aud_ordertotal()

        print("\nAUD " + g.get_orderid())

        # END
