import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@allure.epic("Калькулятор")
class CalcPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")    # noqa: E501

    @allure.step("Выставляем время в секундах {term}")
    def delay(self, term: int):
        """
           Выставляем время в секундах,
           за которое калькулятор должен выполнить операцию
        """
        self.browser.find_element(By.ID, 'delay').clear()
        self.browser.find_element(By.ID, 'delay').send_keys(term)

    @allure.step("Складываются числа и выводится результат")
    def calc(self) -> int:
        """
           Проиcходит сложение чисел и вывода результата
        """
        self.browser.find_element(By.XPATH, "//span[text()='7']").click()
        self.browser.find_element(By.XPATH, "//span[text()='+']").click()
        self.browser.find_element(By.XPATH, "//span[text()='8']").click()
        self.browser.find_element(By.XPATH, "//span[text()='=']").click()

        wait = WebDriverWait(self.browser, 50)
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[class="screen"]'), "1")      # noqa: E501
        )
        self.browser.find_element(By.CSS_SELECTOR, '[class="screen"]').text

    @allure.step("Число для сравнения результата")
    def answer(self):
        int(15)
