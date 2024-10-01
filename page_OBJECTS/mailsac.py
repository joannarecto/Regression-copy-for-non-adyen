from selenium.webdriver.common.by import By
from time import sleep

from page_OBJECTS.data import Data

class Mailsac:

    def __init__(self, driver):
        self.driver = driver

    username              = (By.XPATH, "//*[@name='username']")

    password              = (By.XPATH, "//*[@name='password']")

    signin                = (By.XPATH, "//*[@type='submit']")

    email                 = (By.XPATH, "//*[@class='choose-inbox']/input[1]")

    checkthemail          = (By.XPATH, "//*[contains(@class,'primary btn')]")

    verificationemail     = (By.XPATH, "//*[contains(@class,'inbox-subject') and contains(text(),'Verification')]")

    verificationcode      = (By.XPATH, "//*[contains(text(),'verification code')]//following::p")

    emailinfo             = (By.XPATH, "//*[contains(@class,'btn-info')]")

    verificationcodefield = (By.XPATH, "//*[contains(@id,'gigya-textbox')]")

    verify                = (By.XPATH, "//*[@value='Verify']")

    def input_username(self):

        i = Data(self.driver)

        return self.driver.find_element(*Mailsac.username).send_keys(i.mailsac_username)

    def input_password(self):

        i = Data(self.driver)

        return self.driver.find_element(*Mailsac.password).send_keys(i.mailsac_password)

    def click_signin(self):
        self.driver.find_element(*Mailsac.signin).click()
        sleep(10)

    def input_email(self):

        from page_OBJECTS.login import Login

        i = Login(self.driver)

        return self.driver.find_element(*Mailsac.email).send_keys(i.randomemailaddress)

    def click_checkthemail(self):
        self.driver.find_element(*Mailsac.checkthemail).click()
        sleep(10)

    def open_verificationemail(self):
        self.driver.find_element(*Mailsac.verificationemail).click()

    def go_to_emailinfo(self):
        self.driver.find_element(*Mailsac.emailinfo).click()
        sleep(5)

    def get_verificationcode(self):
        return self.driver.find_element(*Mailsac.verificationcode).text

    def input_verificationcode(self):
        return self.driver.find_element(*Mailsac.verificationcodefield)

    def click_verify(self):
        self.driver.find_element(*Mailsac.verify).click()
        sleep(25)

    def get_verification_code_and_verify_email(self):
        main_window = self.driver.window_handles[0]
        self.driver.execute_script("window.open('');")

        mailsac_window = self.driver.window_handles[1]
        self.driver.switch_to.window(mailsac_window)

        self.driver.get('https://mailsac.com/login')
        sleep(20)

        self.input_username()
        self.input_password()
        self.click_signin()
        self.input_email()
        self.click_checkthemail()
        self.open_verificationemail()
        self.go_to_emailinfo()

        info_window = self.driver.window_handles[2]
        self.driver.switch_to.window(info_window)

        verification_code = self.get_verificationcode()

        self.driver.switch_to.window(main_window)

        self.input_verificationcode().send_keys(verification_code)
        self.click_verify()




    def input_email2(self):

        from page_OBJECTS.prelogin import PreLogin

        i = PreLogin(self.driver)

        return self.driver.find_element(*Mailsac.email).send_keys(i.randomemailaddress2)

    def get_verification_code_and_verify_email2(self):
        main_window = self.driver.window_handles[0]
        self.driver.execute_script("window.open('');")

        mailsac_window = self.driver.window_handles[1]
        self.driver.switch_to.window(mailsac_window)

        self.driver.get('https://mailsac.com/login')
        sleep(20)

        self.input_username()
        self.input_password()
        self.click_signin()
        self.input_email2()
        self.click_checkthemail()
        self.open_verificationemail()
        self.go_to_emailinfo()

        info_window = self.driver.window_handles[2]
        self.driver.switch_to.window(info_window)

        verification_code = self.get_verificationcode()

        print(verification_code)

        # self.driver.switch_to.window(main_window)
        #
        # self.input_verificationcode().send_keys(verification_code)
        # self.click_verify()