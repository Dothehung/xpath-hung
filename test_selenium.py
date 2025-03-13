from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Cấu hình ChromeDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Xóa dòng này nếu muốn thấy trình duyệt mở lên

# Đường dẫn đến ChromeDriver
service = Service(executable_path="D:/kiemthuphanmem/chromedriver-win64/chromedriver.exe")

# Khởi chạy trình duyệt Chrome
driver = webdriver.Chrome(service=service, options=chrome_options)

# Mở trang Google và in ra tiêu đề trang
driver.get("https://www.google.com")
print("Tiêu đề trang:", driver.title)

# Đóng trình duyệt
driver.quit()