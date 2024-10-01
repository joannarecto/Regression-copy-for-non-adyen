from selenium.webdriver.common.by import By



class FailOrderStatus:

    def __init__(self, driver):
        self.driver = driver


    fail_subheader = (By.XPATH, "//h1[@class='message-text']")

    def fail_subheader_msg(self):
        text = self.driver.find_element(*FailOrderStatus.fail_subheader).text
        return text


    fail_body = (By.XPATH, "//p[@class='mb-4']")

    def fail_body_msg(self):
        text = self.driver.find_element(*FailOrderStatus.fail_body).text
        return text

