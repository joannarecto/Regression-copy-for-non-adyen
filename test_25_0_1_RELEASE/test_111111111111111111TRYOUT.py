import time
from urllib.parse import urlparse, parse_qs

from page_OBJECTS.store          import Store
from page_OBJECTS.basket         import Basket
from page_OBJECTS.prelogin       import PreLogin
from page_OBJECTS.billingdetails import BillingDetails
from page_OBJECTS.revieworder    import ReviewOrder
from page_OBJECTS.paypal         import PayPal
from page_OBJECTS.orderstatus    import OrderStatus

import gzip
import json
import pytest

# from pytest_testrail.plugin import pytestrail
from utilities.baseclass    import baseclass

class Test_TC001(baseclass):

    # @pytestrail.case('')
    def test_TC001(self):

        a = Store          (self.driver)
        b = Basket         (self.driver)
        c = PreLogin       (self.driver)
        d = BillingDetails (self.driver)
        e = ReviewOrder    (self.driver)
        f = PayPal         (self.driver)
        g = OrderStatus    (self.driver)

        a.add_to_cart_TT_B2FSS()

        a.click_cart()

        time.sleep(5)

        b.click_gotocheckout()

        c.input_n_test_001_emailaddress()

        c.click_continuetocheckout()

        d.input_test_billing_details_and_proceed()

        for request in self.driver.requests:
            if request.response:
                if "payment-methods" in request.url and request.method == "GET":
                    try:
                        response_body = gzip.decompress(request.response.body).decode('utf-8')
                        response_json = json.loads(response_body)

                        get_greenzone_status = response_json.get("isGlobalGreenzoneEnabled", None)
                        print("\nisGlobalGreenzoneEnabled:", get_greenzone_status)
                    except Exception as e:
                        print("\nan error occurred:", e)



        e.pay_via_paypal()

        f.login_and_pay()

        # for request in self.driver.requests:
        #     if request.response:
        #         if "save-order" in request.url and request.method == "POST":
        #             try:
        #                 # Check if the response is gzipped
        #                 content_encoding = request.response.headers.get('Content-Encoding', '')
        #
        #                 if content_encoding == 'gzip':
        #                     # Gzip-decompress the response body if it's gzipped
        #                     response_body = gzip.decompress(request.response.body).decode('utf-8')
        #                 else:
        #                     # If not gzipped, just decode the response body directly
        #                     response_body = request.response.body.decode('utf-8')
        #
        #                 # Parse the JSON response
        #                 response_json = json.loads(response_body)
        #
        #                 # Extract the orderId from the response
        #                 get_save_orderid = response_json.get("orderId", None)
        #                 print("\nSave-order id:", get_save_orderid)
        #
        #             except Exception as e:
        #                 print("\nAn error occurred:", e)


        # Set a flag to stop after the first orderId is found
        found_orderid = False

        for request in self.driver.requests:
            if not found_orderid:  # Check if we've already found the orderId
                if request.response:
                    if "session" in request.url and request.method == "GET":
                        try:
                            # Parse the URL to extract the query string parameters
                            parsed_url = urlparse(request.url)
                            query_params = parse_qs(parsed_url.query)

                            # Extract 'orderId' from query parameters and ensure it's a single value
                            get_save_orderid = query_params.get("orderId", [None])[0]  # Get the first value if exists

                            # Only print if the orderId is found
                            if get_save_orderid:
                                print(f"\nSave-order id: {get_save_orderid} from URL: {request.url}")
                                found_orderid = True  # Set flag to True to stop further processing

                        except Exception as e:
                            print("\nAn error occurred:", e)

        # get_paypal_orderid = None

        # for request in self.driver.requests:
        #     if request.response:
        #         if "session" in request.url and request.method == "POST":
        #             try:
        #                 response_body = gzip.decompress(request.response.body).decode('utf-8')
        #                 response_json = json.loads(response_body)
        #
        #                 get_paypal_orderid = response_json.get("custom10", None)
        #                 print("\nPaypal session orderId:", get_paypal_orderid)
        #             except Exception as e:
        #                 print("\nan error occurred:", e)
        #
        # g.view_receipt()
        #
        # print("\nBRA " + g.get_orderid())

        # END
