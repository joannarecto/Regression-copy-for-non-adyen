from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus
from selenium.common import NoSuchElementException

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_TC003(baseclass):

    # @pytestrail.case('')
    def test_TC003(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayerAuth(self.driver)
        g = OrderStatus    (self.driver)


        #Physical & Digital products (Mixed basket)

        def yesChargeandavail(e):
            assert "Delivery" in b.get_delivery_charge_text()
            assert "Calculated at checkout" in b.get_delivery_charge_text()
            assert "Availability can vary by location. We'll confirm everything at checkout." == b.get_avail_charge_text()

        def noChargebutyesavail(e):
            assert not "Delivery" in b.page_src()
            assert not "Calculated at checkout" in b.page_src()
            assert "Availability can vary by location. We'll confirm everything at checkout." == b.get_avail_charge_text()

        def noChargeandavail(e):
            assert not "Delivery" in b.page_src()
            assert not "Calculated at checkout" in b.page_src()
            assert not "Availability can vary by location. We'll confirm everything at checkout." in b.page_src()

        #AC1

        a.add_to_cart_PP1()

        a.clear_product_searchfield()

        a.add_to_cart_TT_B2FSS()

        a.click_cart()

        yesChargeandavail(e)


        #AC3 - left with digital

        b.saveforlater_PP1()

        noChargebutyesavail(e)

        b.movetobasket_PP1()


        #AC8 - left with Physical

        b.saveforlater_TT_B2FSS()

        yesChargeandavail(e)

        b.movetobasket_TT_B2FSS()


        #AC2 - left with Digital

        b.YI_delete_PP1()

        noChargebutyesavail(e)

        b.undo_item1()


        #AC7 - left with physical
        b.YI_delete_TT_B2FSS()

        yesChargeandavail(e)

        b.undo_item1()

        # AC5 save all
        b.saveforlater_TT_B2FSS()
        b.saveforlater_PP1()

        noChargeandavail(e)

        b.movetobasket_TT_B2FSS()
        b.movetobasket_PP1()

        b.YI_delete_TT_B2FSS()
        b.YI_delete_PP1()

        noChargeandavail(e)

        b.click_continueshopping()

        a.add_to_cart_PP1()

        a.click_cart()

        b.click_gotocheckout()

        c.input_n_test_003_emailaddress()

        c.click_continuetocheckout()

        d.input_test_billing_details_and_proceed()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        print("\nTEST003 " + g.get_orderid())

        # END
