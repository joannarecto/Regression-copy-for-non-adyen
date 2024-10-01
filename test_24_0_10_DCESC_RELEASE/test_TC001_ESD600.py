from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_TC001(baseclass):

    # @pytestrail.case('')
    def test_TC001(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayerAuth(self.driver)
        g = OrderStatus    (self.driver)

        a.add_to_cart_TT_B2FSS()

        a.click_cart()

        b.click_gotocheckout()

        c.input_n_test_001_emailaddress()

        c.click_continuetocheckout()

        # AC1 - Main Header

        assert "Address details" == d.label_mainHeader()
        assert not "Card billing details" == d.label_mainHeader()
        print("\n" + d.label_mainHeader())

        # AC2 - Complete your order

        assert "Ready to complete your order?" == d.label_completeHeader()
        print(d.label_completeHeader())

        # AC3 - Secondary Heading

        assert "Your details" == d.label_secondary_heading()
        assert not "Cardholder billing details" == d.label_secondary_heading()
        print(d.label_secondary_heading())

        # AC4 - First Name Field

        assert "First name" == d.label_firstName_field()
        assert not "Cardholder First name" == d.label_firstName_field()
        print(d.label_firstName_field())

        # AC5 - Last Name Field

        assert "Last name" == d.label_lastName_field()
        assert not "Cardholder Last name" == d.label_lastName_field()
        print(d.label_lastName_field())

        # AC6 - Country Dropdown

        assert "Country" == d.label_country_dropdown()
        assert not "Country (billing address)" == d.label_country_dropdown()
        print(d.label_country_dropdown())

        # AC7 - Address Line Field

        assert "Address line 1" == d.label_laddressLine1()
        assert not "Billing address line 1" == d.label_laddressLine1()
        print(d.label_laddressLine1())

        # AC8 - Address Line 2 Field

        assert "Address line 2 (optional)" == d.label_laddressLine2()
        assert not "Billing address line 2 (optional)" == d.label_laddressLine2()
        print(d.label_laddressLine2())

        # AC9 - Page Title Update

        assert "Address details" in self.driver.title
        assert not "Billing details" in self.driver.title
        print(self.driver.title)

        # AC10 - URL Update

        assert "/address-details" in self.driver.current_url
        assert not "/billing-details" in self.driver.current_url
        print(self.driver.current_url)

        d.input_test_billing_details_and_proceed()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        print("\nESD-600 " + g.get_orderid())

        # END
