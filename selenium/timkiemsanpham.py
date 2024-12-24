from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
# Mở trang web chứa form tìm kiếm
driver.get("https://shoptest.fun/product-all")
# Phóng to cửa sổ trình duyệt để đảm bảo tất cả các phần tử có thể tương tác
driver.maximize_window()
# Nhập từ khóa từ bàn phím
search_query = input("Nhập thông tin bạn muốn tìm kiếm: ")
# Tìm ô nhập liệu tìm kiếm và nhập từ khóa
search_box = driver.find_element(By.XPATH, '//*[@id="bodycontent"]/div[1]/div[4]/div/div/div[1]/div/form/input')  # Thay đổi selector nếu cần
search_box.send_keys(search_query)
# Nhấn Enter để thực hiện tìm kiếm
search_box.send_keys(Keys.RETURN)
# Đợi kết quả tìm kiếm
time.sleep(10)  # Điều chỉnh thời gian chờ nếu cần
# Đóng trình duyệt
driver.quit()