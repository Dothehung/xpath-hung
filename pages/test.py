import unittest
import time
import configparser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser_setup import BrowserSetup

class GD22BTest(unittest.TestCase):
    def setUp(self):
        # Đọc file cấu hình
        config = configparser.ConfigParser()
        config.read('config.ini')

        # In các section và kiểm tra xem phần 'app' có tồn tại không
        print(config.sections())  # Debugging line

        # Lấy URL từ file config.ini
        self.login_url = config['app']['login_url']

        # Khởi động trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.login_url)

    def test_add_new_data_succesfully(self):
        """Kiểm thử nhập dữ liệu thành công"""
        
        # Bước 1: Nhấn nút "Edit" để chỉnh sửa dữ liệu
        btnEdit = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='editRecordButton']"))
        )
        btnEdit.click()

        # Bước 2: Nhập thông tin vào các ô
        self.driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("Do")
        self.driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys("Hung")
        self.driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("Hung99246@donga.edu.vn")
        self.driver.find_element(By.XPATH, "//input[@id='age']").send_keys("21")
        self.driver.find_element(By.XPATH, "//input[@id='salary']").send_keys("300000000")
        self.driver.find_element(By.XPATH, "//input[@id='department']").send_keys("Graphic Design")

        # Bước 3: Nhấn nút "Submit" để lưu dữ liệu
        btnSubmit = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='submit']"))
        )
        btnSubmit.click()

        # Bước 4: Kiểm tra xem dữ liệu có được lưu thành công không
        table = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='rt-table']"))
        )
        assert "hung99246@donga.edu.vn" in table.text
        assert "Graphic Design" in table.text

    def tearDown(self):
        """Đóng trình duyệt sau khi kiểm thử xong"""
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()