# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestDangnhapcorrect():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_dangnhapcorrect(self):
    self.driver.get("https://shoptest.fun/login")
    self.driver.set_window_size(1552, 832)
    self.driver.find_element(By.LINK_TEXT, "Trang chủ").click()
    self.driver.find_element(By.CSS_SELECTOR, ".our-link li:nth-child(1) > a").click()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("huypanda2001@gmail.com")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("abcd1234")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
  
