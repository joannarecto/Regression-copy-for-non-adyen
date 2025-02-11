import time

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

class Test_TC006(baseclass):

    # @pytestrail.case('')
    def test_TC006(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayerAuth(self.driver)
        g = OrderStatus    (self.driver)

        # AC3 -4

        a.add_to_cart_PP1()

        a.click_cart()

        b.click_gotocheckout()

        c.input_n_test_006_emailaddress()

        c.click_continuetocheckout()

        d.input_test_billing_details_and_proceed()

        e.verify_physicalproduct_address()

        e.click_edit_deliveryaddress()

        del_firstname       = e.get_delivery_firstname_value()
        del_lastname        = e.get_delivery_lastname_value()
        del_fullname        = f"{del_firstname} {del_lastname}"
        del_country         = e.get_delivery_country_value()
        del_addressline1    = e.get_delivery_addressline1_value()
        del_addressline2    = e.get_delivery_addressline2_value()
        del_city            = e.get_delivery_city_value()
        del_state           = e.get_delivery_state_value()
        del_postcode        = e.get_delivery_postcode_value()

        e.click_cancel_btn()

        #compare fo del
        assert del_fullname        == e.get_delivery_fullname()
        assert del_country         == e.get_delivery_country()
        assert del_addressline1    == e.get_delivery_addressline1()
        assert del_addressline2    == e.get_delivery_addressline2()
        assert del_city            == e.get_delivery_city()
        assert del_state           == e.get_delivery_state()
        assert del_postcode        == e.get_delivery_postcode()

        e.verify_physicalproduct_address()

        e.click_billing_checkbox()

        e.input_test_billing_details_and_proceed2()

        e.verify_physicalproduct_address_uncheck()

        e.click_edit_billingaddress()

        bill_firstname       = e.get_billing_firstname_value()
        bill_lastname        = e.get_billing_lastname_value()
        bill_fullname        = f"{bill_firstname} {bill_lastname}"
        bill_country         = e.get_billing_country_value()
        bill_addressline1    = e.get_billing_addressline1_value()
        bill_addressline2    = e.get_billing_addressline2_value()
        bill_city            = e.get_billing_city_value()
        bill_state           = e.get_billing_state_value()
        bill_postcode        = e.get_billing_postcode_value()

        e.click_cancel_btn()

        e.verify_physicalproduct_address_uncheck()

        # compare fo bill
        assert bill_fullname        == e.get_billing_fullname()
        assert bill_country         == e.get_billing_country()
        assert bill_addressline1    == e.get_billing_addressline1()
        assert bill_addressline2    == e.get_billing_addressline2()
        assert bill_city            == e.get_billing_city()
        assert bill_state           == e.get_billing_state()
        assert bill_postcode        == e.get_billing_postcode()


        e.pay_via_card()

        f.authenticate_payment()

        g.view_customer_information()


        # TY page - Billing details
        assert bill_fullname     == g.get_billing_fullname()
        assert bill_country      == g.get_billing_country()
        assert bill_addressline1 == g.get_billing_addressline1()
        assert bill_addressline2 == g.get_billing_addressline2()
        assert bill_city         == g.get_billing_city()
        assert bill_state        == g.get_billing_state()
        assert bill_postcode     == g.get_billing_postcode()

        # TY page - Delivery details
        assert del_fullname     == g.get_delivery_fullname()
        assert del_country      == g.get_delivery_country()
        assert del_addressline1 == g.get_delivery_addressline1()
        assert del_addressline2 == g.get_delivery_addressline2()
        assert del_city         == g.get_delivery_city()
        assert del_state        == g.get_delivery_state()
        assert del_postcode     == g.get_delivery_postcode()

        g.view_receipt()

        print("\nTEST006 " + g.get_orderid())

        # END
