#DCESC-599-AC1&AC2
import time

from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus

from selenium.common.exceptions import NoSuchElementException



from utilities.baseclass import baseclass

class Test_TC011(baseclass):

    def test_TC011(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayerAuth      (self.driver)
        g = OrderStatus    (self.driver)


        # stg
        # uk_price_after_discount = "£15.00"
        # usa_price_after_discount = "US $17.25"
        # ph_price_after_discount = "US $17.25"

        # stg
        uk_price_after_discount = "£14.78"
        usa_price_after_discount = "US $49.50"
        ph_price_after_discount = "US $33.00"


        a.add_to_cart_PP1()

        a.click_cart()

        b.click_gotocheckout()

        c.input_n_test_011_emailaddress()

        c.click_continuetocheckout()

        d.input_test_billing_details_and_proceed()


        # get shipping details
        shipping_charge = e.get_gbp_shippingcharge()
        delivery_date   = e.estimate_delivery_date()
        delivery_days   = e.estimate_delivery_days()


        # get charges
        # subtotal_charge    = e.get_gbp_subtotal()
        delivery_charge      = e.get_gbp_deliverycharge()
        order_total          = e.get_gbp_ordertotal()

        assert shipping_charge == delivery_charge


        e.use_freeshippingcode()

        assert not shipping_charge  == e.get_gbp_shippingcharge()
        assert e.get_gbp_shippingcharge() == "£0.00"
        free_shipping_charge        =  e.get_gbp_shippingcharge()
        assert delivery_date        == e.estimate_delivery_date()
        assert delivery_days        == e.estimate_delivery_days()

        assert not delivery_charge  == e.get_gbp_deliverycharge()
        assert e.get_gbp_deliverycharge() == "£0.00"
        free_delivery_charge         = e.get_gbp_deliverycharge()
        assert free_shipping_charge == free_delivery_charge
        assert not order_total      == e.get_gbp_ordertotal()
        free_order_total             = e.get_gbp_ordertotal()
        assert free_order_total     == e.get_gbp_subtotal()


        e.click_card()
        assert free_order_total == e.get_pay_now_button_price()

        e.check_freeshippingcode_displayed()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        # compare charges
        # assert subtotal_charge    == g.get_gbp_subtotal()
        assert free_delivery_charge == g.get_gbp_deliverycharge()
        assert free_order_total     == g.get_gbp_ordertotal()


        print("\nTEST0011 " + g.get_orderid())

        # END
