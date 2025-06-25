# GUIDE FOR JUNIOR QA: Modular Test Data Structure

This guide will help you understand and work with the new modular test data structure used in our test automation framework. It is designed to improve maintainability, scalability, and clarity in our test code.

---

## 📁 Folder Structure Overview


---

## 📄 Purpose of Each File

- **`dynamic_data.py`**: Generates dynamic values like unique email addresses.
- **`user_profiles.py`**: Defines user types (e.g., Standard, Premium, Admin).
- **`country_profiles.py`**: Contains address and location data for different countries.
- **`product_catalog.py`**: Stores product names and SKUs used in tests. (check joanna)
- **`user_factory.py`**: Combines user type and country data into a complete user profile.

---

## 🧪 How to Use the User Factory in Tests

```python 
from data_test.user_factory 
from data_test.country_profiles import CountryProfile
from data_test.user_types import UserType

def test_checkout_flow():
    user = TestUserFactory.create_user(CountryProfile.BRAZIL, UserType.New)
    print(user)
```
---
## 🧩 How to Pass User Data to Page Objects
Update your page object methods to accept a user dictionary:

```python
class CheckoutPage:
    def fill_shipping_info(self, user):
        self.enter_first_name(user["first_name"])
        self.enter_last_name(user["last_name"])
        self.enter_address(user["address_line_1"], user["address_line_2"])
        self.enter_city(user["city"])
        self.enter_postcode(user["postcode"])
        self.select_country(user["country"])
