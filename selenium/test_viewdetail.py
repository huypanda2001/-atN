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

class TestViewdetail():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_viewdetail(self):
    self.driver.get("https://shoptest.fun/home")
    self.driver.set_window_size(1552, 832)
    self.driver.execute_script("window.scrollBy(0, 600)")
    self.driver.find_element(By.LINK_TEXT, "Áo hoodie").click()
    element = self.driver.find_element(By.LINK_TEXT, "Giày thể thao")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.LINK_TEXT, "Giày thể thao")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.execute_script("window.scrollBy(0, 500)")
    assert self.driver.find_element(By.CSS_SELECTOR, ".single-product-details > h2").text == "Áo hoodie"
  
