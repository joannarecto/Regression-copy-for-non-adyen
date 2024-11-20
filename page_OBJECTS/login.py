from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by  import By
from datetime                      import datetime
from time                          import sleep
import random

from page_OBJECTS.data import Data

class Login:

    def __init__(self, driver):
        self.driver = driver

    password = (By.XPATH, "(//*[contains(@id,'gigya-password')])[1]")

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

    def input_test_007_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.test_007_password)
        sleep(5)

    def input_test_008_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.test_008_password)
        sleep(5)

    def input_test_009_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.test_009_password)
        sleep(5)

    def input_test_010_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.test_010_password)
        sleep(5)

    def input_test_011_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.test_011_password)
        sleep(5)

    def input_test_012_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.test_012_password)
        sleep(5)

    def input_test_013_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.test_013_password)
        sleep(5)

    def input_test_014_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.test_014_password)
        sleep(5)

    def input_no_state_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.no_state_password)
        sleep(5)

    def input_confirmation_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.confirmation_password)
        sleep(5)

    def input_confirmation_password2(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.password).send_keys(i.confirmation_password2)
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

    cart = (By.XPATH, "//*[contains(@class,'cart')]")

    def click_cart(self):
        self.driver.find_element(*Login.cart).click()
        sleep(25)

    #-------------------------------------------------------------------------------------------------------------------

    emailaddress = (By.XPATH, "//*[contains(@id,'gigya-loginID')]")

    def input_e_test_001_emailaddress(self):

        i = Data(self.driver)

        return self.driver.find_element(*Login.emailaddress).send_keys(i.e_test_001_emailaddress)

    def input_e_test_002_emailaddress(self):

        i = Data(self.driver)

        return self.driver.find_element(*Login.emailaddress).send_keys(i.e_test_002_emailaddress)

    def input_e_test_003_emailaddress(self):

        i = Data(self.driver)

        return self.driver.find_element(*Login.emailaddress).send_keys(i.e_test_003_emailaddress)

    def input_e_test_004_emailaddress(self):

        i = Data(self.driver)

        return self.driver.find_element(*Login.emailaddress).send_keys(i.e_test_004_emailaddress)

    def input_e_test_005_emailaddress(self):

        i = Data(self.driver)

        return self.driver.find_element(*Login.emailaddress).send_keys(i.e_test_005_emailaddress)

    def input_e_test_006_emailaddress(self):

        i = Data(self.driver)

        return self.driver.find_element(*Login.emailaddress).send_keys(i.e_test_006_emailaddress)

    def input_e_test_007_emailaddress(self):

        i = Data(self.driver)

        return self.driver.find_element(*Login.emailaddress).send_keys(i.e_test_007_emailaddress)

    def input_e_test_008_emailaddress(self):

        i = Data(self.driver)

        return self.driver.find_element(*Login.emailaddress).send_keys(i.e_test_008_emailaddress)

    def input_e_test_009_emailaddress(self):

        i = Data(self.driver)

        return self.driver.find_element(*Login.emailaddress).send_keys(i.e_test_009_emailaddress)

    def input_e_test_010_emailaddress(self):

        i = Data(self.driver)

        return self.driver.find_element(*Login.emailaddress).send_keys(i.e_test_010_emailaddress)

    def input_e_test_011_emailaddress(self):

        i = Data(self.driver)

        return self.driver.find_element(*Login.emailaddress).send_keys(i.e_test_011_emailaddress)

    def input_e_test_012_emailaddress(self):

        i = Data(self.driver)

        return self.driver.find_element(*Login.emailaddress).send_keys(i.e_test_012_emailaddress)

    def input_e_test_013_emailaddress(self):

        i = Data(self.driver)

        return self.driver.find_element(*Login.emailaddress).send_keys(i.e_test_013_emailaddress)

    def input_e_test_014_emailaddress(self):

        i = Data(self.driver)

        return self.driver.find_element(*Login.emailaddress).send_keys(i.e_test_014_emailaddress)

    def login_existing_user_001(self):
        self.input_e_test_001_emailaddress()
        self.input_test_001_password()
        self.click_signin()

    def login_existing_user_002(self):
        self.input_e_test_002_emailaddress()
        self.input_test_002_password()
        self.click_signin()

    def login_existing_user_003(self):
        self.input_e_test_003_emailaddress()
        self.input_test_003_password()
        self.click_signin()

    def login_existing_user_004(self):
        self.input_e_test_004_emailaddress()
        self.input_test_004_password()
        self.click_signin()

    def login_existing_user_005(self):
        self.input_e_test_005_emailaddress()
        self.input_test_005_password()
        self.click_signin()

    def login_existing_user_006(self):
        self.input_e_test_006_emailaddress()
        self.input_test_006_password()
        self.click_signin()

    def login_existing_user_007(self):
        self.input_e_test_007_emailaddress()
        self.input_test_007_password()
        self.click_signin()

    def login_existing_user_008(self):
        self.input_e_test_008_emailaddress()
        self.input_test_008_password()
        self.click_signin()

    def login_existing_user_009(self):
        self.input_e_test_009_emailaddress()
        self.input_test_009_password()
        self.click_signin()

    def login_existing_user_010(self):
        self.input_e_test_010_emailaddress()
        self.input_test_010_password()
        self.click_signin()

    def login_existing_user_011(self):
        self.input_e_test_011_emailaddress()
        self.input_test_011_password()
        self.click_signin()

    def login_existing_user_012(self):
        self.input_e_test_012_emailaddress()
        self.input_test_012_password()
        self.click_signin()

    def login_existing_user_013(self):
        self.input_e_test_013_emailaddress()
        self.input_test_013_password()
        self.click_signin()

    def login_existing_user_014(self):
        self.input_e_test_014_emailaddress()
        self.input_test_014_password()
        self.click_signin()

# -------------------------------------------------------------------------------------------------------------------
# Currency: Email (E)

    def input_e_aud_emailaddress(self):
        i = Data(self.driver)

        return self.driver.find_element(*Login.emailaddress).send_keys(i.e_aud_emailaddress)
        sleep(5)

    def input_e_cad_emailaddress(self):
        i = Data(self.driver)

        return self.driver.find_element(*Login.emailaddress).send_keys(i.e_cad_emailaddress)
        sleep(5)

    def input_e_eur_emailaddress(self):
        i = Data(self.driver)

        return self.driver.find_element(*Login.emailaddress).send_keys(i.e_eur_emailaddress)
        sleep(5)

    def input_e_eur_c_emailaddress(self):
        i = Data(self.driver)

        return self.driver.find_element(*Login.emailaddress).send_keys(i.e_eur_c_emailaddress)
        sleep(5)

    def input_e_eur_i_emailaddress(self):
        i = Data(self.driver)

        return self.driver.find_element(*Login.emailaddress).send_keys(i.e_eur_i_emailaddress)
        sleep(5)

    def input_e_gbp_emailaddress(self):
        i = Data(self.driver)

        return self.driver.find_element(*Login.emailaddress).send_keys(i.e_gbp_emailaddress)
        sleep(5)

    def input_e_nzd_emailaddress(self):
        i = Data(self.driver)

        return self.driver.find_element(*Login.emailaddress).send_keys(i.e_nzd_emailaddress)
        sleep(5)

    def input_e_usd_emailaddress(self):
        i = Data(self.driver)

        return self.driver.find_element(*Login.emailaddress).send_keys(i.e_usd_emailaddress)
        sleep(5)

    def input_e_usd_e_emailaddress(self):
        i = Data(self.driver)

        return self.driver.find_element(*Login.emailaddress).send_keys(i.e_usd_e_emailaddress)
        sleep(5)

    def input_e_usd_n_emailaddress(self):
        i = Data(self.driver)

        return self.driver.find_element(*Login.emailaddress).send_keys(i.e_usd_n_emailaddress)
        sleep(5)

    def input_confirmation_emailaddress(self):
        i = Data(self.driver)

        return self.driver.find_element(*Login.emailaddress).send_keys(i.confirmation_emailaddress)
        sleep(5)

    def login_existing_user_aud(self):
        self.input_e_aud_emailaddress()
        self.input_test_014_password()
        self.click_signin()

    def login_existing_user_cad(self):
        self.input_e_cad_emailaddress()
        self.input_test_014_password()
        self.click_signin()

    def login_existing_user_eur_c(self):
        self.input_e_eur_c_emailaddress()
        self.input_test_014_password()
        self.click_signin()

    def login_existing_user_eur_i(self):
        self.input_e_eur_i_emailaddress()
        self.input_test_014_password()
        self.click_signin()

    def login_existing_user_eur(self):
        self.input_e_eur_emailaddress()
        self.input_test_014_password()
        self.click_signin()

    def login_existing_user_gbp(self):
        self.input_e_gbp_emailaddress()
        self.input_test_014_password()
        self.click_signin()

    def login_existing_user_nzd(self):
        self.input_e_nzd_emailaddress()
        self.input_test_014_password()
        self.click_signin()

    def login_existing_user_usd_e(self):
        self.input_e_usd_e_emailaddress()
        self.input_test_014_password()
        self.click_signin()

    def login_existing_user_usd_n(self):
        self.input_e_usd_n_emailaddress()
        self.input_test_014_password()
        self.click_signin()

    def login_existing_user_usd(self):
        self.input_e_usd_emailaddress()
        self.input_test_014_password()
        self.click_signin()
    #-------------------------------------------------------------------------------------------------------------------

    createaccount   = (By.XPATH, "//*[contains(@id,'create-account')]")

    firstname       = (By.XPATH, "(//*[contains(@id,'gigya-textbox')])[1]")

    lastname        = (By.XPATH, "(//*[contains(@id,'gigya-textbox')])[2]")

    confirmpassword = (By.XPATH, "(//*[contains(@id,'gigya-password')])[2]")

    dropdown        = (By.XPATH, "//*[contains(@id,'gigya-dropdown')]")

    termsofuse      = (By.XPATH, "//*[contains(@id,'gigya-checkbox')]")

    submit          = (By.XPATH, "//*[contains(@id,'submit-btn')]")

    def click_createaccount(self):
        self.driver.find_element(*Login.createaccount).click()
        sleep(10)

    def input_firstname(self):

        i = Data(self.driver)

        return self.driver.find_element(*Login.firstname).send_keys(i.test_firstname)

    def input_lastname(self):

        i = Data(self.driver)

        return self.driver.find_element(*Login.lastname).send_keys(i.test_lastname)

    a = datetime.now()

    current_time = a.strftime("%H:%M:%S")
    current_date = a.strftime("%d/%m/%Y")

    b = current_time + current_date

    c = b.replace(":","")
    d = c.replace("/","")

    e = str(random.uniform(1,100))

    randomemailaddress = d + e + "@mailsac.com"

    def input_random_emailaddress(self):

        return self.driver.find_element(*Login.emailaddress).send_keys(Login.randomemailaddress)

    def input_test_001_confirm_password(self):

        i = Data (self.driver)

        return self.driver.find_element(*Login.confirmpassword).send_keys(i.test_001_password)

    def select_dropdown(self):
        return self.driver.find_element(*Login.dropdown)

    def select_country(self):

        i = Data(self.driver)

        a = Select(self.select_dropdown())
        a.select_by_visible_text(i.test_country)

    def agree_to_terms_of_use(self):
        self.driver.find_element(*Login.termsofuse).click()

    def click_submit(self):
        self.driver.find_element(*Login.submit).click()
        sleep(15)

    def create_a_new_account(self):
        self.click_createaccount()
        self.input_firstname()
        self.input_lastname()
        self.input_random_emailaddress()
        self.input_test_001_password()
        self.input_test_001_confirm_password()
        self.select_country()
        self.agree_to_terms_of_use()
        self.click_submit()

    #-------------------------------------------------------------------------------------------------------------------
