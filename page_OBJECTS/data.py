from selenium.webdriver.common.by import By
from time import sleep

class Data:

    def __init__(self, driver):
        self.driver = driver

# --------------------------------------- Target market countries
#Exisitng user: email

    e_bra_emailaddress = 'bra@mailsac.com'
    e_can_emailaddress = 'can@mailsac.com'
    e_che_emailaddress = 'che@mailsac.com'
    e_esp_emailaddress = 'esp@mailsac.com'
    e_gbr_emailaddress = 'gbr@mailsac.com'
    e_ind_emailaddress = 'ind@mailsac.com'
    e_ita_emailaddress = 'ita@mailsac.com'
    e_mex_emailaddress = 'mex@mailsac.com'
    e_nld_emailaddress = 'nld@mailsac.com'
    e_phl_emailaddress = 'phl@mailsac.com'
    e_pol_emailaddress = 'pol@mailsac.com'
    e_prt_emailaddress = 'prt@mailsac.com'
    e_rus_emailaddress = 'rus@mailsac.com'
    e_usa_emailaddress = 'usa@mailsac.com'

    e_tur_emailaddress = 'tur@mailsac.com'


# Existing and Non-existing: password

    bra_password = 'Cambridge123!'
    can_password = 'Cambridge123!'
    che_password = 'Cambridge123!'
    esp_password = 'Cambridge123!'
    gbr_password = 'Cambridge123!'
    ind_password = 'Cambridge123!'
    ita_password = 'Cambridge123!'
    mex_password = 'Cambridge123!'
    nld_password = 'Cambridge123!'
    phl_password = 'Cambridge123!'
    pol_password = 'Cambridge123!'
    prt_password = 'Cambridge123!'
    rus_password = 'Cambridge123!'
    usa_password = 'Cambridge123!'

    tur_password = 'Cambridge123!'

# Non-existing: email

    n_bra_emailaddress = 'n_bra@mailsac.com'
    n_can_emailaddress = 'n_can@mailsac.com'
    n_che_emailaddress = 'n_che@mailsac.com'
    n_esp_emailaddress = 'n_esp@mailsac.com'
    n_gbr_emailaddress = 'n_gbr@mailsac.com'
    n_ind_emailaddress = 'n_ind@mailsac.com'
    n_ita_emailaddress = 'n_ita@mailsac.com'
    n_mex_emailaddress = 'n_mex@mailsac.com'
    n_nld_emailaddress = 'n_nld@mailsac.com'
    n_phl_emailaddress = 'n_phl@mailsac.com'
    n_pol_emailaddress = 'n_pol@mailsac.com'
    n_prt_emailaddress = 'n_prt@mailsac.com'
    n_rus_emailaddress = 'n_rus@mailsac.com'
    n_usa_emailaddress = 'n_usa@mailsac.com'

# --------------------------------------- Currency
# Existing user: email

    e_aud_emailaddress   = 'aud@mailsac.com'
    e_cad_emailaddress   = 'cad@mailsac.com'
    e_eur_emailaddress   = 'eur@mailsac.com'
    e_eur_c_emailaddress = 'eur_c@mailsac.com'
    e_eur_i_emailaddress = 'eur_i@mailsac.com'
    e_gbp_emailaddress   = 'gbp@mailsac.com'
    e_nzd_emailaddress   = 'nzd@mailsac.com'
    e_usd_emailaddress   = 'usd@mailsac.com'
    e_usd_e_emailaddress = 'usd_e@mailsac.com'
    e_usd_n_emailaddress = 'usd_n@mailsac.com'

# Existing and Non-existing user: password

    aud_password   = 'Cambridge123!'
    cad_password   = 'Cambridge123!'
    eur_password   = 'Cambridge123!'
    eur_c_password = 'Cambridge123!'
    eur_i_password = 'Cambridge123!'
    gbp_password   = 'Cambridge123!'
    nzd_password   = 'Cambridge123!'
    usd_password   = 'Cambridge123!'
    usd_e_password = 'Cambridge123!'
    usd_n_password = 'Cambridge123!'

# Non-existing user: email

    n_aud_emailaddress   = 'n_aud@mailsac.com'
    n_cad_emailaddress   = 'n_cad@mailsac.com'
    n_eur_emailaddress   = 'n_eur@mailsac.com'
    n_eur_c_emailaddress = 'n_eur_c@mailsac.com'
    n_eur_i_emailaddress = 'n_eur_i@mailsac.com'
    n_gbp_emailaddress   = 'n_gbp@mailsac.com'
    n_nzd_emailaddress   = 'n_nzd@mailsac.com'
    n_usd_emailaddress   = 'n_usd@mailsac.com'
    n_usd_e_emailaddress = 'n_usd_e@mailsac.com'
    n_usd_n_emailaddress = 'n_usd_n@mailsac.com'

    e_test_001_emailaddress = 'test_001@mailsac.com'
    e_test_002_emailaddress = 'test_002@mailsac.com'
    e_test_003_emailaddress = 'test_003@mailsac.com'
    e_test_004_emailaddress = 'test_004@mailsac.com'
    e_test_005_emailaddress = 'test_005@mailsac.com'
    e_test_006_emailaddress = 'test_006@mailsac.com'

    test_001_password = 'Cambridge123!'
    test_002_password = 'Cambridge123!'
    test_003_password = 'Cambridge123!'
    test_004_password = 'Cambridge123!'
    test_005_password = 'Cambridge123!'
    test_006_password = 'Cambridge123!'

    n_test_001_emailaddress = 'n_test_001@mailsac.com'
    n_test_002_emailaddress = 'n_test_002@mailsac.com'
    n_test_003_emailaddress = 'n_test_003@mailsac.com'
    n_test_004_emailaddress = 'n_test_004@mailsac.com'
    n_test_005_emailaddress = 'n_test_005@mailsac.com'
    n_test_006_emailaddress = 'n_test_006@mailsac.com'
    n_test_007_emailaddress = 'n_test_007@mailsac.com'
    n_test_008_emailaddress = 'n_test_008@mailsac.com'
    n_test_009_emailaddress = 'n_test_009@mailsac.com'
    n_test_010_emailaddress = 'n_test_010@mailsac.com'

    # --------------------------------------- Countries billing credentials

    bra_firstname           = 'Bra'
    bra_lastname            = 'Hull'
    bra_country             = 'Brazil'
    bra_billingaddressline1 = 'Test Address 1'
    bra_billingaddressline2 = 'Test Address 2'
    bra_city                = 'Test City'
    bra_state               = 'Acre'
    bra_postcode            = '12345678'

    can_firstname           = 'Can'
    can_lastname            = 'Jackinoff'
    can_country             = 'Canada'
    can_billingaddressline1 = 'Test Address 1'
    can_billingaddressline2 = 'Test Address 2'
    can_city                = 'Test City'
    can_state               = 'Quebec'
    can_postcode            = 'J0B 3E3'

    ind_firstname           = 'Ind'
    ind_lastname            = 'Torres'
    ind_country             = 'India'
    ind_billingaddressline1 = 'Test Address 1'
    ind_billingaddressline2 = 'Test Address 2'
    ind_city                = 'Test City'
    ind_state               = 'Jharkhand'
    ind_postcode            = '814112'

    ita_firstname           = 'Ita'
    ita_lastname            = 'Teats'
    ita_country             = 'Italy'
    ita_billingaddressline1 = 'Test Address 1'
    ita_billingaddressline2 = 'Test Address 2'
    ita_city                = 'Test City'
    ita_state               = 'Bologna'
    ita_postcode            = '40132'

    mex_firstname           = 'Mex'
    mex_lastname            = 'Liquin'
    mex_country             = 'Mexico'
    mex_billingaddressline1 = 'Test Address 1'
    mex_billingaddressline2 = 'Test Address 2'
    mex_city                = 'Test City'
    mex_state               = 'Michoacan'
    mex_postcode            = '60110'

    nld_firstname           = 'Nld'
    nld_lastname            = 'Jazz'
    nld_country             = 'Netherlands'
    nld_billingaddressline1 = 'Test Address 1'
    nld_billingaddressline2 = 'Test Address 2'
    nld_city                = 'Test City'
    nld_state               = 'Noord-Brabant'
    nld_postcode            = '5662 VN'

    phl_firstname           = 'Phl'
    phl_lastname            = 'Spencer'
    phl_country             = 'Philippines'
    phl_billingaddressline1 = 'Test Address 1'
    phl_billingaddressline2 = 'Test Address 2'
    phl_city                = 'Test City'
    phl_state               = 'Zamboanga Peninsula'
    phl_postcode            = '7000'

    pol_firstname           = 'Pol'
    pol_lastname            = 'Pants'
    pol_country             = 'Poland'
    pol_billingaddressline1 = 'Test Address 1'
    pol_billingaddressline2 = 'Test Address 2'
    pol_city                = 'Test City'
    pol_state               = 'Woj. Mazowieckie'
    pol_postcode            = '09-130'

    prt_firstname           = 'Prt'
    prt_lastname            = 'Tutchem'
    prt_country             = 'Portugal'
    prt_billingaddressline1 = 'Test Address 1'
    prt_billingaddressline2 = 'Test Address 2'
    prt_city                = 'Test City'
    prt_state               = 'Vila Real'
    prt_postcode            = '5400-189'

    rus_firstname           = 'Rus'
    rus_lastname            = 'Lott'
    rus_country             = 'Russian Federation'
    rus_billingaddressline1 = 'Test Address 1'
    rus_billingaddressline2 = 'Test Address 2'
    rus_city                = 'Test City'
    rus_state               = 'Центральный федеральный округ'
    rus_postcode            = '121596'

    esp_firstname           = 'Esp'
    esp_lastname            = 'Rect'
    esp_country             = 'Spain'
    esp_billingaddressline1 = 'Test Address 1'
    esp_billingaddressline2 = 'Test Address 2'
    esp_city                = 'Test City'
    esp_state               = 'Sevilla'
    esp_postcode            = '41004'

    che_firstname           = 'Che'
    che_lastname            = 'Nate'
    che_country             = 'Switzerland'
    che_billingaddressline1 = 'Test Address 1'
    che_billingaddressline2 = 'Test Address 2'
    che_city                = 'Test City'
    che_state               = 'Solothurn'
    che_postcode            = '2544'

    gbr_firstname           = 'Gbr'
    gbr_lastname            = 'Gurrer'
    gbr_country             = 'United Kingdom'
    gbr_billingaddressline1 = 'Test Address 1'
    gbr_billingaddressline2 = 'Test Address 2'
    gbr_city                = 'Test City'
    gbr_state               = 'County Armagh'
    gbr_postcode            = 'BT61 0BN'

    usa_firstname           = 'Usa'
    usa_lastname            = 'Cade'
    usa_country             = 'United States'
    usa_billingaddressline1 = 'Test Address 1'
    usa_billingaddressline2 = 'Test Address 2'
    usa_city                = 'Test City'
    usa_state               = 'New York'
    usa_postcode            = '12534-1719'

    #Special case specific for Türkiye (Manual input)

    tur_firstname           = 'Turk'
    tur_lastname            = 'Iye'
    tur_country             = 'Türkiye'
    tur_billingaddressline1 = 'M. Hıdıroğlu Sokak'
    tur_billingaddressline2 = 'Yeni'
    tur_city                = 'Bolvadin'
    tur_state               = 'Afyonkarahisar'
    tur_postcode            = '03302'

# ------------------------------------------------- PAYPAL

    paypal_emailaddress = 'test@gabriel.com'
    paypal_password     = '12345678'

# --------------------------------------- Currency billing credentials

    aud_firstname           = 'Aud'
    aud_lastname            = 'York'
    aud_country             = 'Australia'
    aud_billingaddressline1 = 'Test Address 1'
    aud_billingaddressline2 = 'Test Address 2'
    aud_city                = 'Test City'
    aud_state               = 'New South Wales'
    aud_postcode            = '2000'

    cad_firstname           = 'Cad'
    cad_lastname            = 'Prince'
    cad_country             = 'Canada'
    cad_billingaddressline1 = 'Test Address 1'
    cad_billingaddressline2 = 'Test Address 2'
    cad_city                = 'Test City'
    cad_state               = 'Ontario'
    cad_postcode            = 'M5V 2T6'

    eur_firstname           = 'Eur'
    eur_lastname            = 'Leblanc'
    eur_country             = 'Germany'
    eur_billingaddressline1 = 'Test Address 1'
    eur_billingaddressline2 = 'Test Address 2'
    eur_city                = 'Test City'
    eur_state               = 'Bavaria'
    eur_postcode            = '80331'

    eur_c_firstname           = 'EurC'
    eur_c_lastname            = 'Cade'
    eur_c_country             = 'Spain'
    eur_c_billingaddressline1 = 'Test Address 1'
    eur_c_billingaddressline2 = 'Test Address 2'
    eur_c_city                = 'Test City'
    eur_c_state               = 'Alicante'
    eur_c_postcode            = '03680'

    eur_i_firstname           = 'EurI'
    eur_i_lastname            = 'Lawson'
    eur_i_country             = 'Italy'
    eur_i_billingaddressline1 = 'Test Address 1'
    eur_i_billingaddressline2 = 'Test Address 2'
    eur_i_city                = 'Test City'
    eur_i_state               = 'Lazio'
    eur_i_postcode            = '00100'

    gbp_firstname           = 'GBP'
    gbp_lastname            = 'Chang'
    gbp_country             = 'United Kingdom'
    gbp_billingaddressline1 = 'Test Address 1'
    gbp_billingaddressline2 = 'Test Address 2'
    gbp_city                = 'Test City'
    gbp_state               = 'England'
    gbp_postcode            = 'SW1A 1AA'

    nzd_firstname           = 'Nzd'
    nzd_lastname            = 'Wood'
    nzd_country             = 'New Zealand'
    nzd_billingaddressline1 = 'Test Address 1'
    nzd_billingaddressline2 = 'Test Address 2'
    nzd_city                = 'Test City'
    nzd_state               = 'Auckland'
    nzd_postcode            = '1010'

    usd_firstname           = 'Usd'
    usd_lastname            = 'Bell'
    usd_country             = 'United States'
    usd_billingaddressline1 = 'Test Address 1'
    usd_billingaddressline2 = 'Test Address 2'
    usd_city                = 'Test City'
    usd_state               = 'California'
    usd_postcode            = '90210'

    usd_e_firstname           = 'UsdE'
    usd_e_lastname            = 'White'
    usd_e_country             = 'United States'
    usd_e_billingaddressline1 = 'Test Address 1'
    usd_e_billingaddressline2 = 'Test Address 2'
    usd_e_city                = 'Test City'
    usd_e_state               = 'New York'
    usd_e_postcode            = '10001'

    usd_n_firstname           = 'UsaN'
    usd_n_lastname            = 'Pitts'
    usd_n_country             = 'United States'
    usd_n_billingaddressline1 = 'Test Address 1'
    usd_n_billingaddressline2 = 'Test Address 2'
    usd_n_city                = 'Test City'
    usd_n_state               = 'Texas'
    usd_n_postcode            = '77001'


    test_firstname           = 'gab'
    test_lastname            = 'test'
    test_country             = 'United Kingdom'
    test_billingaddressline1 = 'Test Address 1'
    test_billingaddressline2 = 'Test Address 2'
    test_city                = 'Test City'
    test_state               = 'England'
    test_postcode            = 'SW1A 1AA'

    #-------------------------------------------------------------------------------------------------------------------

    legal_title         = 'Legal | Cambridge University Press & Assessment'

    privacynotice_title = 'Legal - Privacy | Cambridge University Press & Assessment'

    accessibility_title = 'Accessibility | Cambridge University Press & Assessment'

    help_title          = 'Contact Us'

    #-------------------------------------------------------------------------------------------------------------------
