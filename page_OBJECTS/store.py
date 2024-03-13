from selenium.webdriver.common.by import By
from time import sleep

class Store:

    def __init__(self, driver):
        self.driver = driver

    addtobasket1 = (By.XPATH, "(//*[text()=' Add to cart '])[1]")

    addtobasket2 = (By.XPATH, "(//*[text()=' Add to cart '])[2]")

    addtobasket3 = (By.XPATH, "(//*[text()=' Add to cart '])[3]")

    def click_addtobasket1(self):
        self.driver.find_element(*Store.addtobasket1).click()
        sleep(5)

    def click_addtobasket2(self):
        self.driver.find_element(*Store.addtobasket2).click()
        sleep(5)

    def click_addtobasket3(self):
        self.driver.find_element(*Store.addtobasket3).click()
        sleep(5)

    #-------------------------------------------------------------------------------------------------------------------

    cart = (By.XPATH, "//*[contains(@class,'basket-icon')]")

    def click_cart(self):
        self.driver.find_element(*Store.cart).click()
        sleep(20)

    #-------------------------------------------------------------------------------------------------------------------

    currency = (By.XPATH, "//div[contains(@id,'vs3')]")

    aud      = (By.XPATH, "//*[contains(text(),'AUD')]")

    cad      = (By.XPATH, "//*[contains(text(),'CAD')]")

    eur      = (By.XPATH, "//*[contains(text(),'EUR')]")

    nzd      = (By.XPATH, "//*[contains(text(),'NZD')]")

    gbp      = (By.XPATH, "//*[contains(text(),'GBP')]")

    usd      = (By.XPATH, "//*[contains(text(),'USD')]")

    usd_e    = (By.XPATH, "//*[contains(text(),'USD-E')]")

    usd_n    = (By.XPATH, "//*[contains(text(),'USD-N')]")

    eur_c    = (By.XPATH, "//*[contains(text(),'EUR-C')]")

    eur_i    = (By.XPATH, "//*[contains(text(),'EUR-I')]")

    store    = (By.XPATH, "//div[contains(@id,'vs1')]")

    compass  = (By.XPATH, "//*[contains(text(),'Compass')]")

    cem      = (By.XPATH, "//*[contains(text(),'CEM')]")

    eds      = (By.XPATH, "//*[contains(text(),'English')]")

    cws      = (By.XPATH, "//*[contains(text(),'CWS')]")

    def click_currency(self):
        self.driver.find_element(*Store.currency).click()
        sleep(5)

    def click_aud(self):
        self.driver.find_element(*Store.aud).click()
        sleep(10)

    def click_cad(self):
        self.driver.find_element(*Store.cad).click()
        sleep(10)

    def click_eur(self):
        self.driver.find_element(*Store.eur).click()
        sleep(10)

    def click_eur_c(self):
        self.driver.find_element(*Store.eur_c).click()
        sleep(10)

    def click_eur_i(self):
        self.driver.find_element(*Store.eur_i).click()
        sleep(10)

    def click_gbp(self):
        self.driver.find_element(*Store.gbp).click()
        sleep(10)

    def click_nzd(self):
        self.driver.find_element(*Store.nzd).click()
        sleep(10)

    def click_usd(self):
        self.driver.find_element(*Store.usd).click()
        sleep(10)

    def click_usd_e(self):
        self.driver.find_element(*Store.usd_e).click()
        sleep(10)

    def click_usd_n(self):
        self.driver.find_element(*Store.usd_n).click()
        sleep(10)
    def select_aud(self):
        self.click_currency()
        self.click_aud()

    def select_cad(self):
        self.click_currency()
        self.click_cad()

    def select_eur(self):
        self.click_currency()
        self.click_eur()

    def select_eur_c(self):
        self.click_store()
        self.click_eds()
        self.click_currency()
        self.click_eur_c()

    def select_eur_i(self):
        self.click_store()
        self.click_eds()
        self.click_currency()
        self.click_eur_i()

    def select_gbp(self):
        self.click_currency()
        self.click_gbp()

    def select_nzd(self):
        self.click_currency()
        self.click_nzd()

    def select_usd(self):
        self.click_currency()
        self.click_usd()

    def select_usd_e(self):
        self.click_store()
        self.click_eds()
        self.click_currency()
        self.click_usd_e()

    def select_usd_n(self):
        self.click_store()
        self.click_eds()
        self.click_currency()
        self.click_usd_n()

    def click_store(self):
        self.driver.find_element(*Store.store).click()
        sleep(5)

    def click_compass(self):
        self.driver.find_element(*Store.compass).click()
        sleep(10)

    def click_cem(self):
        self.driver.find_element(*Store.cem).click()
        sleep(10)

    def click_eds(self):
        self.driver.find_element(*Store.eds).click()
        sleep(10)

    def click_cws(self):
        self.driver.find_element(*Store.cws).click()
        sleep(10)
