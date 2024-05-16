from selenium.webdriver.common.by import By
from time import sleep

from page_OBJECTS.data import Data

class BillingDetails:

    def __init__(self, driver):
        self.driver = driver

    firstname           = (By.XPATH, "//*[@id='first_name']")

    lastname            = (By.XPATH, "//*[@id='last_name']")

    country             = (By.XPATH, "//*[@id='country']")

    billingaddressline1 = (By.XPATH, "//*[@id='street_1']")

    billingaddressline2 = (By.XPATH, "//*[@id='street_2']")

    city                = (By.XPATH, "//*[@id='city']")

    state               = (By.XPATH, "//*[@id='state']")

    postcode            = (By.XPATH, "//*[@id='postcode']")


    # Select countries for target market country test

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

    tur                 = (By.XPATH, "//a[text()='Türkiye']")


    #Button to Review order

    gotorevieworder     = (By.XPATH, "//*[contains(text(),'Review order')]")



    #select countires for currency test
    aud                 = (By.XPATH, "//a[text()='Australia']")

    cad                 = (By.XPATH, "//a[text()='Canada']")

    eur                 = (By.XPATH, "//a[text()='Germany']")

    eur_c                 = (By.XPATH, "//a[text()='Spain']")

    eur_i                 = (By.XPATH, "//a[text()='Italy']")

    gbp                 = (By.XPATH, "//a[text()='United Kingdom']")

    nzd                 = (By.XPATH, "//a[text()='New Zealand']")

    usd                 = (By.XPATH, "//a[text()='United States']")


#------------------------------------------------ Countries
#Countries: Firstname

    def input_bra_firstname(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.firstname).send_keys(i.bra_firstname)
        sleep(2)

    def input_can_firstname(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.firstname).send_keys(i.can_firstname)
        sleep(2)

    def input_che_firstname(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.firstname).send_keys(i.che_firstname)
        sleep(2)

    def input_esp_firstname(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.firstname).send_keys(i.esp_firstname)
        sleep(2)

    def input_gbr_firstname(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.firstname).send_keys(i.gbr_firstname)
        sleep(2)

    def input_ind_firstname(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.firstname).send_keys(i.ind_firstname)
        sleep(2)

    def input_ita_firstname(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.firstname).send_keys(i.ita_firstname)
        sleep(2)

    def input_mex_firstname(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.firstname).send_keys(i.mex_firstname)
        sleep(2)

    def input_nld_firstname(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.firstname).send_keys(i.nld_firstname)
        sleep(2)

    def input_phl_firstname(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.firstname).send_keys(i.phl_firstname)
        sleep(2)

    def input_pol_firstname(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.firstname).send_keys(i.pol_firstname)
        sleep(2)

    def input_prt_firstname(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.firstname).send_keys(i.prt_firstname)
        sleep(2)

    def input_rus_firstname(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.firstname).send_keys(i.rus_firstname)
        sleep(2)

    def input_usa_firstname(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.firstname).send_keys(i.usa_firstname)
        sleep(2)

    #-------------------------------------------------------------------------------------------------------------------
    # Countries: Lastname

    def input_bra_lastname(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.lastname).send_keys(i.bra_lastname)
        sleep(2)

    def input_can_lastname(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.lastname).send_keys(i.can_lastname)
        sleep(2)

    def input_che_lastname(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.lastname).send_keys(i.che_lastname)
        sleep(2)

    def input_esp_lastname(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.lastname).send_keys(i.esp_lastname)
        sleep(2)

    def input_gbr_lastname(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.lastname).send_keys(i.gbr_lastname)
        sleep(2)

    def input_ind_lastname(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.lastname).send_keys(i.ind_lastname)
        sleep(2)

    def input_ita_lastname(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.lastname).send_keys(i.ita_lastname)
        sleep(2)

    def input_mex_lastname(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.lastname).send_keys(i.mex_lastname)
        sleep(2)

    def input_nld_lastname(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.lastname).send_keys(i.nld_lastname)
        sleep(2)

    def input_phl_lastname(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.lastname).send_keys(i.phl_lastname)
        sleep(2)

    def input_pol_lastname(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.lastname).send_keys(i.pol_lastname)
        sleep(2)

    def input_prt_lastname(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.lastname).send_keys(i.prt_lastname)
        sleep(2)

    def input_rus_lastname(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.lastname).send_keys(i.rus_lastname)
        sleep(2)

    def input_usa_lastname(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.lastname).send_keys(i.usa_lastname)
        sleep(2)

    #-------------------------------------------------------------------------------------------------------------------
    # Countries: Input Country


    def input_bra_country(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.country).send_keys(i.bra_country)
        sleep(2)

    def input_can_country(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.country).send_keys(i.can_country)
        sleep(2)

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
    # Countries: billing address line1

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
    # Countries: billing address line2


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
    # Countries: Input city

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
    # Countries: Input state


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
    # Countries: Input post code

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
    # Countries: Select country

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
# Click button - go to review order
    def click_gotorevieworder(self):
        self.driver.find_element(*BillingDetails.gotorevieworder).click()
        sleep(25)

# -------------------------------------------------------------------------------------------------------------------
# Countries: Proceed to billing details

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


#------------------------------------------------ Currency
#Currency: Firstname

    def input_aud_firstname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.firstname).send_keys(i.aud_firstname)
        sleep(5)


    def input_cad_firstname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.firstname).send_keys(i.cad_firstname)
        sleep(5)


    def input_eur_firstname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.firstname).send_keys(i.eur_firstname)
        sleep(5)


    def input_eur_c_firstname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.firstname).send_keys(i.eur_c_firstname)
        sleep(5)



    def input_eur_i_firstname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.firstname).send_keys(i.eur_i_firstname)
        sleep(5)


    def input_gbp_firstname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.firstname).send_keys(i.gbp_firstname)
        sleep(5)


    def input_nzd_firstname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.firstname).send_keys(i.nzd_firstname)
        sleep(5)


    def input_usd_firstname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.firstname).send_keys(i.usd_firstname)
        sleep(5)


    def input_usd_e_firstname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.firstname).send_keys(i.usd_e_firstname)
        sleep(5)


    def input_usd_n_firstname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.firstname).send_keys(i.usd_n_firstname)
        sleep(5)


    def input_test_firstname(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.firstname).send_keys(i.test_firstname)
        sleep(5)

#Currency: Lastname

    def input_aud_lastname(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.lastname).send_keys(i.aud_lastname)
        sleep(5)

    def input_cad_lastname(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.lastname).send_keys(i.cad_lastname)
        sleep(5)

    def input_eur_lastname(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.lastname).send_keys(i.eur_lastname)
        sleep(5)

    def input_eur_c_lastname(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.lastname).send_keys(i.eur_c_lastname)
        sleep(5)

    def input_eur_i_lastname(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.lastname).send_keys(i.eur_i_lastname)
        sleep(5)

    def input_gbp_lastname(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.lastname).send_keys(i.gbp_lastname)
        sleep(5)

    def input_nzd_lastname(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.lastname).send_keys(i.nzd_lastname)
        sleep(5)

    def input_usd_lastname(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.lastname).send_keys(i.usd_lastname)
        sleep(5)

    def input_usd_e_lastname(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.lastname).send_keys(i.usd_e_lastname)
        sleep(5)

    def input_usd_n_lastname(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.lastname).send_keys(i.usd_n_lastname)
        sleep(5)


    def input_test_lastname(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.lastname).send_keys(i.test_lastname)
        sleep(5)


# Currency: Input Country

    def input_aud_country(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.country).send_keys(i.aud_country)
        sleep(5)


    def input_cad_country(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.country).send_keys(i.cad_country)
        sleep(5)


    def input_eur_country(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.country).send_keys(i.eur_country)
        sleep(5)


    def input_eur_c_country(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.country).send_keys(i.eur_c_country)
        sleep(5)


    def input_eur_i_country(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.country).send_keys(i.eur_i_country)
        sleep(5)


    def input_gbp_country(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.country).send_keys(i.gbp_country)
        sleep(5)


    def input_nzd_country(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.country).send_keys(i.nzd_country)
        sleep(5)


    def input_usd_country(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.country).send_keys(i.usd_country)
        sleep(5)


    def input_usd_e_country(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.country).send_keys(i.usd_e_country)
        sleep(5)


    def input_usd_n_country(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.country).send_keys(i.usd_n_country)
        sleep(5)

    def input_test_country(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.country).send_keys(i.test_country)
        sleep(5)

    def input_tur_country(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.country).send_keys(i.tur_country)
        sleep(5)

    # Currency: Billing details 1

    def input_aud_billingaddressline1(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline1).send_keys(i.aud_billingaddressline1)
        sleep(5)


    def input_cad_billingaddressline1(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline1).send_keys(i.cad_billingaddressline1)
        sleep(5)


    def input_eur_billingaddressline1(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline1).send_keys(i.eur_billingaddressline1)
        sleep(5)


    def input_eur_c_billingaddressline1(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline1).send_keys(i.eur_c_billingaddressline1)
        sleep(5)


    def input_eur_i_billingaddressline1(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline1).send_keys(i.eur_i_billingaddressline1)
        sleep(5)



    def input_gbp_billingaddressline1(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline1).send_keys(i.gbp_billingaddressline1)
        sleep(5)



    def input_nzd_billingaddressline1(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline1).send_keys(i.nzd_billingaddressline1)
        sleep(5)


    def input_usd_billingaddressline1(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline1).send_keys(i.usd_billingaddressline1)
        sleep(5)


    def input_usd_e_billingaddressline1(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline1).send_keys(i.usd_e_billingaddressline1)
        sleep(5)


    def input_usd_n_billingaddressline1(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline1).send_keys(i.usd_n_billingaddressline1)
        sleep(5)


    def input_test_billingaddressline1(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline1).send_keys(i.test_billingaddressline1)
        sleep(5)


    def input_tur_billingaddressline1(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline1).send_keys(i.tur_billingaddressline1)
        sleep(5)


    # Currency: Billing details 2

    def input_aud_billingaddressline2(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline2).send_keys(i.aud_billingaddressline2)
        sleep(5)


    def input_cad_billingaddressline2(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline2).send_keys(i.cad_billingaddressline2)
        sleep(5)


    def input_eur_billingaddressline2(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline2).send_keys(i.eur_billingaddressline2)
        sleep(5)


    def input_eur_c_billingaddressline2(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline2).send_keys(i.eur_c_billingaddressline2)
        sleep(5)


    def input_eur_i_billingaddressline2(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline2).send_keys(i.eur_i_billingaddressline2)
        sleep(5)


    def input_gbp_billingaddressline2(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline2).send_keys(i.gbp_billingaddressline2)
        sleep(5)


    def input_nzd_billingaddressline2(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline2).send_keys(i.nzd_billingaddressline2)
        sleep(5)


    def input_usd_billingaddressline2(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline2).send_keys(i.usd_billingaddressline2)
        sleep(5)


    def input_usd_e_billingaddressline2(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline2).send_keys(i.usd_e_billingaddressline2)
        sleep(5)


    def input_usd_n_billingaddressline2(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline2).send_keys(i.usd_n_billingaddressline2)
        sleep(5)


    def input_test_billingaddressline2(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline2).send_keys(i.test_billingaddressline2)
        sleep(5)


    def input_tur_billingaddressline2(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.billingaddressline2).send_keys(i.tur_billingaddressline2)
        sleep(5)

    # Currency: Input city

    def input_aud_city(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.city).send_keys(i.aud_city)
        sleep(5)


    def input_cad_city(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.city).send_keys(i.cad_city)
        sleep(5)


    def input_eur_city(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.city).send_keys(i.eur_city)
        sleep(5)


    def input_eur_c_city(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.city).send_keys(i.eur_c_city)
        sleep(5)


    def input_eur_i_city(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.city).send_keys(i.eur_i_city)
        sleep(5)


    def input_gbp_city(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.city).send_keys(i.gbp_city)
        sleep(5)


    def input_nzd_city(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.city).send_keys(i.nzd_city)
        sleep(5)


    def input_usd_city(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.city).send_keys(i.usd_city)
        sleep(5)


    def input_usd_e_city(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.city).send_keys(i.usd_e_city)
        sleep(5)


    def input_usd_n_city(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.city).send_keys(i.usd_n_city)
        sleep(5)


    def input_test_city(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.city).send_keys(i.test_city)
        sleep(5)


    def input_tur_city(self):
        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.city).send_keys(i.tur_city)
        sleep(5)


    # Currency: Input state


    def input_aud_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.state).send_keys(i.aud_state)
        sleep(5)


    def input_cad_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.state).send_keys(i.cad_state)
        sleep(5)


    def input_eur_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.state).send_keys(i.eur_state)
        sleep(5)


    def input_eur_c_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.state).send_keys(i.eur_c_state)
        sleep(5)


    def input_eur_i_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.state).send_keys(i.eur_i_state)
        sleep(5)


    def input_gbp_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.state).send_keys(i.gbp_state)
        sleep(5)


    def input_nzd_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.state).send_keys(i.nzd_state)
        sleep(5)


    def input_usd_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.state).send_keys(i.usd_state)
        sleep(5)


    def input_usd_e_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.state).send_keys(i.usd_e_state)
        sleep(5)


    def input_usd_n_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.state).send_keys(i.usd_n_state)
        sleep(5)


    def input_test_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.state).send_keys(i.test_state)
        sleep(5)

    def input_tur_state(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.state).send_keys(i.tur_state)
        sleep(5)


    # Currency: Input post code

    def input_aud_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.postcode).send_keys(i.aud_postcode)
        sleep(5)


    def input_cad_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.postcode).send_keys(i.cad_postcode)
        sleep(5)


    def input_eur_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.postcode).send_keys(i.eur_postcode)
        sleep(5)


    def input_eur_c_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.postcode).send_keys(i.eur_c_postcode)
        sleep(5)


    def input_eur_i_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.postcode).send_keys(i.eur_i_postcode)
        sleep(5)


    def input_gbp_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.postcode).send_keys(i.gbp_postcode)
        sleep(5)


    def input_nzd_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.postcode).send_keys(i.nzd_postcode)
        sleep(5)


    def input_usd_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.postcode).send_keys(i.usd_postcode)
        sleep(5)


    def input_usd_e_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.postcode).send_keys(i.usd_e_postcode)
        sleep(5)


    def input_usd_n_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.postcode).send_keys(i.usd_n_postcode)
        sleep(5)

    def input_test_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.postcode).send_keys(i.test_postcode)
        sleep(5)


    def input_tur_postcode(self):

        i = Data(self.driver)

        return self.driver.find_element(*BillingDetails.postcode).send_keys(i.tur_postcode)
        sleep(5)



    def input_tur_billingaddressline2(self):
        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.billingaddressline2).send_keys(i.tur_billingaddressline2)
        sleep(5)

    # Currency: Input city

    def input_aud_city(self):
        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.city).send_keys(i.aud_city)
        sleep(5)


    def input_cad_city(self):
        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.city).send_keys(i.cad_city)
        sleep(5)


    def input_eur_city(self):
        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.city).send_keys(i.eur_city)
        sleep(5)


    def input_eur_c_city(self):
        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.city).send_keys(i.eur_c_city)
        sleep(5)


    def input_eur_i_city(self):
        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.city).send_keys(i.eur_i_city)
        sleep(5)


    def input_gbp_city(self):
        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.city).send_keys(i.gbp_city)
        sleep(5)


    def input_nzd_city(self):
        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.city).send_keys(i.nzd_city)
        sleep(5)


    def input_usd_city(self):
        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.city).send_keys(i.usd_city)
        sleep(5)


    def input_usd_e_city(self):
        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.city).send_keys(i.usd_e_city)
        sleep(5)


    def input_usd_n_city(self):
        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.city).send_keys(i.usd_n_city)
        sleep(5)


    def input_test_city(self):
        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.city).send_keys(i.test_city)

    def input_tur_city(self):
        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.city).send_keys(i.tur_city)
        sleep(5)


    # Currency: Input state


    def input_aud_state(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.state).send_keys(i.aud_state)
        sleep(5)


    def input_cad_state(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.state).send_keys(i.cad_state)
        sleep(5)


    def input_eur_state(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.state).send_keys(i.eur_state)
        sleep(5)


    def input_eur_c_state(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.state).send_keys(i.eur_c_state)
        sleep(5)


    def input_eur_i_state(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.state).send_keys(i.eur_i_state)
        sleep(5)


    def input_gbp_state(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.state).send_keys(i.gbp_state)
        sleep(5)


    def input_nzd_state(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.state).send_keys(i.nzd_state)
        sleep(5)


    def input_usd_state(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.state).send_keys(i.usd_state)
        sleep(5)


    def input_usd_e_state(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.state).send_keys(i.usd_e_state)
        sleep(5)


    def input_usd_n_state(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.state).send_keys(i.usd_n_state)
        sleep(5)


    def input_test_state(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.state).send_keys(i.test_state)

    def input_tur_state(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.state).send_keys(i.tur_state)
        sleep(5)


    # Currency: Input post code

    def input_aud_postcode(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.postcode).send_keys(i.aud_postcode)
        sleep(5)


    def input_cad_postcode(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.postcode).send_keys(i.cad_postcode)
        sleep(5)


    def input_eur_postcode(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.postcode).send_keys(i.eur_postcode)
        sleep(5)


    def input_eur_c_postcode(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.postcode).send_keys(i.eur_c_postcode)
        sleep(5)


    def input_eur_i_postcode(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.postcode).send_keys(i.eur_i_postcode)
        sleep(5)


    def input_gbp_postcode(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.postcode).send_keys(i.gbp_postcode)
        sleep(5)


    def input_nzd_postcode(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.postcode).send_keys(i.nzd_postcode)
        sleep(5)


    def input_usd_postcode(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.postcode).send_keys(i.usd_postcode)
        sleep(5)


    def input_usd_e_postcode(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.postcode).send_keys(i.usd_e_postcode)
        sleep(5)


    def input_usd_n_postcode(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.postcode).send_keys(i.usd_n_postcode)
        sleep(5)

    def input_test_postcode(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.postcode).send_keys(i.test_postcode)

    def input_tur_postcode(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.postcode).send_keys(i.tur_postcode)
        sleep(5)



    # Currency: Select country

    def select_aud(self):
        self.driver.find_element(*BillingDetails.aud).click()
        sleep(10)


    def select_cad(self):
        self.driver.find_element(*BillingDetails.cad).click()
        sleep(10)


    def select_eur(self):
        self.driver.find_element(*BillingDetails.eur).click()
        sleep(10)


    def select_eur_c(self):
        self.driver.find_element(*BillingDetails.eur_c).click()
        sleep(10)

    def select_eur_i(self):
        self.driver.find_element(*BillingDetails.eur_i).click()
        sleep(10)


    def select_gbp(self):
        self.driver.find_element(*BillingDetails.gbp).click()
        sleep(10)


    def select_nzd(self):
        self.driver.find_element(*BillingDetails.nzd).click()
        sleep(10)


    def select_usd(self):
        self.driver.find_element(*BillingDetails.usd).click()
        sleep(10)


    def select_test_country(self):
        self.driver.find_element(*BillingDetails.gbp).click()
        sleep(10)

    def select_tur_country(self):
        self.driver.find_element(*BillingDetails.tur).click()
        sleep(10)

    # Countries: Proceed to billing details

    def input_aud_billing_details_and_proceed(self):
        self.input_aud_firstname()
        self.input_aud_lastname()
        self.input_aud_country()
        self.select_aud()
        self.input_aud_billingaddressline1()
        self.input_aud_billingaddressline2()
        self.input_aud_city()
        self.input_aud_state()
        self.input_aud_postcode()
        self.click_gotorevieworder()


    def input_cad_billing_details_and_proceed(self):
        self.input_cad_firstname()
        self.input_cad_lastname()
        self.input_cad_country()
        self.select_cad()
        self.input_cad_billingaddressline1()
        self.input_cad_billingaddressline2()
        self.input_cad_city()
        self.input_cad_state()
        self.input_cad_postcode()
        self.click_gotorevieworder()


    def input_eur_billing_details_and_proceed(self):
        self.input_eur_firstname()
        self.input_eur_lastname()
        self.input_eur_country()
        self.select_eur()
        self.input_eur_billingaddressline1()
        self.input_eur_billingaddressline2()
        self.input_eur_city()
        self.input_eur_state()
        self.input_eur_postcode()
        self.click_gotorevieworder()


    def input_eur_c_billing_details_and_proceed(self):
        self.input_eur_c_firstname()
        self.input_eur_c_lastname()
        self.input_eur_c_country()
        self.select_eur_c()
        self.input_eur_c_billingaddressline1()
        self.input_eur_c_billingaddressline2()
        self.input_eur_c_city()
        self.input_eur_c_state()
        self.input_eur_c_postcode()
        self.click_gotorevieworder()


    def input_eur_i_billing_details_and_proceed(self):
        self.input_eur_i_firstname()
        self.input_eur_i_lastname()
        self.input_eur_i_country()
        self.select_eur_i()
        self.input_eur_i_billingaddressline1()
        self.input_eur_i_billingaddressline2()
        self.input_eur_i_city()
        self.input_eur_i_state()
        self.input_eur_i_postcode()
        self.click_gotorevieworder()


    def input_gbp_billing_details_and_proceed(self):
        self.input_gbp_firstname()
        self.input_gbp_lastname()
        self.input_gbp_country()
        self.select_gbp()
        self.input_gbp_billingaddressline1()
        self.input_gbp_billingaddressline2()
        self.input_gbp_city()
        self.input_gbp_state()
        self.input_gbp_postcode()
        self.click_gotorevieworder()


    def input_nzd_billing_details_and_proceed(self):
        self.input_nzd_firstname()
        self.input_nzd_lastname()
        self.input_nzd_country()
        self.select_nzd()
        self.input_nzd_billingaddressline1()
        self.input_nzd_billingaddressline2()
        self.input_nzd_city()
        self.input_nzd_state()
        self.input_nzd_postcode()
        self.click_gotorevieworder()


    def input_usd_billing_details_and_proceed(self):
        self.input_usd_firstname()
        self.input_usd_lastname()
        self.input_usd_country()
        self.select_usd()
        self.input_usd_billingaddressline1()
        self.input_usd_billingaddressline2()
        self.input_usd_city()
        self.input_usd_state()
        self.input_usd_postcode()
        self.click_gotorevieworder()


    def input_usd_e_billing_details_and_proceed(self):
        self.input_usd_e_firstname()
        self.input_usd_e_lastname()
        self.input_usd_e_country()
        self.select_usd()
        self.input_usd_e_billingaddressline1()
        self.input_usd_e_billingaddressline2()
        self.input_usd_e_city()
        self.input_usd_e_state()
        self.input_usd_e_postcode()
        self.click_gotorevieworder()


    def input_usd_n_billing_details_and_proceed(self):
        self.input_usd_n_firstname()
        self.input_usd_n_lastname()
        self.input_usd_n_country()
        self.select_usd()
        self.input_usd_n_billingaddressline1()
        self.input_usd_n_billingaddressline2()
        self.input_usd_n_city()
        self.input_usd_n_state()
        self.input_usd_n_postcode()
        self.click_gotorevieworder()

    def input_test_billing_details_and_proceed(self):
        self.input_test_firstname()
        self.input_test_lastname()
        self.input_test_country()
        self.select_test_country()
        self.input_test_billingaddressline1()
        self.input_test_billingaddressline2()
        self.input_test_city()
        self.input_test_state()
        self.input_test_postcode()
        self.click_gotorevieworder()

    # -------------------------------------------------------------------------------------------------------------------
    # DCESC-579
    def input_tur_billing_details_and_proceed(self):
        self.input_test_firstname()
        self.input_test_lastname()
        self.input_tur_country()
        self.select_tur_country()
        self.input_tur_billingaddressline1()
        self.input_tur_billingaddressline2()
        self.input_tur_city()
        self.input_tur_state()
        self.input_tur_postcode()
        self.click_gotorevieworder()
    #-------------------------------------------------------------------------------------------------------------------
    # DCESC

    search_address = (By.XPATH, "//*[@id='address_search']")

    tur_search = (By.XPATH, "//span[text()='Türkiye']")

    tur_country_code = (By.XPATH, "//li[@countrycode='tur']")

    tur_address_search = (By.XPATH, "//*[@id='cc_c2a']/ul/li[1]")

    change_country_btn = (By.XPATH, "//span[text()='Change country']")


    def click_searchaddress(self):

        self.driver.find_element(*BillingDetails.search_address).click()
        sleep(5)

    def click_change_country_btn(self):
        self.driver.find_element(*BillingDetails.change_country_btn).click()
        sleep(5)

    def input_tur_country_search(self):

        i = Data(self.driver)

        self.driver.find_element(*BillingDetails.search_address).send_keys(i.tur_country)
        sleep(10)

    def select_tur_country_search(self):
        self.driver.find_element(*BillingDetails.tur_search).click()
        sleep(5)

    def input_tur_address_search(self):
        self.driver.find_element(*BillingDetails.search_address).send_keys(1)
        sleep(5)

    def select_tur_address_search(self):
        self.driver.find_element(*BillingDetails.tur_address_search).click()
        sleep(5)

    def input_tur_billing_details_searchaddress_and_proceed(self):
        self.input_test_firstname()
        self.input_test_lastname()
        self.click_searchaddress()
        self.click_change_country_btn()
        self.input_tur_country_search()
        self.select_tur_country_search()
        self.input_tur_address_search()
        self.select_tur_address_search()
        self.click_gotorevieworder()

    def check_tur_country_dropdown_text(self):
        text = self.driver.find_element(*BillingDetails.tur_search).text
        return text

    def check_tur_country_dropdown_code(self):
        code = self.driver.find_element(*BillingDetails.tur_country_code).get_attribute("countrycode")
        return code

    def check_country_searchbox_value(self):
        value = self.driver.find_element(*BillingDetails.search_address).get_attribute("value")
        return value


    def input_tur_billing_details_searchaddress_only_p1(self):
        self.input_test_firstname()
        self.input_test_lastname()
        self.click_searchaddress()
        self.click_change_country_btn()
        self.input_tur_country_search()

    def check_country_value(self):
        value = self.driver.find_element(*BillingDetails.country).get_attribute("value")
        return value

    def input_tur_billing_details_searchaddress_only_p2(self):
        self.select_tur_country_search()
        self.input_tur_address_search()
        self.select_tur_address_search()

    #-------------------------------------------------------------------------------------------------------------------

    subtotal = (By.XPATH, "//*[@class='subtotal']/span")

    def get_subtotal_with_whitespace(self):
        return self.driver.find_element(*BillingDetails.subtotal).text.replace(" \n", " ")

    def get_subtotal_without_whitespace(self):
        return self.driver.find_element(*BillingDetails.subtotal).text.strip()

    def get_aud_subtotal(self):
        return self.get_subtotal_with_whitespace()

    def get_cad_subtotal(self):
        return self.get_subtotal_with_whitespace()

    def get_eur_subtotal(self):
        return self.get_subtotal_without_whitespace()

    def get_eur_c_subtotal(self):
        return self.get_subtotal_without_whitespace()

    def get_eur_i_subtotal(self):
        return self.get_subtotal_without_whitespace()

    def get_gbp_subtotal(self):
        return self.get_subtotal_without_whitespace()

    def get_nzd_subtotal(self):
        return self.get_subtotal_with_whitespace()

    def get_usd_subtotal(self):
        return self.get_subtotal_with_whitespace()

    def get_usd_e_subtotal(self):
        return self.get_subtotal_with_whitespace()

    def get_usd_n_subtotal(self):
        return self.get_subtotal_with_whitespace()

    #-------------------------------------------------------------------------------------------------------------------

    backtoshopping = (By.XPATH, "//*[text()=' Back to shopping ']")

    def backtoshopping_enabled(self):
        return self.driver.find_element(*BillingDetails.backtoshopping).is_enabled()

    #-------------------------------------------------------------------------------------------------------------------

    chevron = (By.XPATH, "//*[contains(@class,'chevron')]")

    def click_chevron(self):
        self.driver.find_element(*BillingDetails.chevron).click()
        sleep(25)

    def chevron_enabled(self):
        return self.driver.find_element(*BillingDetails.chevron).is_enabled()

    #-------------------------------------------------------------------------------------------------------------------

    def page_src(self):
        body = self.driver.find_element(By.TAG_NAME, 'body').text
        return body

    #-------------------------------------------------------------------------------------------------------------------

    legal         = (By.XPATH, "//*[text()=' Legal ']")

    privacynotice = (By.XPATH, "//*[text()=' Privacy Notice ']")

    accessibilty  = (By.XPATH, "//*[text()=' Accessibility ']")

    help          = (By.XPATH, "//*[text()=' Help ']")

    def click_legal(self):
        return self.driver.find_element(*BillingDetails.legal).click()

    def click_privacynotice(self):
        self.driver.find_element(*BillingDetails.privacynotice).click()

    def click_accessibility(self):
        self.driver.find_element(*BillingDetails.accessibilty).click()

    def click_help(self):
        self.driver.find_element(*BillingDetails.help).click()

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
        self.driver.find_element(*BillingDetails.cart).click()
        sleep(25)

    #-------------------------------------------------------------------------------------------------------------------
