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


    def input_tur_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.tur_password)
        sleep(5)

    def input_aud_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.aud_password)
        sleep(5)

    def input_cad_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.cad_password)
        sleep(5)

    def input_eur_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.eur_password)
        sleep(5)

    def input_eur_c_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.eur_c_password)
        sleep(5)

    def input_eur_i_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.eur_i_password)
        sleep(5)

    def input_gbp_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.gbp_password)
        sleep(5)

    def input_nzd_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.nzd_password)
        sleep(5)

    def input_usd_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.usd_password)
        sleep(5)

    def input_usd_e_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.usd_e_password)
        sleep(5)

    def input_usd_n_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.usd_n_password)
        sleep(5)

    def input_test_001_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.test_001_password)
        sleep(5)

    def input_test_002_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.test_002_password)
        sleep(5)

    def input_test_003_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.test_003_password)
        sleep(5)

    def input_test_004_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.test_004_password)
        sleep(5)

    def input_test_005_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.test_005_password)
        sleep(5)

    def input_test_006_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.test_006_password)
        sleep(5)

    #-------------------------------------------------------------------------------------------------------------------

    signin = (By.XPATH, "//*[@value='Sign in']")

    def click_signin(self):
        self.driver.find_element(*Login.signin).click()
        sleep(25)

    #-------------------------------------------------------------------------------------------------------------------

    legal         = (By.XPATH, "//*[text()=' Legal ']")

    privacynotice = (By.XPATH, "//*[text()=' Privacy Notice ']")

    accessibilty  = (By.XPATH, "//*[text()=' Accessibility ']")

    help          = (By.XPATH, "//*[text()=' Help ']")

    def click_legal(self):
        return self.driver.find_element(*Login.legal).click()

    def click_privacynotice(self):
        self.driver.find_element(*Login.privacynotice).click()

    def click_accessibility(self):
        self.driver.find_element(*Login.accessibilty).click()

    def click_help(self):
        self.driver.find_element(*Login.help).click()

    def verify_footers_are_accessible(self):

        i = Data(self.driver)

        main_window = self.driver.window_handles[0]

        self.click_legal()
        sleep(25)
        legal_window = self.driver.window_handles[1]
        self.driver.switch_to.window(legal_window)
        assert i.legal_title == self.driver.title
        self.driver.close()

        self.driver.switch_to.window(main_window)

        self.click_privacynotice()
        sleep(25)
        privacynotice_window = self.driver.window_handles[1]
        self.driver.switch_to.window(privacynotice_window)
        assert i.privacynotice_title == self.driver.title
        self.driver.close()

        self.driver.switch_to.window(main_window)

        self.click_accessibility()
        sleep(25)
        accessibility_window = self.driver.window_handles[1]
        self.driver.switch_to.window(accessibility_window)
        assert i.accessibility_title == self.driver.title
        self.driver.close()

        self.driver.switch_to.window(main_window)

        self.click_help()
        sleep(25)
        help_window = self.driver.window_handles[1]
        self.driver.switch_to.window(help_window)
        assert i.help_title == self.driver.title
        self.driver.close()

        self.driver.switch_to.window(main_window)

    #-------------------------------------------------------------------------------------------------------------------
