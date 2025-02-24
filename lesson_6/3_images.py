from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # noqa: E501

browser.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")  # noqa: E501

waitr = WebDriverWait(browser, 40)
waitr.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#text"), "Done!")
)

award = browser.find_element(By.CSS_SELECTOR, "#award")
src = award.get_attribute("src")

print(src)
