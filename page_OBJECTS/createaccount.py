from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CreateAccount:

    def __init__(self, driver):
        self.driver = driver

    firstname           = (By.XPATH, "(//input[@name='profile.firstName'])[3]")

    lastname            = (By.XPATH, "(//input[@name='profile.lastName'])[3]")

    email               = (By.XPATH, "(//input[@name='email'])[4]")

    password            = (By.XPATH, "(//input[@name='password'])[5]")

    password2           = (By.XPATH, "(//input[@name='passwordRetype'])[5]")

    country             = (By.XPATH, "(//select[@name='profile.country'])[3]")

    agree               = (By.XPATH, "(//*[contains(@class,'fd-checkbox')])[3]")


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