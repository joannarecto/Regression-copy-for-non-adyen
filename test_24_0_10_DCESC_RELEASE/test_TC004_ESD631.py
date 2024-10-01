from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus
from page_OBJECTS.login       import Login
from selenium.common import NoSuchElementException

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_TC004(baseclass):

    # @pytestrail.case('')
    def test_TC004(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayerAuth(self.driver)
        g = OrderStatus    (self.driver)
        h = Login(self.driver)

        a.add_to_cart_TT_B2FSS()

        a.click_cart()

        b.click_gotocheckout()

        c.input_n_test_004_emailaddress()

        c.click_continuetocheckout()

        d.click_chevron()

        try:
            assert b.basketproducts_displayed() == True
        except NoSuchElementException:
            assert False, "NoSuchElementException occurred, test failed"

        assert not "Your basket is empty" in b.page_src()

        b.click_gotocheckout()

        c.input_e_test_004_emailaddress()

        c.click_continuetocheckout()

        h.input_test_001_password()

        h.click_signin()

        try:
            assert e.basketproducts_displayed() == True
        except NoSuchElementException:
            assert False, "NoSuchElementException occurred, test failed"

        assert not "Your basket is empty" in e.page_src()

        e.pay_via_card()

        f.authenticate_payment()

        g.view_receipt()

        print("\nESD-631 " + g.get_orderid())

        # END
