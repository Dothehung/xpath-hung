from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Đợi tối đa 10 giây

    def get_password_field(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))

    def get_confirm_password_field(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='confirmPassword']")))

    def get_register_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))