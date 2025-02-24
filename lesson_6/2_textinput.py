from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # noqa: E501

browser.get("http://uitestingplayground.com/textinput")

input = browser.find_element(By.CSS_SELECTOR, '#newButtonName')

input.send_keys("SkyPro")
browser.find_element(By.CSS_SELECTOR, "#updatingButton").click()

button = browser.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(button)
