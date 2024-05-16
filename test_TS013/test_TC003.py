#BACK TO SHOPPING BUTTONS

from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.login          import Login
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus

from utilities.baseclass import baseclass
from time import sleep

class Test_TC003(baseclass):

    def test_TC003(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = Login          (self.driver)
        f = ReviewOrder    (self.driver)
        g = PayerAuth      (self.driver)
        h = OrderStatus    (self.driver)

        a.click_addtobasket1()

        a.click_cart()

        b.click_backtoshopping()

        a.click_cart()