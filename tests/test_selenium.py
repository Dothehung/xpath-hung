from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Cập nhật đường dẫn đến chromedriver.exe
chrome_driver_path = r"D:\kiem thu phan mem\b1\chromedriver.exe"
service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com")

print("Chrome đã mở thành công!")
driver.quit()python D:\kiem thu phan mem\b1\test_selenium.py # type: ignore