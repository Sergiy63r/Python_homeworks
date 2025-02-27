import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))    # noqa: E501

browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")    # noqa: E501

browser.find_element(By.ID, 'delay').clear()
times = browser.find_element(By.ID, 'delay')
times.send_keys("45")

browser.find_element(By.XPATH, "//span[text()='7']").click()
browser.find_element(By.XPATH, "//span[text()='+']").click()
browser.find_element(By.XPATH, "//span[text()='8']").click()
browser.find_element(By.XPATH, "//span[text()='=']").click()

wait = WebDriverWait(browser, 50)
wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR,
                                      '[class="screen"]'), "1")
)

answer = browser.find_element(By.CSS_SELECTOR, '[class="screen"]').text

browser.quit()


@pytest.mark.filterwarnings
def test_answer():
    assert answer == "15"
