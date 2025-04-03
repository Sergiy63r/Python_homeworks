import allure

from calcPage import CalcPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@allure.suite("Работа с калькулятором")
@allure.epic("Калькулятор")
@allure.title("Тест калькулятора")
def test_calc():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))    # noqa: E501

    with allure.step("Открываем браузер и сайт с калькулятором"):
        calc = CalcPage(browser)
    with allure.step("Выставляем время(сек)"):
        calc.delay("45")
    with allure.step("Производим сложение и выводим результат"):
        ca = calc.calc()
    with allure.step("Число"):
        an = calc.answer()
    with allure.step("Сравниваем результат с нашим числом"):
        assert ca == an
    with allure.step("Закрываем браузер"):
        browser.quit()
