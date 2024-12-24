from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 
driver = webdriver.Chrome()
uname=input("Nhập name: ")
uemail=input("Nhập email: ")
upass=input("Nhập password:")
ufname=input("Nhập full name:")
uaddress=input("Nhập address: ")
uphone=input("Nhập phone: ")
driver.get("https://shoptest.fun/register")
driver.maximize_window()
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div[1]/div[2]/div[2]/ul/li[2]/a").click()
driver.find_element(By.XPATH,value="/html/body/div[1]/div[3]/div/form/div/div[1]/div[1]/input").send_keys(uname)
driver.find_element(By.XPATH,value="/html/body/div[1]/div[3]/div/form/div/div[1]/div[2]/input").send_keys(uemail)
driver.find_element(By.XPATH,value="/html/body/div[1]/div[3]/div/form/div/div[1]/div[3]/input").send_keys(upass)
driver.find_element(By.XPATH,value="/html/body/div[1]/div[3]/div/form/div/div[1]/div[4]/input").send_keys(upass)
driver.find_element(By.XPATH,value="/html/body/div[1]/div[3]/div/form/div/div[2]/div[1]/input").send_keys(ufname)
driver.find_element(By.XPATH,value="/html/body/div[1]/div[3]/div/form/div/div[2]/div[2]/input").send_keys(uaddress)
driver.find_element(By.XPATH,value="/html/body/div[1]/div[3]/div/form/div/div[2]/div[3]/input").send_keys(uphone)
# Click nút đăng ký sau khi đã kiểm tra
driver.find_element(By.XPATH,value="/html/body/div[1]/div[3]/div/form/div/div[2]/div[5]/button").click()
# Dừng lại 15 giây để kiểm tra thông tin
time.sleep(15)