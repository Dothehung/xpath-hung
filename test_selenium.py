from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Đặt đường dẫn đến ChromeDriver - dùng raw string để tránh lỗi với các dấu cách và ký tự đặc biệt
chrome_driver_path = r"D:\kiem thu phan mem\b1\chromedriver.exe"

# Tạo service cho ChromeDriver
service = Service(chrome_driver_path)

# Khởi tạo WebDriver với service đã cấu hình
driver = webdriver.Chrome(service=service)

# Mở trang Google
driver.get("https://www.google.com")

# In tiêu đề trang ra console
print("Chrome đã mở thành công! Tiêu đề trang:", driver.title)

# Đợi 5 giây để xem trang
time.sleep(5)

# Đóng trình duyệt
driver.quit()