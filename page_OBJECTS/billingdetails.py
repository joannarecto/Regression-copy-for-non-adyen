from selenium.webdriver.common.by import By
from time import sleep

from page_OBJECTS.data import Data

class BillingDetails:

    def __init__(self, driver):
        self.driver = driver

    firstname           = (By.XPATH, "//*[@id='first_name']")

    lastname            = (By.XPATH, "//*[@id='last_name']")

    country             = (By.XPATH, "//*[@id='country']")

    billingaddressline1 = (By.XPATH, "//*[@id='street_address']")

    billingaddressline2 = (By.XPATH, "//*[@id='street_address_1']")

    city                = (By.XPATH, "//*[@id='city']")

    state               = (By.XPATH, "//*[@id='state']")

    postcode            = (By.XPATH, "//*[@id='postcode']")

    bra                 = (By.XPATH, "//a[text()='Brazil']")

    can                 = (By.XPATH, "//a[text()='Canada']")

    ind                 = (By.XPATH, "//a[text()='India']")

    ita                 = (By.XPATH, "//a[text()='Italy']")

    mex                 = (By.XPATH, "//a[text()='Mexico']")

    nld                 = (By.XPATH, "//a[text()='Netherlands']")

    phl                 = (By.XPATH, "//a[text()='Philippines']")

    pol                 = (By.XPATH, "//a[text()='Poland']")

    prt                 = (By.XPATH, "//a[text()='Portugal']")

    rus                 = (By.XPATH, "//a[text()='Russian Federation']")

    esp                 = (By.XPATH, "//a[text()='Spain']")

    che                 = (By.XPATH, "//a[text()='Switzerland']")

    gbr                 = (By.XPATH, "//a[text()='United Kingdom']")

    usa                 = (By.XPATH, "//a[text()='United States']")

    gotorevieworder     = (By.XPATH, "//*[contains(text(),'Review order')]")

    def input_bra_firstname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.firstname).send_keys(i.bra_firstname)
        sleep(5)

    def input_can_firstname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.firstname).send_keys(i.can_firstname)
        sleep(5)

    def input_che_firstname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.firstname).send_keys(i.che_firstname)
        sleep(5)

    def input_esp_firstname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.firstname).send_keys(i.esp_firstname)
        sleep(5)

    def input_gbr_firstname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.firstname).send_keys(i.gbr_firstname)
        sleep(5)

    def input_ind_firstname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.firstname).send_keys(i.ind_firstname)
        sleep(5)

    def input_ita_firstname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.firstname).send_keys(i.ita_firstname)
        sleep(5)

    def input_mex_firstname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.firstname).send_keys(i.mex_firstname)
        sleep(5)

    def input_nld_firstname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.firstname).send_keys(i.nld_firstname)
        sleep(5)

    def input_phl_firstname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.firstname).send_keys(i.phl_firstname)
        sleep(5)

    def input_pol_firstname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.firstname).send_keys(i.pol_firstname)
        sleep(5)

    def input_prt_firstname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.firstname).send_keys(i.prt_firstname)
        sleep(5)

    def input_rus_firstname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.firstname).send_keys(i.rus_firstname)
        sleep(5)

    def input_usa_firstname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.firstname).send_keys(i.usa_firstname)
        sleep(5)

    #-------------------------------------------------------------------------------------------------------------------

    def input_bra_lastname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.lastname).send_keys(i.bra_lastname)
        sleep(5)

    def input_can_lastname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.lastname).send_keys(i.can_lastname)
        sleep(5)

    def input_che_lastname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.lastname).send_keys(i.che_lastname)
        sleep(5)

    def input_esp_lastname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.lastname).send_keys(i.esp_lastname)
        sleep(5)

    def input_gbr_lastname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.lastname).send_keys(i.gbr_lastname)
        sleep(5)

    def input_ind_lastname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.lastname).send_keys(i.ind_lastname)
        sleep(5)

    def input_ita_lastname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.lastname).send_keys(i.ita_lastname)
        sleep(5)

    def input_mex_lastname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.lastname).send_keys(i.mex_lastname)
        sleep(5)

    def input_nld_lastname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.lastname).send_keys(i.nld_lastname)
        sleep(5)

    def input_phl_lastname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.lastname).send_keys(i.phl_lastname)
        sleep(5)

    def input_pol_lastname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.lastname).send_keys(i.pol_lastname)
        sleep(5)

    def input_prt_lastname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.lastname).send_keys(i.prt_lastname)
        sleep(5)

    def input_rus_lastname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.lastname).send_keys(i.rus_lastname)
        sleep(5)

    def input_usa_lastname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.lastname).send_keys(i.usa_lastname)
        sleep(5)

    #-------------------------------------------------------------------------------------------------------------------

    def input_bra_country(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.country).send_keys(i.bra_country)
        sleep(5)

    def input_can_country(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.country).send_keys(i.can_country)
        sleep(5)

    def input_che_country(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.country).send_keys(i.che_country)
        sleep(5)

    def input_esp_country(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.country).send_keys(i.esp_country)
        sleep(5)

    def input_gbr_country(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.country).send_keys(i.gbr_country)
        sleep(5)

    def input_ind_country(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.country).send_keys(i.ind_country)
        sleep(5)

    def input_ita_country(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.country).send_keys(i.ita_country)
        sleep(5)

    def input_mex_country(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.country).send_keys(i.mex_country)
        sleep(5)

    def input_nld_country(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.country).send_keys(i.nld_country)
        sleep(5)

    def input_phl_country(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.country).send_keys(i.phl_country)
        sleep(5)

    def input_pol_country(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.country).send_keys(i.pol_country)
        sleep(5)

    def input_prt_country(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.country).send_keys(i.prt_country)
        sleep(5)

    def input_rus_country(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.country).send_keys(i.rus_country)
        sleep(5)

    def input_usa_country(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.country).send_keys(i.usa_country)
        sleep(5)

    #-------------------------------------------------------------------------------------------------------------------
    def input_bra_billingaddressline1(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline1).send_keys(i.bra_billingaddressline1)
        sleep(5)

    def input_can_billingaddressline1(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline1).send_keys(i.can_billingaddressline1)
        sleep(5)

    def input_che_billingaddressline1(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline1).send_keys(i.che_billingaddressline1)
        sleep(5)

    def input_esp_billingaddressline1(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline1).send_keys(i.esp_billingaddressline1)
        sleep(5)

    def input_gbr_billingaddressline1(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline1).send_keys(i.gbr_billingaddressline1)
        sleep(5)

    def input_ind_billingaddressline1(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline1).send_keys(i.ind_billingaddressline1)
        sleep(5)

    def input_ita_billingaddressline1(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline1).send_keys(i.ita_billingaddressline1)
        sleep(5)

    def input_mex_billingaddressline1(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline1).send_keys(i.mex_billingaddressline1)
        sleep(5)

    def input_nld_billingaddressline1(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline1).send_keys(i.nld_billingaddressline1)
        sleep(5)

    def input_phl_billingaddressline1(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline1).send_keys(i.phl_billingaddressline1)
        sleep(5)

    def input_pol_billingaddressline1(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline1).send_keys(i.pol_billingaddressline1)
        sleep(5)

    def input_prt_billingaddressline1(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline1).send_keys(i.prt_billingaddressline1)
        sleep(5)

    def input_rus_billingaddressline1(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline1).send_keys(i.rus_billingaddressline1)
        sleep(5)

    def input_usa_billingaddressline1(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline1).send_keys(i.usa_billingaddressline1)
        sleep(5)

    #-------------------------------------------------------------------------------------------------------------------
    def input_bra_billingaddressline2(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline2).send_keys(i.bra_billingaddressline2)
        sleep(5)

    def input_can_billingaddressline2(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline2).send_keys(i.can_billingaddressline2)
        sleep(5)

    def input_che_billingaddressline2(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline2).send_keys(i.che_billingaddressline2)
        sleep(5)

    def input_esp_billingaddressline2(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline2).send_keys(i.esp_billingaddressline2)
        sleep(5)

    def input_gbr_billingaddressline2(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline2).send_keys(i.gbr_billingaddressline2)
        sleep(5)

    def input_ind_billingaddressline2(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline2).send_keys(i.ind_billingaddressline2)
        sleep(5)

    def input_ita_billingaddressline2(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline2).send_keys(i.ita_billingaddressline2)
        sleep(5)

    def input_mex_billingaddressline2(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline2).send_keys(i.mex_billingaddressline2)
        sleep(5)

    def input_nld_billingaddressline2(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline2).send_keys(i.nld_billingaddressline2)
        sleep(5)

    def input_phl_billingaddressline2(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline2).send_keys(i.phl_billingaddressline2)
        sleep(5)

    def input_pol_billingaddressline2(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline2).send_keys(i.pol_billingaddressline2)
        sleep(5)

    def input_prt_billingaddressline2(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline2).send_keys(i.prt_billingaddressline2)
        sleep(5)

    def input_rus_billingaddressline2(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline2).send_keys(i.rus_billingaddressline2)
        sleep(5)

    def input_usa_billingaddressline2(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline2).send_keys(i.usa_billingaddressline2)
        sleep(5)

    #-------------------------------------------------------------------------------------------------------------------
    def input_bra_city(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.city).send_keys(i.bra_city)
        sleep(5)

    def input_can_city(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.city).send_keys(i.can_city)
        sleep(5)

    def input_che_city(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.city).send_keys(i.che_city)
        sleep(5)

    def input_esp_city(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.city).send_keys(i.esp_city)
        sleep(5)

    def input_gbr_city(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.city).send_keys(i.gbr_city)
        sleep(5)

    def input_ind_city(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.city).send_keys(i.ind_city)
        sleep(5)

    def input_ita_city(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.city).send_keys(i.ita_city)
        sleep(5)

    def input_mex_city(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.city).send_keys(i.mex_city)
        sleep(5)

    def input_nld_city(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.city).send_keys(i.nld_city)
        sleep(5)

    def input_phl_city(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.city).send_keys(i.phl_city)
        sleep(5)

    def input_pol_city(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.city).send_keys(i.pol_city)
        sleep(5)

    def input_prt_city(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.city).send_keys(i.prt_city)
        sleep(5)

    def input_rus_city(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.city).send_keys(i.rus_city)
        sleep(5)

    def input_usa_city(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.city).send_keys(i.usa_city)
        sleep(5)

    #-------------------------------------------------------------------------------------------------------------------
    def input_bra_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.state).send_keys(i.bra_state)
        sleep(5)

    def input_can_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.state).send_keys(i.can_state)
        sleep(5)

    def input_che_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.state).send_keys(i.che_state)
        sleep(5)

    def input_esp_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.state).send_keys(i.esp_state)
        sleep(5)

    def input_gbr_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.state).send_keys(i.gbr_state)
        sleep(5)

    def input_ind_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.state).send_keys(i.ind_state)
        sleep(5)

    def input_ita_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.state).send_keys(i.ita_state)
        sleep(5)

    def input_mex_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.state).send_keys(i.mex_state)
        sleep(5)

    def input_nld_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.state).send_keys(i.nld_state)
        sleep(5)

    def input_phl_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.state).send_keys(i.phl_state)
        sleep(5)

    def input_pol_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.state).send_keys(i.pol_state)
        sleep(5)

    def input_prt_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.state).send_keys(i.prt_state)
        sleep(5)

    def input_rus_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.state).send_keys(i.rus_state)
        sleep(5)

    def input_usa_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.state).send_keys(i.usa_state)
        sleep(5)

    #-------------------------------------------------------------------------------------------------------------------
    def input_bra_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.postcode).send_keys(i.bra_postcode)
        sleep(5)

    def input_can_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.postcode).send_keys(i.can_postcode)
        sleep(5)

    def input_che_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.postcode).send_keys(i.che_postcode)
        sleep(5)

    def input_esp_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.postcode).send_keys(i.esp_postcode)
        sleep(5)

    def input_gbr_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.postcode).send_keys(i.gbr_postcode)
        sleep(5)

    def input_ind_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.postcode).send_keys(i.ind_postcode)
        sleep(5)

    def input_ita_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.postcode).send_keys(i.ita_postcode)
        sleep(5)

    def input_mex_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.postcode).send_keys(i.mex_postcode)
        sleep(5)

    def input_nld_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.postcode).send_keys(i.nld_postcode)
        sleep(5)

    def input_phl_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.postcode).send_keys(i.phl_postcode)
        sleep(5)

    def input_pol_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.postcode).send_keys(i.pol_postcode)
        sleep(5)

    def input_prt_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.postcode).send_keys(i.prt_postcode)
        sleep(5)

    def input_rus_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.postcode).send_keys(i.rus_postcode)
        sleep(5)

    def input_usa_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.postcode).send_keys(i.usa_postcode)
        sleep(5)

    #-------------------------------------------------------------------------------------------------------------------
    def select_bra(self):
        self.driver.find_element(*BillingDetails.bra).click()
        sleep(10)

    def select_can(self):
        self.driver.find_element(*BillingDetails.can).click()
        sleep(10)

    def select_che(self):
        self.driver.find_element(*BillingDetails.che).click()
        sleep(10)

    def select_esp(self):
        self.driver.find_element(*BillingDetails.esp).click()
        sleep(10)

    def select_gbr(self):
        self.driver.find_element(*BillingDetails.gbr).click()
        sleep(10)

    def select_ind(self):
        self.driver.find_element(*BillingDetails.ind).click()
        sleep(10)

    def select_ita(self):
        self.driver.find_element(*BillingDetails.ita).click()
        sleep(10)

    def select_mex(self):
        self.driver.find_element(*BillingDetails.mex).click()
        sleep(10)

    def select_nld(self):
        self.driver.find_element(*BillingDetails.nld).click()
        sleep(10)

    def select_phl(self):
        self.driver.find_element(*BillingDetails.phl).click()
        sleep(10)

    def select_pol(self):
        self.driver.find_element(*BillingDetails.pol).click()
        sleep(10)

    def select_prt(self):
        self.driver.find_element(*BillingDetails.prt).click()
        sleep(10)

    def select_rus(self):
        self.driver.find_element(*BillingDetails.rus).click()
        sleep(10)

    def select_usa(self):
        self.driver.find_element(*BillingDetails.usa).click()
        sleep(10)

    #-------------------------------------------------------------------------------------------------------------------
    def click_gotorevieworder(self):
        self.driver.find_element(*BillingDetails.gotorevieworder).click()
        sleep(25)

    def input_bra_billing_details_and_proceed(self):
        self.input_bra_firstname()
        self.input_bra_lastname()
        self.input_bra_country()
        self.select_bra()
        self.input_bra_billingaddressline1()
        self.input_bra_billingaddressline2()
        self.input_bra_city()
        self.input_bra_state()
        self.input_bra_postcode()
        self.click_gotorevieworder()

    def input_can_billing_details_and_proceed(self):
        self.input_can_firstname()
        self.input_can_lastname()
        self.input_can_country()
        self.select_can()
        self.input_can_billingaddressline1()
        self.input_can_billingaddressline2()
        self.input_can_city()
        self.input_can_state()
        self.input_can_postcode()
        self.click_gotorevieworder()

    def input_che_billing_details_and_proceed(self):
        self.input_che_firstname()
        self.input_che_lastname()
        self.input_che_country()
        self.select_che()
        self.input_che_billingaddressline1()
        self.input_che_billingaddressline2()
        self.input_che_city()
        self.input_che_state()
        self.input_che_postcode()
        self.click_gotorevieworder()

    def input_esp_billing_details_and_proceed(self):
        self.input_esp_firstname()
        self.input_esp_lastname()
        self.input_esp_country()
        self.select_esp()
        self.input_esp_billingaddressline1()
        self.input_esp_billingaddressline2()
        self.input_esp_city()
        self.input_esp_state()
        self.input_esp_postcode()
        self.click_gotorevieworder()

    def input_gbr_billing_details_and_proceed(self):
        self.input_gbr_firstname()
        self.input_gbr_lastname()
        self.input_gbr_country()
        self.select_gbr()
        self.input_gbr_billingaddressline1()
        self.input_gbr_billingaddressline2()
        self.input_gbr_city()
        self.input_gbr_state()
        self.input_gbr_postcode()
        self.click_gotorevieworder()

    def input_ind_billing_details_and_proceed(self):
        self.input_ind_firstname()
        self.input_ind_lastname()
        self.input_ind_country()
        self.select_ind()
        self.input_ind_billingaddressline1()
        self.input_ind_billingaddressline2()
        self.input_ind_city()
        self.input_ind_state()
        self.input_ind_postcode()
        self.click_gotorevieworder()

    def input_ita_billing_details_and_proceed(self):
        self.input_ita_firstname()
        self.input_ita_lastname()
        self.input_ita_country()
        self.select_ita()
        self.input_ita_billingaddressline1()
        self.input_ita_billingaddressline2()
        self.input_ita_city()
        self.input_ita_state()
        self.input_ita_postcode()
        self.click_gotorevieworder()

    def input_mex_billing_details_and_proceed(self):
        self.input_mex_firstname()
        self.input_mex_lastname()
        self.input_mex_country()
        self.select_mex()
        self.input_mex_billingaddressline1()
        self.input_mex_billingaddressline2()
        self.input_mex_city()
        self.input_mex_state()
        self.input_mex_postcode()
        self.click_gotorevieworder()

    def input_nld_billing_details_and_proceed(self):
        self.input_nld_firstname()
        self.input_nld_lastname()
        self.input_nld_country()
        self.select_nld()
        self.input_nld_billingaddressline1()
        self.input_nld_billingaddressline2()
        self.input_nld_city()
        self.input_nld_state()
        self.input_nld_postcode()
        self.click_gotorevieworder()

    def input_phl_billing_details_and_proceed(self):
        self.input_phl_firstname()
        self.input_phl_lastname()
        self.input_phl_country()
        self.select_phl()
        self.input_phl_billingaddressline1()
        self.input_phl_billingaddressline2()
        self.input_phl_city()
        self.input_phl_state()
        self.input_phl_postcode()
        self.click_gotorevieworder()

    def input_pol_billing_details_and_proceed(self):
        self.input_pol_firstname()
        self.input_pol_lastname()
        self.input_pol_country()
        self.select_pol()
        self.input_pol_billingaddressline1()
        self.input_pol_billingaddressline2()
        self.input_pol_city()
        self.input_pol_state()
        self.input_pol_postcode()
        self.click_gotorevieworder()

    def input_prt_billing_details_and_proceed(self):
        self.input_prt_firstname()
        self.input_prt_lastname()
        self.input_prt_country()
        self.select_prt()
        self.input_prt_billingaddressline1()
        self.input_prt_billingaddressline2()
        self.input_prt_city()
        self.input_prt_state()
        self.input_prt_postcode()
        self.click_gotorevieworder()

    def input_rus_billing_details_and_proceed(self):
        self.input_rus_firstname()
        self.input_rus_lastname()
        self.input_rus_country()
        self.select_rus()
        self.input_rus_billingaddressline1()
        self.input_rus_billingaddressline2()
        self.input_rus_city()
        self.input_rus_state()
        self.input_rus_postcode()
        self.click_gotorevieworder()

    def input_usa_billing_details_and_proceed(self):
        self.input_usa_firstname()
        self.input_usa_lastname()
        self.input_usa_country()
        self.select_usa()
        self.input_usa_billingaddressline1()
        self.input_usa_billingaddressline2()
        self.input_usa_city()
        self.input_usa_state()
        self.input_usa_postcode()
        self.click_gotorevieworder()

