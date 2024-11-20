from selenium.webdriver.common.by import By
from time import sleep
import math

class Store:

    def __init__(self, driver):
        self.driver = driver
        self.get_gbp_PS1_price_for_mixed = self.get_gbp_PS1_price()

        self.AUD_del_charge = 9.90
        self.CAD_del_charge = 10.50
        self.GBP_del_charge = 4.50
        self.NZD_del_charge = 13.95
        # EUR - C
        # EUR - I
        # USD - E
        # USD - N

    cart_count = (By.XPATH, "//*[contains(@class,'count')]")

    def cartcount_displayed(self):
        self.driver.find_element(*Store.cart_count).is_displayed()

    def get_cartcount(self):
        return self.driver.find_element(*Store.cart_count).text

    #-------------------------------------------------------------------------------------------------------------------

    addtobasket1 = (By.XPATH, "(//*[text()=' Add to cart '])[1]")

    addtobasket2 = (By.XPATH, "(//*[text()=' Add to cart '])[2]")

    addtobasket3 = (By.XPATH, "(//*[text()=' Add to cart '])[3]")

    addtobasket7 = (By.XPATH, "(//*[text()=' Add to cart '])[7]")

    def click_addtobasket1(self):
        self.driver.find_element(*Store.addtobasket1).click()
        sleep(5)

    def click_addtobasket2(self):
        self.driver.find_element(*Store.addtobasket2).click()
        sleep(5)

    def click_addtobasket3(self):
        self.driver.find_element(*Store.addtobasket3).click()
        sleep(5)

    def click_addtobasket7(self):
        self.driver.find_element(*Store.addtobasket7).click()
        sleep(5)

    #-------------------------------------------------------------------------------------------------------------------

    buynow1 = (By.XPATH, "(//*[text()=' Buy now '])[1]")

    buynow2 = (By.XPATH, "(//*[text()=' Buy now '])[2]")

    def click_buynow1(self):
        self.driver.find_element(*Store.buynow1).click()
        sleep(25)

    def click_buynow2(self):
        self.driver.find_element(*Store.buynow2).click()
        sleep(25)

    #-------------------------------------------------------------------------------------------------------------------

    cart = (By.XPATH, "//*[contains(@class,'basket-icon')]")

    def click_cart(self):
        self.driver.find_element(*Store.cart).click()
        sleep(20)

    def click_cart_slow(self):
        self.driver.find_element(*Store.cart).click()
        sleep(5)

    #-------------------------------------------------------------------------------------------------------------------

    currency = (By.XPATH, "//div[contains(@id,'vs4')]")

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

    store    = (By.XPATH, "//div[contains(@id,'vs2')]")

    compass  = (By.XPATH, "//*[contains(text(),'Compass')]")

    cem      = (By.XPATH, "//*[contains(text(),'CEM')]")

    eds      = (By.XPATH, "//*[contains(text(),'English')]")

    cws      = (By.XPATH, "//*[contains(text(),'CWS')]")

    next     = (By.XPATH, "//*[text()='›']")

    language = (By.XPATH, "//div[contains(@id,'vs3')]")

    english     = (By.XPATH, "//*[contains(text(),'English')]")

    spanish     = (By.XPATH, "//*[contains(text(),'Spanish')]")

    italian     = (By.XPATH, "//*[contains(text(),'Italian')]")

    french      = (By.XPATH, "//*[contains(text(),'French')]")

    german      = (By.XPATH, "//*[contains(text(),'German')]")

    portuguese  = (By.XPATH, "//*[contains(text(),'Portuguese')]")

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

    def click_next(self):
        self.driver.find_element(*Store.next).click()
        sleep(3)

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

    def click_language(self):
        self.driver.find_element(*Store.language).click()
        sleep(5)

    def click_english(self):
        self.driver.find_element(*Store.english).click()
        sleep(10)

    def select_english(self):
        self.click_language()
        self.click_english()

    def click_spanish(self):
        self.driver.find_element(*Store.spanish).click()
        sleep(10)

    def select_spanish(self):
        self.click_language()
        self.click_spanish()

    def click_italian(self):
        self.driver.find_element(*Store.italian).click()
        sleep(10)

    def select_italian(self):
        self.click_language()
        self.click_italian()

    def click_french(self):
        self.driver.find_element(*Store.french).click()
        sleep(10)

    def select_french(self):
        self.click_language()
        self.click_french()

    def click_german(self):
        self.driver.find_element(*Store.german).click()
        sleep(10)

    def select_german(self):
        self.click_language()
        self.click_german()

    def click_portuguese(self):
        self.driver.find_element(*Store.portuguese).click()
        sleep(10)

    def select_portuguese(self):
        self.click_language()
        self.click_portuguese()

    #Stores switch
    def select_eds(self):
        self.click_store()
        self.click_eds()

    def select_compass(self):
        self.click_store()
        self.click_compass()

    #-------------------------------------------------------------------------------------------------------------------

    shop_price1 = (By.XPATH, "(//*[contains(@class, 'font-weight-bold')])[1]")


    def check_store_currency(self):
        currency_text = self.driver.find_element(*Store.shop_price1).text
        currency_str = currency_text.replace("AU$", "AU $")
        currency_str1 = currency_str.replace("AU $ ", "AU $")
        return currency_str1

    #-------------------------------------------------------------------------------------------------------------------

    itemprice1 = (By.XPATH, "//*[@class='product-card'][contains(.,'B2')]//*[contains(@class,'price')]")

    itemprice2 = (By.XPATH, "//*[@class='product-card'][contains(.,'C1')]//*[contains(@class,'price')]")

    itemprice3 = (By.XPATH, "//*[@class='product-card'][contains(.,'A2')]//*[contains(@class,'price')]")

    def get_itemprice1(self):
        return self.driver.find_element(*Store.itemprice1).text

    def get_itemprice2(self):
        return self.driver.find_element(*Store.itemprice2).text

    def get_itemprice3(self):
        return self.driver.find_element(*Store.itemprice3).text

    def get_aud_itemprice1(self):
        x001 = self.get_itemprice1()
        x002 = x001[:2] + " " + x001[2:]
        x003 = x002[:4] + x002[4+1:]
        return x003

    def get_cad_itemprice1(self):
        x001 = self.get_itemprice1()
        x002 = x001[:2] + " " + x001[2:]
        x003 = x002[:4] + x002[4+1:]
        return x003

    def get_eur_itemprice1(self):
        x001 = self.get_itemprice1()
        x002 = x001.replace(".", ",")
        return x002

    def get_eur_c_itemprice1(self):
        x001 = self.get_itemprice1()
        x002 = x001.replace(".", ",")
        x003 = x002.replace(" ", "")
        return x003

    def get_eur_i_itemprice1(self):
        x001 = self.get_itemprice1()
        x002 = x001.replace(".", ",")
        x003 = x002.replace(" ", "")
        return x003

    def get_gbp_itemprice1(self):
        x001 = self.get_itemprice1()
        x003 = x001.replace(" ", "")
        return x003

    def get_nzd_itemprice1(self):
        x001 = self.get_itemprice1()
        x002 = x001[:2] + " " + x001[2:]
        x003 = x002[:4] + x002[4+1:]
        return x003

    def get_usd_itemprice1(self):
        x001 = self.get_itemprice1()
        x002 = x001[:2] + " " + x001[2:]
        x003 = x002[:4] + x002[4+1:]
        return x003

    def get_usd_e_itemprice1(self):
        x001 = self.get_itemprice1()
        x002 = x001[:2] + " " + x001[2:]
        x003 = x002[:4] + x002[4+1:]
        return x003

    def get_usd_n_itemprice1(self):
        x001 = self.get_itemprice1()
        x002 = x001[:2] + " " + x001[2:]
        x003 = x002[:4] + x002[4+1:]
        return x003

    def get_subtotal(self):
        x0011 = self.get_itemprice1()
        x0012 = x0011[2:]
        x0013 = float(x0012)

        x0021 = self.get_itemprice2()
        x0022 = x0021[2:]
        x0023 = float(x0022)

        x0031 = self.get_itemprice3()
        x0032 = x0031[2:]
        x0033 = float(x0032)

        a = (x0013 + x0023 + x0033)
        b = ("{:.2f}".format(a))

        self.subtotal = b # store b as instance variable

        j = '£' + b

        return j

    def get_discount(self):
        subtotal = self.subtotal # access the instance variable

        c = float(subtotal)
        d = c * 0.25

        self.discount = d

        k = round(d + 1e-9,2) # small delta
        l = '£' + str(k)

        return l

    def get_ordertotal(self):
        subtotal = self.subtotal
        discount = self.discount

        e = float(subtotal)
        f = float(discount)
        g = e-f

        m = round(g + 1e-9,2)
        n = '£' + str(m)

        return n

    #-------------------------------------------------------------------------------------------------------------------

    TT_B2FSS_price = (By.XPATH, "//*[@class='product-card'][contains(.,'B2')]//*[contains(@class,'price')]")

    TT_B2FSS_qty   = (By.XPATH, "//*[@class='product-card'][contains(.,'B2')]//*[contains(@class,'input')]")

    TT_B2FSS = (By.XPATH, "//*[@class='product-card'][contains(.,'B2')]//*[contains(@class,'title')]")

    SF_L1DSB_price = (By.XPATH, "//*[@class='product-card'][contains(.,'Shape')]//*[contains(@class,'price')]")

    QM_L2TRBSE_price = (By.XPATH, "//*[@class='product-card'][contains(.,'Quick')]//*[contains(@class,'price')]")

    OAA_L1TRD_price = (By.XPATH, "//*[@class='product-card'][contains(.,'Out and About')]//*[contains(@class,'price')]")

    # SF_L1DSB_price = (By.XPATH, "//*[@class='product-card'][contains(.,'Evolve Digital Level 6B')]//*[contains(@class,'price')]")

    FP1_price = (By.XPATH, "//*[@class='product-card'][contains(.,'Free Product 1')]//*[contains(@class,'price')]")

    MB2RPR_price = (By.XPATH, "//*[@class='product-card'][contains(.,'Mosaic B2')]//*[contains(@class,'price')]")

    def get_TT_B2FSS_price(self):
        return self.driver.find_element(*Store.TT_B2FSS_price).text.replace(" ","")

    def get_TT_B2FSS_qty(self):
        return self.driver.find_element(*Store.TT_B2FSS_qty).get_attribute('value')

    def get_TT_B2FSS(self):
        return self.driver.find_element(*Store.TT_B2FSS).text

    def get_SF_L1DSB_price(self):
        return self.driver.find_element(*Store.SF_L1DSB_price).text.replace(" ","")

    def get_QM_L2TRBSE_price(self):
        return self.driver.find_element(*Store.QM_L2TRBSE_price).text.replace(" ","")

    def get_OAA_L1TRD_price(self):
        return self.driver.find_element(*Store.OAA_L1TRD_price).text.replace(" ","")


    def get_FP1_price(self):
        return self.driver.find_element(*Store.FP1_price).text.replace(" ","")

    def get_MB2RPR_price(self):
        return self.driver.find_element(*Store.MB2RPR_price).text

    def get_aud_TT_B2FSS_price(self):
        x001 = self.get_TT_B2FSS_price()
        x002 = x001[:2] + " " + x001[2:]
        x003 = x002[:4] + x002[4+1:]
        return x002

    def get_aud_PS1_price(self):
        x001 = self.get_PS1_price()
        x002 = x001[:2] + " " + x001[2:]
        x003 = x002[:4] + x002[4+1:]
        return x002

    def get_aud_FP1_price(self):
        x001 = self.get_FP1_price()
        x002 = x001[:2] + " " + x001[2:]
        return x002

    def get_cad_TT_B2FSS_price(self):
        x001 = self.get_TT_B2FSS_price()
        x002 = x001[:2] + " " + x001[2:]
        x003 = x002[:4] + x002[4+1:]
        return x002

    def get_cad_PS1_price(self):
        x001 = self.get_PS1_price()
        x002 = x001[:2] + " " + x001[2:]
        x003 = x002[:4] + x002[4+1:]
        return x002

    def get_cad_FP1_price(self):
        x001 = self.get_FP1_price()
        x002 = x001[:2] + " " + x001[2:]
        return x002

    def get_eur_TT_B2FSS_price(self):
        x001 = self.get_TT_B2FSS_price()
        x002 = x001.replace(".", ",")
        x003 = x002[:1] + " " + x002[1:]
        return x003

    def get_eur_PS1_price(self):
        x001 = self.get_PS1_price()
        x002 = x001.replace(".", ",")
        x003 = x002[:1] + " " + x002[1:]
        return x003

    def get_eur_FP1_price(self):
        x001 = self.get_FP1_price()
        x002 = x001.replace(".", ",")
        x003 = x002[:1] + " " + x002[1:]
        return x003

    def get_eur_c_SF_L1DSB_price(self):
        x001 = self.get_SF_L1DSB_price()
        x002 = x001.replace(".", ",")
        x003 = x002.replace(" ", "")
        return x003


    def get_eur_c_QM_L2TRBSE_price(self):
        x001 = self.get_QM_L2TRBSE_price()
        x002 = x001.replace(".", ",")
        x003 = x002.replace(" ", "")
        return x003

    def get_eur_c_OAA_L1TRD_price(self):
        x001 = self.get_OAA_L1TRD_price()
        x002 = x001.replace(".", ",")
        x003 = x002.replace(" ", "")
        return x003


    def get_eur_c_MB2RPR_price(self):
        x001 = self.get_MB2RPR_price()
        x002 = x001.replace(".", ",")
        x003 = x002.replace(" ", "")
        return x003

    def get_eur_i_SF_L1DSB_price(self):
        x001 = self.get_SF_L1DSB_price()
        x002 = x001.replace(".", ",")
        x003 = x002.replace(" ", "")
        return x003

    def get_eur_i_QM_L2TRBSE_price(self):
        x001 = self.get_QM_L2TRBSE_price()
        x002 = x001.replace(".", ",")
        x003 = x002.replace(" ", "")
        return x003

    def get_eur_i_OAA_L1TRD_price(self):
        x001 = self.get_OAA_L1TRD_price()
        x002 = x001.replace(".", ",")
        x003 = x002.replace(" ", "")
        return x003

    def get_eur_i_MB2RPR_price(self):
        x001 = self.get_MB2RPR_price()
        x002 = x001.replace(".", ",")
        x003 = x002.replace(" ", "")
        return x003

    def get_gbp_TT_B2FSS_price(self):
        x001 = self.get_TT_B2FSS_price()
        x003 = x001.replace(" ", "")
        return x003

    def get_gbp_FP1_price(self):
        x001 = self.get_FP1_price()
        x003 = x001.replace(" ", "")
        return x003

    def get_gbp_PS1_price(self):
        x001 = self.get_PS1_price()
        x003 = x001.replace(" ", "")
        return x003

    def get_nzd_TT_B2FSS_price(self):
        x001 = self.get_TT_B2FSS_price()
        x002 = x001[:2] + " " + x001[2:]
        x003 = x002[:4] + x002[4+1:]
        return x002

    def get_nzd_FP1_price(self):
        x001 = self.get_FP1_price()
        x002 = x001[:2] + " " + x001[2:]
        return x002

    def get_nzd_PS1_price(self):
        x001 = self.get_PS1_price()
        x002 = x001[:2] + " " + x001[2:]
        return x002

    def get_usd_TT_B2FSS_price(self):
        x001 = self.get_TT_B2FSS_price()
        x002 = x001[:2] + " " + x001[2:]
        x003 = x002[:4] + x002[4+1:]
        return x002

    def get_usd_FP1_price(self):
        x001 = self.get_FP1_price()
        x002 = x001[:2] + " " + x001[2:]
        return x002

    def get_usd_PS1_price(self):
        x001 = self.get_PS1_price()
        x002 = x001[:2] + " " + x001[2:]
        return x002

    def get_usd_e_SF_L1DSB_price(self):
        x001 = self.get_SF_L1DSB_price()
        x002 = x001[:2] + " " + x001[2:]
        x003 = x002[:4] + x002[4+1:]
        return x002

    def get_usd_e_MB2RPR_price(self):
        x001 = self.get_MB2RPR_price()
        x002 = x001[:2] + " " + x001[2:]
        x003 = x002[:4] + x002[4+1:]
        return x003

    def get_usd_e_QM_L2TRBSE_price(self):
        x001 = self.get_QM_L2TRBSE_price()
        x002 = x001[:2] + " " + x001[2:]
        x003 = x002[:4] + x002[4+1:]
        return x002

    def get_usd_e_OAA_L1TRD_price(self):
        x001 = self.get_OAA_L1TRD_price()
        x002 = x001[:2] + " " + x001[2:]
        x003 = x002[:4] + x002[4+1:]
        return x002

    def get_usd_n_SF_L1DSB_price(self):
        x001 = self.get_SF_L1DSB_price()
        x002 = x001[:2] + " " + x001[2:]
        x003 = x002[:4] + x002[4+1:]
        return x002

    def get_usd_n_MB2RPR_price(self):
        x001 = self.get_MB2RPR_price()
        x002 = x001[:2] + " " + x001[2:]
        x003 = x002[:4] + x002[4+1:]
        return x003

    def get_usd_n_QM_L2TRBSE_price(self):
        x001 = self.get_QM_L2TRBSE_price()
        x002 = x001[:2] + " " + x001[2:]
        x003 = x002[:4] + x002[4+1:]
        return x002

    def get_usd_n_OAA_L1TRD_price(self):
        x001 = self.get_OAA_L1TRD_price()
        x002 = x001[:2] + " " + x001[2:]
        x003 = x002[:4] + x002[4+1:]
        return x002

    def get_aud_mixed_price(self):
        def extract_price(currency_str):
            return float(currency_str.replace("AU $", "").replace(",", "").strip())

        total_value = sum(extract_price(price) for price in [self.get_aud_PS1_price(), self.get_aud_TT_B2FSS_price()])

        return f"AU ${total_value:.2f}"


    def get_cad_mixed_price(self):
        def extract_price(currency_str):
            return float(currency_str.replace("CA $", "").replace(",", "").strip())

        total_value = sum(extract_price(price) for price in [self.get_cad_PS1_price(), self.get_cad_TT_B2FSS_price()])

        return f"CA ${total_value:.2f}"


    def get_gbp_mixed_price(self):
        def extract_price(currency_str):
            return float(currency_str.replace("£", "").replace(",", "").strip())

        total_value = sum(extract_price(price) for price in [self.get_gbp_PS1_price_for_mixed, self.get_gbp_TT_B2FSS_price()])

        return f"£{total_value:.2f}"

    def get_nzd_mixed_price(self):
        def extract_price(currency_str):
            return float(currency_str.replace("NZ $", "").replace(",", "").strip())

        total_value = sum(extract_price(price) for price in [self.get_nzd_PS1_price(), self.get_nzd_TT_B2FSS_price()])

        return f"NZ ${total_value:.2f}"

    def get_eur_c_mixed_price(self):
        def extract_price(currency_str):
            return float(currency_str.replace("€", "").replace(",", "").strip())

        total_value = sum(extract_price(price) for price in [
            self.get_eur_c_OAA_L1TRD_price(),
            self.get_eur_c_SF_L1DSB_price()
        ])
        total_value_in_euros = total_value / 100
        formatted_value = f"€{total_value_in_euros:.2f}".replace('.', ',')
        return formatted_value

    def get_eur_i_mixed_price(self):
        def extract_price(currency_str):
            return float(currency_str.replace("€", "").replace(",", "").strip())

        total_value = sum(extract_price(price) for price in [
            self.get_eur_c_OAA_L1TRD_price(),
            self.get_eur_c_SF_L1DSB_price()
        ])
        total_value_in_euros = total_value / 100
        formatted_value = f"€{total_value_in_euros:.2f}".replace('.', ',')
        return formatted_value


    def get_usd_e_mixed_price(self):
        def extract_price(currency_str):
            return float(currency_str.replace("US $", "").replace(",", "").strip())

        total_value = sum(extract_price(price) for price in [self.get_usd_e_OAA_L1TRD_price(), self.get_usd_e_SF_L1DSB_price()])

        return f"US ${total_value:.2f}"

    def get_usd_n_mixed_price(self):
        def extract_price(currency_str):
            return float(currency_str.replace("US $", "").replace(",", "").strip())

        total_value = sum(extract_price(price) for price in [self.get_usd_n_OAA_L1TRD_price(), self.get_usd_n_SF_L1DSB_price()])

        return f"US ${total_value:.2f}"






    #-------------------------------------------------------------------------------------------------------------------

    cartoval = (By.XPATH, "//*[@class='oval']")

    def cartoval_displayed(self):
        return self.driver.find_element(*Store.cartoval).is_displayed()

    def cart_oval_is_displayed(self):
        return self.driver.find_element(*Store.cartoval).is_displayed()

    #-------------------------------------------------------------------------------------------------------------------

    userprofile = (By.XPATH, "//button[contains(@class,'user')]")

    signin      = (By.XPATH, "//*[contains(text(),'Sign in')]")

    def click_userprofile(self):
        self.driver.find_element(*Store.userprofile).click()
        sleep(5)

    def click_signin(self):
        self.driver.find_element(*Store.signin).click()
        sleep(5)

    def go_to_the_login_page_from_the_store(self):
        self.click_userprofile()
        self.click_signin()

    #-------------------------------------------------------------------------------------------------------------------

    atc_tp1 = (By.XPATH, "//*[@class='product-card'][contains(.,'Test Product 1')]//*[contains(text(),'Add to cart')]")

    TP1     = (By.XPATH, "//*[@class='product-card'][contains(.,'Test Product 1')]//*[contains(@class,'title')]")

    TP1_price = (By.XPATH, "//*[@class='product-card'][contains(.,'Test Product 1')]//*[contains(@class,'price')]")

    TP1_qty = (By.XPATH, "//*[@class='product-card'][contains(.,'Test Product 1')]//*[contains(@class,'input')]")

    atc_tp2 = (By.XPATH, "//*[@class='product-card'][contains(.,'Test Product 2')]//*[contains(text(),'Add to cart')]")

    atc_tp3 = (By.XPATH, "//*[@class='product-card'][contains(.,'Test Product 3')]//*[contains(text(),'Add to cart')]")

    def add_to_cart_TP1(self):
        self.driver.find_element(*Store.atc_tp1).click()
        sleep(5)

    def get_TP1(self):
        return self.driver.find_element(*Store.TP1).text

    def get_TP1_price(self):
        return self.driver.find_element(*Store.TP1_price).text.replace(" ","")

    def get_TP1_qty(self):
        return self.driver.find_element(*Store.TP1_qty).get_attribute('value')

    def add_to_cart_TP2(self):
        self.driver.find_element(*Store.atc_tp2).click()
        sleep(5)

    def add_to_cart_TP3(self):
        self.driver.find_element(*Store.atc_tp3).click()
        sleep(5)

    #-------------------------------------------------------------------------------------------------------------------

    atc_tt_b2fss   = (By.XPATH, "//*[@class='product-card'][contains(.,'B2')]//*[contains(text(),'Add to cart')]")

    bn_tt_b2fss    = (By.XPATH, "//*[@class='product-card'][contains(.,'B2')]//*[contains(text(),'Buy now')]")

    tt_b2fss_price = (By.XPATH, "//*[@class='product-card'][contains(.,'B2')]//*[contains(@class,'price')]")

    def add_to_cart_TT_B2FSS(self):
        self.driver.find_element(*Store.product_search).send_keys("B2")
        self.driver.find_element(*Store.atc_tt_b2fss).click()
        sleep(5)

    def buy_now_TT_B2FSS(self):
        self.driver.find_element(*Store.bn_tt_b2fss).click()
        sleep(20)


    # def get_TT_B2FSS_price(self):
    #     return self.driver.find_element(*Store.tt_b2fss_price).text.replace(" ","")

    atc_tt_c1ass   = (By.XPATH, "//*[@class='product-card'][contains(.,'C1')]//*[contains(text(),'Add to cart')]")

    bn_tt_c1ass    = (By.XPATH, "//*[@class='product-card'][contains(.,'C1')]//*[contains(text(),'Buy now')]")

    tt_c1ass_price = (By.XPATH, "//*[@class='product-card'][contains(.,'C1')]//*[contains(@class,'price')]")

    TT_C1ASS       = (By.XPATH, "//*[@class='product-card'][contains(.,'C1')]//*[contains(@class,'title')]")

    TT_C1ASS_qty   = (By.XPATH, "//*[@class='product-card'][contains(.,'C1')]//*[contains(@class,'input')]")

    def add_to_cart_TT_C1ASS(self):
        self.driver.find_element(*Store.atc_tt_c1ass).click()
        sleep(5)

    def buy_now_TT_C1ASS(self):
        self.driver.find_element(*Store.bn_tt_c1ass).click()
        sleep(20)

    def get_TT_C1ASS_price(self):
        return self.driver.find_element(*Store.tt_c1ass_price).text.replace(" ","")

    def get_TT_C1ASS(self):
        return self.driver.find_element(*Store.TT_C1ASS).text

    def get_TT_C1ASS_qty(self):
        return self.driver.find_element(*Store.TT_C1ASS_qty).get_attribute('value')

    atc_tt_a2ksss   = (By.XPATH, "//*[@class='product-card'][contains(.,'A2')]//*[contains(text(),'Add to cart')]")

    bn_tt_a2ksss    = (By.XPATH, "//*[@class='product-card'][contains(.,'A2')]//*[contains(text(),'Buy now')]")

    tt_a2ksss_price = (By.XPATH, "//*[@class='product-card'][contains(.,'A2')]//*[contains(@class,'price')]")

    TT_A2KSSS       = (By.XPATH, "//*[@class='product-card'][contains(.,'A2')]//*[contains(@class,'title')]")

    TT_A2KSSS_qty   = (By.XPATH, "//*[@class='product-card'][contains(.,'A2')]//*[contains(@class,'input')]")

    def add_to_cart_TT_A2KSSS(self):
        self.driver.find_element(*Store.atc_tt_a2ksss).click()
        sleep(5)

    def buy_now_TT_A2KSSS(self):
        self.driver.find_element(*Store.bn_tt_a2ksss).click()
        sleep(15)

    def get_TT_A2KSSS_price(self):
        return self.driver.find_element(*Store.tt_a2ksss_price).text.replace(" ","")

    def get_TT_A2KSSS(self):
        return self.driver.find_element(*Store.TT_A2KSSS).text

    def get_TT_A2KSSS_qty(self):
        return self.driver.find_element(*Store.TT_A2KSSS_qty).get_attribute('value')

    atc_sf_l1dsb = (By.XPATH, "//*[@class='product-card'][contains(.,'Shape')]//*[contains(text(),'Add to cart')]")

    # atc_sf_l1dsb = (By.XPATH, "//*[@class='product-card'][contains(.,'Evolve Digital Level 6B')]//*[contains(text(),'Add to cart')]")

    def add_to_cart_SF_L1DSB(self):
        self.driver.find_element(*Store.product_search).send_keys("Shape")
        self.driver.find_element(*Store.atc_sf_l1dsb).click()
        sleep(5)

    atc_qm_l2trbse = (By.XPATH, "//*[@class='product-card'][contains(.,'Quick')]//*[contains(text(),'Add to cart')]")

    def add_to_cart_QM_L2TRBSE(self):
        self.driver.find_element(*Store.product_search).send_keys("Quick")
        self.driver.find_element(*Store.atc_qm_l2trbse).click()
        sleep(5)

    atc_oaa_l1trd = (By.XPATH, "//*[@class='product-card'][contains(.,'Out and About')]//*[contains(text(),'Add to cart')]")

    def add_to_cart_OAA_L1TRD(self):
        self.driver.find_element(*Store.atc_oaa_l1trd).click()
        sleep(5)

    atc_bp1 = (By.XPATH, "//*[@class='product-card'][contains(.,'Bookable Product 1')]//*[contains(text(),'Add to cart')]")

    inc_bp1 = (By.XPATH, "//*[@class='product-card'][contains(.,'Bookable Product 1')]//*[contains(text(),'+')]")

    bp1_qty = (By.XPATH, "//*[@class='product-card'][contains(.,'Bookable Product 1')]//*[@class='quantity-input']")

    def add_to_cart_BP1(self):
        self.driver.find_element(*Store.atc_bp1).click()
        sleep(5)

    def increase_BP1(self):
        self.driver.find_element(*Store.inc_bp1).click()
        sleep(2)

    def get_BP1_qty(self):
        return self.driver.find_element(*Store.bp1_qty).get_attribute('value')

    atc_bp2 = (By.XPATH, "//*[@class='product-card'][contains(.,'Bookable Product 2')]//*[contains(text(),'Add to cart')]")

    inc_bp2 = (By.XPATH, "//*[@class='product-card'][contains(.,'Bookable Product 2')]//*[contains(text(),'+')]")

    bp2_qty = (By.XPATH, "//*[@class='product-card'][contains(.,'Bookable Product 2')]//*[@class='quantity-input']")

    def add_to_cart_BP2(self):
        self.driver.find_element(*Store.atc_bp2).click()
        sleep(5)

    def increase_BP2(self):
        self.driver.find_element(*Store.inc_bp2).click()
        sleep(2)

    def get_BP2_qty(self):
        return self.driver.find_element(*Store.bp2_qty).get_attribute('value')

    atc_bp3 = (By.XPATH, "//*[@class='product-card'][contains(.,'Bookable Product 3')]//*[contains(text(),'Add to cart')]")

    inc_bp3 = (By.XPATH, "//*[@class='product-card'][contains(.,'Bookable Product 3')]//*[contains(text(),'+')]")

    bp3_qty = (By.XPATH, "//*[@class='product-card'][contains(.,'Bookable Product 3')]//*[@class='quantity-input']")

    def add_to_cart_BP3(self):
        self.driver.find_element(*Store.atc_bp3).click()
        sleep(5)

    def increase_BP3(self):
        self.driver.find_element(*Store.inc_bp3).click()
        sleep(2)

    def get_BP3_qty(self):
        return self.driver.find_element(*Store.bp3_qty).get_attribute('value')

    atc_ps1 = (By.XPATH, "//div[@class='product-card'][.//h2[@title='Physical Product 1']]//button[contains(., 'Add to cart')]")

    bn_ps1 = (By.XPATH, "//div[@class='product-card'][.//h2[@title='Physical Product 1']]//button[contains(., 'Buy now')]")

    ps1_price = (By.XPATH, "//div[@class='product-card'][.//h2[@title='Physical Product 1']]//*[contains(@class,'price')]")

    def add_to_cart_PS1(self):
        self.driver.find_element(*Store.atc_ps1).click()
        sleep(5)

    def buy_now_TT_ps1(self):
        self.driver.find_element(*Store.bn_tt_b2fss).click()
        sleep(20)

    def get_PS1_price(self):
        return self.driver.find_element(*Store.ps1_price).text.replace(" ","")


    ga_fp1 = (By.XPATH, "//*[@class='product-card'][contains(.,'Free Product 1')]//*[contains(text(),'Get Access')]")

    ga_fp1_spanish =   (By.XPATH, "//*[@class='product-card'][contains(.,'Free Product 1')]//*[contains(text(),'Obtener acceso')]")
    ga_fp1_italian =   (By.XPATH, "//*[@class='product-card'][contains(.,'Free Product 1')]//*[contains(text(),'Ottenere accesso')]")
    ga_fp1_french  =   (By.XPATH, "//*[@class='product-card'][contains(.,'Free Product 1')]//*[contains(text(),'Accéder')]")
    ga_fp1_german  =   (By.XPATH, "//*[@class='product-card'][contains(.,'Free Product 1')]//*[contains(text(),'Zugang erhalten')]")
    ga_fp1_port    =   (By.XPATH, "//*[@class='product-card'][contains(.,'Free Product 1')]//*[contains(text(),'Obter acesso')]")

    FP1 = (By.XPATH, "//*[@class='product-card'][contains(.,'Free Product 1')]//*[contains(@class,'title')]")

    def get_access_FP1(self):
        self.driver.find_element(*Store.ga_fp1).click()
        sleep(20)

    def get_access_FP1_spanish(self):
        self.driver.find_element(*Store.ga_fp1_spanish).click()
        sleep(20)

    def get_access_FP1_italian(self):
        self.driver.find_element(*Store.ga_fp1_italian).click()
        sleep(20)

    def get_access_FP1_french(self):
        self.driver.find_element(*Store.ga_fp1_french).click()
        sleep(20)

    def get_access_FP1_german(self):
        self.driver.find_element(*Store.ga_fp1_german).click()
        sleep(20)

    def get_access_FP1_port(self):
        self.driver.find_element(*Store.ga_fp1_port).click()
        sleep(20)

    def get_FP1(self):
        return self.driver.find_element(*Store.FP1).text

    def check_text_FP1_btn(self):
        text = self.driver.find_element(*Store.ga_fp1).text
        return text


    ga_fp2 = (By.XPATH, "//*[@class='product-card'][contains(.,'Free Product 2')]//*[contains(text(),'Get Access')]")

    FP2 = (By.XPATH, "//*[@class='product-card'][contains(.,'Free Product 2')]//*[contains(@class,'title')]")

    def get_access_FP2(self):
        self.driver.find_element(*Store.ga_fp2).click()
        sleep(15)

    def get_FP2(self):
        return self.driver.find_element(*Store.FP2).text

    ga_mb2rpr = (By.XPATH, "//*[@class='product-card'][contains(.,'Mosaic B2')]//*[contains(text(),'Get Access')]")

    MB2RPR = (By.XPATH, "//*[@class='product-card'][contains(.,'Mosaic B2')]//*[contains(@class,'title')]")

    def get_access_MB2RPR(self):
        self.go_to_page2()
        self.driver.find_element(*Store.ga_mb2rpr).click()
        sleep(15)

    def get_MB2RPR(self):
        return self.driver.find_element(*Store.MB2RPR).text



#EDS products
    bn_QML2 = (By.XPATH, "//*[@class='product-card'][contains(.,'Quick Minds Level 2')]//*[contains(text(),'Buy now')]")

    QML2 = (By.XPATH, "//*[@class='product-card'][contains(.,'Quick Minds Level 2')]//*[contains(@class,'title')]")

    def buy_now_QML2(self):
        self.driver.find_element(*Store.bn_QML2).click()
        sleep(15)

    def get_QML2(self):
        return self.driver.find_element(*Store.QML2).text



    def page_src(self):
        body = self.driver.find_element(By.TAG_NAME, 'body').text
        return body

    # -----------------------------------------------------------------------------------------------------------------
    # Pagination

    firstpage = (By.XPATH, "//*[@aria-label='Go to first page']")

    previouspage = (By.XPATH, "//*[@aria-label='Go to previous page']")


    page1 = (By.XPATH, "//*[text()='1']")
    page2 = (By.XPATH, "//*[text()='2']")
    page3 = (By.XPATH, "//*[text()='3']")
    page4 = (By.XPATH, "//*[text()='4']")


    nextpage = (By.XPATH, "//*[@aria-label='Go to next page']")

    lastpage = (By.XPATH, "//*[@aria-label='Go to last page']")

    def go_to_firstpage(self):
        self.driver.find_element(*Store.firstpage).click()
        sleep(5)


    def go_to_previouspage(self):
        self.driver.find_element(*Store.previouspage).click()
        sleep(5)

    def go_to_page1(self):
        self.driver.find_element(*Store.page1).click()
        sleep(5)

    def go_to_page2(self):
        self.driver.find_element(*Store.page2).click()
        sleep(8)

    def go_to_page3(self):
        self.driver.find_element(*Store.page3).click()
        sleep(8)

    def go_to_page4(self):
        self.driver.find_element(*Store.page4).click()
        sleep(5)

    def go_to_nextpage(self):
        self.driver.find_element(*Store.nextpage).click()
        sleep(5)

    def go_to_lastpage(self):
        self.driver.find_element(*Store.lastpage).click()
        sleep(5)


    pagination = (By.XPATH, "//ul[contains(@class, 'pagination')]")

    def get_pagination_displayed(self):
        return self.driver.find_element(*Store.pagination).is_displayed()

    productcard = (By.XPATH, "//div[@class='product-card']")

    def get_productcard(self):
        items = self.driver.find_elements(*Store.productcard)
        store_items = [item.text for item in items]
        return len(store_items)

    product_search = (By.XPATH, "//input[@placeholder='Search']")


    def get_aud_total_delcharge(self):
        def extract_price(currency_str):
            return float(currency_str.replace("AU $", "").replace(",", "").strip())

        total_value = sum(extract_price(price) for price in [self.get_aud_PS1_price(), f"AU ${self.AUD_del_charge}"])

        return f"AU ${total_value:.2f}"

    def get_aud_mixed_total_delcharge(self):
        def extract_price(currency_str):
            return float(currency_str.replace("AU $", "").replace(",", "").strip())

        total_value = sum(extract_price(price) for price in [self.get_aud_total_delcharge(), self.get_aud_TT_B2FSS_price()])

        return f"AU ${total_value:.2f}"



