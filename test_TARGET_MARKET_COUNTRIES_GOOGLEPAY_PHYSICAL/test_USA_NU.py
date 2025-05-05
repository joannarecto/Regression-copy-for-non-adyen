from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.google_pay_page      import GooglePay
from page_OBJECTS.orderstatus    import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_USA(baseclass):

    # @pytestrail.case('')
    def test_USA(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = GooglePay(self.driver)
        g = OrderStatus    (self.driver)

        a.add_to_cart_PP1()

        a.click_cart()

        b.click_gotocheckout()

        c.input_n_usa_emailaddress()

        c.click_continuetocheckout()

        d.input_usa_billing_details_and_proceed()

        e.PAY_VIA_GOOGLE_PAY()

        f.LOGIN_AND_PAY()

        g.view_receipt()

        print("\nUSA " + g.get_orderid())

        # END
