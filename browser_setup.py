from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def setup_browser():
    """Thiết lập trình duyệt Chrome với Selenium"""
    service = Service(ChromeDriverManager().install())  # Tự động tải ChromeDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Mở trình duyệt ở chế độ full màn hình
    options.add_argument("--disable-blink-features=AutomationControlled")  # Tránh bị phát hiện tự động
    driver = webdriver.Chrome(service=service, options=options)
    return driver

if __name__ == "__main__":
    driver = setup_browser()
    driver.get("https://www.google.com")  # Kiểm tra mở trình duyệt
