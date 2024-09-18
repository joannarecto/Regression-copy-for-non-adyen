from page_OBJECTS.store       import Store
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.orderstatus import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_CHE(baseclass):

    # @pytestrail.case('')
    def test_CHE(self):

        a = Store       (self.driver)
        b = PreLogin    (self.driver)
        c = Login       (self.driver)
        d = ReviewOrder (self.driver)
        e = OrderStatus (self.driver)

        a.get_access_FP1()

        b.input_e_che_emailaddress()

        b.click_continuetocheckout()

        c.input_che_password()

        c.click_signin()

        d.pay_via_gratis()

        e.view_receipt()

        print("\nCHE " + e.get_orderid())

        # END
