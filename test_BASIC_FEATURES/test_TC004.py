#PRODUCT IMAGE BORDER

from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
from page_OBJECTS.orderstatus import OrderStatus

from utilities.baseclass import baseclass

class Test_TC004(baseclass):

    def test_TC004(self):

        a = Store       (self.driver)
        b = Basket      (self.driver)
        c = PreLogin    (self.driver)
        d = Login       (self.driver)
        e = ReviewOrder (self.driver)
        f = PayerAuth   (self.driver)
        g = OrderStatus (self.driver)

        a.add_to_cart_TT_B2FSS()

        a.clear_product_searchfield()

        a.add_to_cart_TT_C1ASS()

        a.click_cart()

        TT_B2FSS = b.get_TT_B2FSS()

        assert TT_B2FSS.value_of_css_property('box-shadow')          == 'rgba(0, 0, 0, 0.08) 0px 2px 10px 0px'
        assert TT_B2FSS.value_of_css_property('border-top-width')    == '1.2px'
        assert TT_B2FSS.value_of_css_property('border-bottom-width') == '1.2px'
        assert TT_B2FSS.value_of_css_property('border-left-width')   == '1.2px'
        assert TT_B2FSS.value_of_css_property('border-right-width')  == '1.2px'
        assert TT_B2FSS.value_of_css_property('border-image-width')  == '1'

        TT_C1ASS = b.get_TT_C1ASS()

        assert TT_C1ASS.value_of_css_property('box-shadow')          == 'rgba(0, 0, 0, 0.08) 0px 2px 10px 0px'
        assert TT_C1ASS.value_of_css_property('border-top-width')    == '1.2px'
        assert TT_C1ASS.value_of_css_property('border-bottom-width') == '1.2px'
        assert TT_C1ASS.value_of_css_property('border-left-width')   == '1.2px'
        assert TT_C1ASS.value_of_css_property('border-right-width')  == '1.2px'
        assert TT_C1ASS.value_of_css_property('border-image-width')  == '1'

        b.click_gotocheckout()

        c.input_e_test_004_emailaddress()

        c.click_continuetocheckout()

        d.input_test_004_password()

        d.click_signin()

        TT_B2FSS = e.get_TT_B2FSS()

        assert TT_B2FSS.value_of_css_property('box-shadow')          == 'rgba(0, 0, 0, 0.08) 0px 2px 10px 0px'
        assert TT_B2FSS.value_of_css_property('border-top-width')    == '1.2px'
        assert TT_B2FSS.value_of_css_property('border-bottom-width') == '1.2px'
        assert TT_B2FSS.value_of_css_property('border-left-width')   == '1.2px'
        assert TT_B2FSS.value_of_css_property('border-right-width')  == '1.2px'
        assert TT_B2FSS.value_of_css_property('border-image-width')  == '1'

        TT_C1ASS = e.get_TT_C1ASS()

        assert TT_C1ASS.value_of_css_property('box-shadow')          == 'rgba(0, 0, 0, 0.08) 0px 2px 10px 0px'
        assert TT_C1ASS.value_of_css_property('border-top-width')    == '1.2px'
        assert TT_C1ASS.value_of_css_property('border-bottom-width') == '1.2px'
        assert TT_C1ASS.value_of_css_property('border-left-width')   == '1.2px'
        assert TT_C1ASS.value_of_css_property('border-right-width')  == '1.2px'
        assert TT_C1ASS.value_of_css_property('border-image-width')  == '1'

        e.pay_via_amex_challenge_card()

        f.authenticate_payment()

        TT_B2FSS = g.get_TT_B2FSS()

        assert TT_B2FSS.value_of_css_property('box-shadow')          == 'rgba(0, 0, 0, 0.08) 0px 2px 10px 0px'
        assert TT_B2FSS.value_of_css_property('border-top-width')    == '1.2px'
        assert TT_B2FSS.value_of_css_property('border-bottom-width') == '1.2px'
        assert TT_B2FSS.value_of_css_property('border-left-width')   == '1.2px'
        assert TT_B2FSS.value_of_css_property('border-right-width')  == '1.2px'
        assert TT_B2FSS.value_of_css_property('border-image-width')  == '1'

        TT_C1ASS = g.get_TT_C1ASS()

        assert TT_C1ASS.value_of_css_property('box-shadow')          == 'rgba(0, 0, 0, 0.08) 0px 2px 10px 0px'
        assert TT_C1ASS.value_of_css_property('border-top-width')    == '1.2px'
        assert TT_C1ASS.value_of_css_property('border-bottom-width') == '1.2px'
        assert TT_C1ASS.value_of_css_property('border-left-width')   == '1.2px'
        assert TT_C1ASS.value_of_css_property('border-right-width')  == '1.2px'
        assert TT_C1ASS.value_of_css_property('border-image-width')  == '1'

        g.view_receipt()

        print("\nTC004 " + g.get_orderid())

        # END
