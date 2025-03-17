
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalcPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")    # noqa: E501

    def delay(self, term):
        self.browser.find_element(By.ID, 'delay').clear()
        self.browser.find_element(By.ID, 'delay').send_keys(term)

    def calc(self):
        self.browser.find_element(By.XPATH, "//span[text()='7']").click()
        self.browser.find_element(By.XPATH, "//span[text()='+']").click()
        self.browser.find_element(By.XPATH, "//span[text()='8']").click()
        self.browser.find_element(By.XPATH, "//span[text()='=']").click()

        wait = WebDriverWait(self.browser, 50)
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[class="screen"]'), "1")      # noqa: E501
        )
        self.browser.find_element(By.CSS_SELECTOR, '[class="screen"]').text

    def answer(self):
        int(15)
