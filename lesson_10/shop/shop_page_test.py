import allure

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from shopPage import ShopPage
from webdriver_manager.chrome import ChromeDriverManager


@allure.suite("Онлайн магазин")
@allure.epic("Онлайн магазин")
@allure.title("Добавляем товары в корзину и сравниваем итоговую цену")
def test_shop():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))    # noqa: E501

    with allure.step("Открываем браузер и сайт"):
        sh = ShopPage(browser)
    with allure.step("Выполняем авторизацию"):
        sh.auth()
    with allure.step("Добавляем товар в корзину"):
        sh.add_item()
    with allure.step("Вводим адрес доставки"):
        sh.delivery_address()
    with allure.step("Итоговая стоимость товаров"):
        tot = sh.total()
    with allure.step("Цена которая должна быть"):
        res = sh.result()

    with allure.step("Сравниваем цены"):
        assert tot == res

    with allure.step("Закрываем браузер"):
        browser.quit()