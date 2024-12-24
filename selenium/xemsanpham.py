import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
# Mở trang web chứa form tìm kiếm
driver.get("http://localhost/trinnie_store/public/home")
# Tối đa hóa cửa sổ trình duyệt (nếu cần)
driver.maximize_window()
hoodie_link = driver.find_element(By.LINK_TEXT, 'Áo hoodie')
hoodie_link.click()

# Chờ đợi cho đến khi trang sản phẩm được tải
time.sleep(10)