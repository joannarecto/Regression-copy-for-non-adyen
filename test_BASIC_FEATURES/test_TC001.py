#FOOTERS & LINKS

from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.login          import Login
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus

from utilities.baseclass import baseclass

class Test_TC001(baseclass):

    @pytest.mark.skip()
    def test_TC001(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = Login          (self.driver)
        f = ReviewOrder    (self.driver)
        g = PayerAuth      (self.driver)
        h = OrderStatus    (self.driver)

        a.add_to_cart_TT_B2FSS()

        a.click_cart()

        # basket page

        b.verify_footers_are_accessible()

        b.click_gotocheckout()

        # prelogin page

        c.verify_footers_are_accessible()

        c.input_n_test_001_emailaddress()

        c.click_continuetocheckout()

        # billing details page

        d.verify_footers_are_accessible()

        d.click_chevron()

        b.click_gotocheckout()

        c.input_e_test_001_emailaddress()

        c.click_continuetocheckout()

        # login page

        e.verify_footers_are_accessible()

        e.input_test_001_password()

        e.click_signin()

        # review order page

        f.verify_footers_are_accessible()

        f.pay_via_failed_challenge_card()

        g.authenticate_payment()

        # order status (failed) page

        h.verify_footers_are_accessible()

        h.check_details_and_try_again()

        f.pay_via_amex_challenge_card()

        g.authenticate_payment()

        # order status (successful) page

        h.verify_footers_are_accessible()

        h.view_receipt()

        print("\nTC001 " + h.get_orderid())

        # END
