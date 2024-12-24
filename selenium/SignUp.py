from selenium import webdriver
from selenium.webdriver.common.by import By
# Khởi tạo WebDriver cho Chrome
driver = webdriver.Chrome()

# Mở trang web
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2FAdmin")

# Nhập thông tin đăng nhập
email = input("Nhập email: ")
password = input("Nhập password: ")

# Điền thông tin vào trường Email và Password
driver.find_element(By.ID, "Email").send_keys(email)
driver.find_element(By.ID, "Password").send_keys(password)

# Click nút "Log in"
driver.find_element(By.XPATH, "//button[text()='Log in']").click()

# Kiểm tra xem đăng nhập thành công hay không (có thể thay đổi dựa trên trang web của bạn)
if "logout" in driver.current_url.lower():
    print("Đăng nhập thành công!")
else:
    print("Đăng nhập thất bại!")

# Đóng trình duyệt sau khi hoàn thành test
driver.quit()
