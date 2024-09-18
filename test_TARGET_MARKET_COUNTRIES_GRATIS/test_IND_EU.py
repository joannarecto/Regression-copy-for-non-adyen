from page_OBJECTS.store       import Store
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.orderstatus import OrderStatus

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_IND(baseclass):

    # @pytestrail.case('')
    def test_IND(self):

        a = Store       (self.driver)
        b = PreLogin    (self.driver)
        c = Login       (self.driver)
        d = ReviewOrder (self.driver)
        e = OrderStatus (self.driver)

        a.get_access_FP1()

        b.input_e_ind_emailaddress()

        b.click_continuetocheckout()

        c.input_ind_password()

        c.click_signin()

        d.pay_via_gratis()

        e.view_receipt()

        print("\nIND " + e.get_orderid())

        # END
