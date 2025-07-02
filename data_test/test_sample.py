import pytest

@pytest.mark.parametrize("payment_method", ["CARD", "GOOGLE_PAY", "PAYPAL"])
@pytest.mark.parametrize("user_type", ["NEW", "EXISTING"])
def test_checkout_australia(self, payment_method, user_type):
    a, b, c, d, e, f, i, currency, product, country, address = self.GET_AUSTRALIA_TEST_DATA()

    a.SELECT_CURRENCY(currency)
    a.ADD_TO_CART(product)
    item_price = a.GET_PRICE()
    a.CLICK_CART()

    assert item_price == b.GET_BASKET_PRODUCT_PRICE()
    assert item_price == b.GET_BASKET_SUBTOTAL()

    b.CLICK_GO_TO_CHECKOUT()

    # Handle user type
    if user_type == "NEW":
        c.LOGIN_GUEST_USER()
    elif user_type == "EXISTING":
        c.LOGIN_EXISTING_USER()

    assert item_price == d.GET_ADDRESS_DETAILS_SUBTOTAL()

    c.INPUT_ADDRESS_DETAILS(country, address)

    assert item_price == e.GET_RO_ORDERTOTAL()
    assert item_price == e.GET_RO_SUBTOTAL()
    assert item_price == e.GET_RO_PRODUCT_PRICE()

    # Handle payment method
    if payment_method == "CARD":
        e.CLICK_CARDS()
        assert item_price == e.GET_PAY_BUTTON_PRICE()
        e.PAY_VIA_FRICTIONLESS_MASTERCARD()
    elif payment_method == "GOOGLE_PAY":
        e.PAY_VIA_GOOGLE_PAY()
    elif payment_method == "PAYPAL":
        e.PAY_VIA_PAYPAL()

    f.CLICK_YOUR_RECEIPT()
    assert item_price == f.GET_RECEIPT_SUBTOTAL()
    assert item_price == f.GET_RECEIPT_ORDERTOTAL()

    print(f"\nAUSTRALIA_{payment_method}_{user_type} " + f.GET_ORDER_NUMBER())
