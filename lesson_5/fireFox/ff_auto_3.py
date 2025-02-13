from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))   # noqa: E501

driver.get("http://the-internet.herokuapp.com/login")
search_input = driver.find_element(By.CSS_SELECTOR, "#username")
search_input.send_keys("tomsmith")

search_input = driver.find_element(By.ID, "password")
search_input.send_keys("SuperSecretPassword!")

search_input = driver.find_element(By.CSS_SELECTOR, ".radius")
search_input.click()
