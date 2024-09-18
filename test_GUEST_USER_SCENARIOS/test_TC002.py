#DCESC-597

from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus

from utilities.baseclass import baseclass
from time import sleep

class Test_TC002(baseclass):

    def test_TC002(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayerAuth      (self.driver)
        g = OrderStatus    (self.driver)

        a.add_to_cart_TT_B2FSS()

        a.click_cart()

        b.go_back()

        a.buy_now_TT_C1ASS()

        c.input_n_test_002_emailaddress()

        c.click_continuetocheckout()

        assert d.chevron_enabled()        == True
        assert d.backtoshopping_enabled() == True

        d.input_test_billing_details_and_proceed()

        assert e.chevron_enabled()        == True
        assert e.backtoshopping_enabled() == True

        e.delete_item1()

        assert e.continueshopping_enabled() == True

        e.undo_item1()

        e.go_back()

        assert b.chevron_enabled()        == True
        assert b.backtoshopping_enabled() == True

        b.delete_item2()
        b.delete_item1()

        assert b.continueshopping_enabled() == True

        b.undo_item2()
        b.undo_item1()

        b.saveforlater_item2()
        b.saveforlater_item1()

        assert b.continueshopping_enabled() == True

        b.movetobasket_item2()
        b.movetobasket_item1()

        b.click_gotocheckout()
        sleep(20)

        e.pay_via_mastercard_challenge_card()

        f.authenticate_payment()

        g.view_receipt()

        print("\nTC002 " + g.get_orderid())

        # END
