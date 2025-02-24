from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # noqa: E501
browser.implicitly_wait(20)

browser.get("http://uitestingplayground.com/ajax")

browser.find_element(By.CSS_SELECTOR, '#ajaxButton').click()

content = browser.find_element(By.CSS_SELECTOR, "#content")
txt = content.find_element(By.CSS_SELECTOR, '.bg-success').text
print(txt)

browser.quit()
