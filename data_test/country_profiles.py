from selenium.webdriver.common.by import By
from utilities.wait import wait_for_element
from time import sleep

class CountryProfile:
    CANADA = {
        "country": "Canada",
        "address_line_1": "123 Maple Street",
        "address_line_2": "Suite 100",
        "city": "Toronto",
        "postcode": "M5H 2N2"
    }

    BRAZIL = {
        "country": "Brazil",
        "address_line_1": "Test Address 1",
        "address_line_2": "Test Address 2",
        "city": "Test City",
        "state": "Acre",
        "postcode": "12345678"
    }
