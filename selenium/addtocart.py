import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://shoptest.fun/product-detail?id=21")
driver.maximize_window()

add_to_cart_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "div-cart"))
)
add_to_cart_button.click()
# Chờ đợi cho đến khi trang sản phẩm được tải
time.sleep(15)
#Đóng trình duyệt
driver.quit()

