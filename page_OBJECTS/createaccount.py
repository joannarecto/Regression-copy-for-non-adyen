from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from page_OBJECTS.data import Data


class CreateAccount:

    def __init__(self, driver):
        self.driver = driver

    firstname           = (By.XPATH, "(//input[@name='profile.firstName'])[3]")

    lastname            = (By.XPATH, "(//input[@name='profile.lastName'])[3]")

    email               = (By.XPATH, "(//input[@name='email'])[4]")

    password            = (By.XPATH, "(//input[@name='password'])[5]")

    password2           = (By.XPATH, "(//input[@name='passwordRetype'])[5]")

    country             = (By.XPATH, "(//select[@name='profile.country'])[3]")

    confirmpassword = (By.XPATH, "(//*[contains(@id,'gigya-password')])[2]")

    agree               = (By.XPATH, "(//*[contains(@class,'fd-checkbox')])[3]")

    termsofuse      = (By.XPATH, "//*[contains(@id,'gigya-checkbox')]")

    submit          = (By.XPATH, "//input[@class='gigya-input-submit' and @value='Continue']")


    #-------------------------------------------------------------------------------------------------------------------

    def page_src(self):
        body = self.driver.find_element(By.TAG_NAME, 'body').text
        return body

    #-------------------------------------------------------------------------------------------------------------------

    def check_country_text(self):
        value = self.driver.find_element(*CreateAccount.country)
        select = Select(value)
        selected_option = select.first_selected_option
        selected_value = selected_option.text
        return selected_value

    #-------------------------------------------------------------------------------------------------------------------

    tur_search = (By.XPATH, "(//option[@value=' TR'])[3]")

    def check_tur_country_dropdown_text(self):
        text = self.driver.find_element(*CreateAccount.tur_search).text
        return text

    def input_test_001_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*CreateAccount.password).send_keys(i.test_001_password)
        sleep(5)


    def agree_to_terms_of_use(self):
        self.driver.find_element(*CreateAccount.termsofuse).click()

    def click_submit(self):
        self.driver.find_element(*CreateAccount.submit).click()
        sleep(15)

    def input_test_001_confirm_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*CreateAccount.confirmpassword).send_keys(i.test_001_password)


    def create_a_new_account(self):
        self.input_test_001_password()
        self.input_test_001_confirm_password()
        self.agree_to_terms_of_use()
        self.click_submit()




