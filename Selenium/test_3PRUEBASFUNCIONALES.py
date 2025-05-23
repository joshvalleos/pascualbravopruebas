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

class Test3PRUEBASFUNCIONALES():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_3PRUEBASFUNCIONALES(self):
    self.driver.get("http://localhost:8000/?post_type=product")
    self.driver.set_window_size(1015, 799)
    self.driver.find_element(By.CSS_SELECTOR, ".wp-block-button__link > span").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".wc-block-mini-cart__button")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".wc-block-mini-cart__icon").click()
    WebDriverWait(self.driver, 300).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".wc-block-cart-item__remove-link")))
    self.driver.find_element(By.CSS_SELECTOR, ".wc-block-cart-item__remove-link").click()
  
