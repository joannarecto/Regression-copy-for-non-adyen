import pytest
from page_OBJECTS.store       import Store
from page_OBJECTS.basket      import Basket
from page_OBJECTS.prelogin    import PreLogin
from page_OBJECTS.login       import Login
from page_OBJECTS.revieworder import ReviewOrder
from page_OBJECTS.payerauth   import PayerAuth
from page_OBJECTS.orderstatus import OrderStatus
from selenium.common import NoSuchElementException

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_USD(baseclass):

    # @pytestrail.case('')
    @pytest.mark.skip
    def test_USD(self):

        a = Store(self.driver)
        b = Login(self.driver)
        c = Basket(self.driver)
        d = PayerAuth(self.driver)
        e = OrderStatus(self.driver)

        a.select_usd()

        a.go_to_the_login_page_from_the_store()

        b.login_existing_user_usd()

        a.click_cart()

        c.remove_all_items()

        try:
            assert b.basketproducts_displayed() == False
        except NoSuchElementException:
            pass

        assert b.empty_basket_label() == "Your basket is empty"

        # END