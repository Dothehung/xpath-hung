from selenium import webdriver
import configparser

class BrowserSetup:
    @staticmethod
    def get_driver():
        # Đọc cấu hình từ file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')
        
        # Lấy đường dẫn chromedriver từ cấu hình
        driver_path = config['webdriver']['driver_path']
        
        # Khởi tạo và trả về đối tượng driver
        driver = webdriver.Chrome(executable_path=driver_path)
        return driver