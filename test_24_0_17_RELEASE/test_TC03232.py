#DCESC-599-AC1&AC2
import time

from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.payerauth      import PayerAuth
from page_OBJECTS.orderstatus    import OrderStatus

import gzip
import json
import pytest


from selenium.common.exceptions import NoSuchElementException



from utilities.baseclass import baseclass

class Test_TC001(baseclass):
    @pytest.mark.skip
    def test_TC001(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayerAuth      (self.driver)
        g = OrderStatus    (self.driver)


        # stg
        # uk_price_after_discount = "£15.00"
        # usa_price_after_discount = "US $17.25"
        # ph_price_after_discount = "US $17.25"

        # stg
        uk_price_after_discount = "£14.78"
        usa_price_after_discount = "US $49.50"
        ph_price_after_discount = "US $33.00"


        a.add_to_cart_PP2()

        a.click_cart()

        b.click_gotocheckout()

        c.input_n_test_002_emailaddress()

        c.click_continuetocheckout()

        d.input_test_billing_details_and_proceed()

        get_catalogId = None

        # for request in self.driver.requests:
        #     if request.response:
        #         if "create-order" in request.url and request.method == "POST":  # Check for 'create-order' POST request
        #             try:
        #                 # HANDLE GZIP DECODING
        #                 response_body = gzip.decompress(request.response.body).decode('utf-8')
        #                 response_json = json.loads(response_body)
        #
        #                 # EXTRACT CATALOGID (if needed, but seems irrelevant here)
        #                 get_catalogId = response_json.get("isTaxExclusive", None)
        #                 print("\ncatalogId:", get_catalogId)
        #
        #                 # EXTRACT custom10 for "Physical Product 1"
        #                 order_products = response_json.get("order", {}).get("orderProducts", None)
        #                 for product in order_products:
        #                     if product.get("name") == "Physical Product 2":
        #                         custom10_value = product.get("product", {}).get("custom10", None)
        #                         if custom10_value:
        #                             print("\nCustom10 Value for 'Physical Product 2':", custom10_value)
        #                         else:
        #                             print("\nNo custom10 value found for 'Physical Product 2'")
        #             except Exception as e:
        #                 print("\nan error occurred:", e)

        get_catalogId = None

        for request in self.driver.requests:
            if request.response:
                if "create-order" in request.url and request.method == "POST":
                    try:
                        # HANDLE GZIP DECODING
                        response_body = gzip.decompress(request.response.body).decode('utf-8')
                        response_json = json.loads(response_body)

                        # EXTRACT CATALOGID
                        get_catalogId = response_json.get("custom10", None)
                        print("\ncatalogId:", get_catalogId)
                    except Exception as e:
                        print("\nan error occurred:", e)

        # assert i.cad_catalogId == get_catalogId

        # b.click_gotocheckout()
        #
        # c.input_n_test_001_emailaddress()
        #
        # c.click_continuetocheckout()
        #
        # d.input_test_billing_details_and_proceed()
        #
        # get_catalogId = None
        #
        # for request in self.driver.requests:
        #     if request.response:
        #         if "payment-methods" in request.url and request.method == "GET":
        #             try:
        #                 # HANDLE GZIP DECODING
        #                 response_body = gzip.decompress(request.response.body).decode('utf-8')
        #                 response_json = json.loads(response_body)
        #
        #                 # EXTRACT CATALOGID
        #                 get_catalogId = response_json.get("isTaxExclusive", None)
        #                 print("\ncatalogId:", get_catalogId)
        #             except Exception as e:
        #                 print("\nan error occurred:", e)
        #
        # # assert i.cad_catalogId == get_catalogId
        #
        # # END
