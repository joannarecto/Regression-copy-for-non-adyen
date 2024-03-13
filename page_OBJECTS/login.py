from selenium.webdriver.common.by import By
from time import sleep

from page_OBJECTS.data import Data

class Login:

    def __init__(self, driver):
        self.driver = driver

    password = (By.XPATH, "//*[contains(@id,'gigya-password')]")

    def input_bra_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.bra_password)
        sleep(5)

    def input_can_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.can_password)
        sleep(5)

    def input_che_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.che_password)
        sleep(5)

    def input_esp_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.esp_password)
        sleep(5)

    def input_gbr_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.gbr_password)
        sleep(5)

    def input_ind_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.ind_password)
        sleep(5)

    def input_ita_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.ita_password)
        sleep(5)

    def input_mex_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.mex_password)
        sleep(5)

    def input_nld_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.nld_password)
        sleep(5)

    def input_phl_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.phl_password)
        sleep(5)

    def input_pol_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.pol_password)
        sleep(5)

    def input_prt_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.prt_password)
        sleep(5)

    def input_rus_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.rus_password)
        sleep(5)

    def input_usa_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.usa_password)
        sleep(5)

    #-------------------------------------------------------------------------------------------------------------------

    signin = (By.XPATH, "//*[@value='Sign in']")

    def click_signin(self):
        self.driver.find_element(*Login.signin).click()
        sleep(25)
