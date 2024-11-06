from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

        # Xác định các phần tử trên trang đăng ký
        self.email_field = (By.XPATH, "//input[@name='email']")
        self.password_field = (By.XPATH, "//input[@name='password']")
        self.name_field = (By.XPATH, "//input[@name='name']")
        self.register_button = (By.XPATH, "//button[@type='submit' and contains(text(), 'Register')]")
    
    def enterEmailField(self, value):
        self.driver.find_element(*self.email_field).send_keys(value)

    def enterPasswordField(self, value):
        self.driver.find_element(*self.password_field).send_keys(value)

    def enterNameField(self, value):
        self.driver.find_element(*self.name_field).send_keys(value)

    def clickRegisterButton(self):
        self.driver.find_element(*self.register_button).click()
