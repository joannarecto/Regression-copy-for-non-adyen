from time import sleep

from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
from page_OBJECTS.orderstatus import OrderStatus
from selenium.common import NoSuchElementException

from utilities.baseclass import baseclass

class Test_TC001(baseclass):

    def test_TC001(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayerAuth   (self.driver)
        g = OrderStatus (self.driver)

        a.get_access_FP1()

        c.input_e_test_001_emailaddress()

        c.click_continuetocheckout()

        d.input_test_001_password()

        d.click_signin()


        def run_validations(e):
            # AC1 - Detection of Free Products &
            # AC2 - Discount Code
            try:
                assert e.discount_checkbox_section() == False
            except NoSuchElementException:
                pass

            assert not "Got a discount code?" in e.order_summary_section()


            # AC1 - Detection of Free Products &
            # AC3 - Payment Methods
            try:
                assert e.payment_method_section() == False
            except NoSuchElementException:
                pass

            assert not "Card" in e.order_summary_section()
            assert not "PayPal" in e.order_summary_section()

            # AC4 - Payment Heading
            assert not "How would you like to pay?" in e.order_summary_section()

            # AC7 - Submit Order Button
            assert "0.00" == e.gratis_btn_price_check()

            # AC8 - FREE label
            assert "FREE" == e.gratis_label_check()
            sleep(3)

        run_validations(e)


        # AC5 - Back Chevron
        e.click_chevron()
        assert "Shopfront" in a.page_src()
        a.get_access_FP1()
        sleep(5)
        run_validations(e)


        # AC6 - Back Button
        e.go_back()
        assert "Shopfront" in a.page_src()
        a.get_access_FP1()
        sleep(5)
        run_validations(e)

        e.pay_via_gratis()

        g.view_receipt()

        print("\nTS001 " + g.get_orderid())

        # END
