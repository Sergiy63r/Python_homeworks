import allure

from page.colorPage import ColorPage
from page.data_typesPage import DataTypesPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@allure.suite("Работа с формой")
@allure.epic("Форма")
@allure.title("Форма для заполнения данных")
def test_form():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))    # noqa: E501

    with allure.step("Открываем браузер и сайт с формой"):
        forma = DataTypesPage(browser)

    with allure.step("Заполняем форму и переходим дальше"):
        forma.first_name("Иван")
        forma.last_name("Петров")
        forma.address("Ленина, 55-3")
        forma.city("Москва")
        forma.country("Россия")
        forma.e_mail("test@skypro.com")
        forma.phone("+7985899998787")
        forma.job("QA")
        forma.company("SkyPro")
        forma.clik()

    with allure.step("Запрашиваем цвета ячеек"):
        color = ColorPage(browser)
        with allure.step("Цвета ячеек запрошенные с DevTool"):
            zip = color.zip_color()
            first = color.first_color()
            last = color.last_color()
            address = color.address_color()
            city = color.city_color()
            country = color.country_color()
            e_mail = color.e_mail_color()
            phone = color.phone_color()
            job = color.job_color()
            company = color.company_color()
        with allure.step("Цвета для сравнения ячеек запрошенных из DevTool"):
            zip_check = color.zip_col()
            first_check = color.first_col()
            last_check = color.last_col()
            address_check = color.address_col()
            city_check = color.city_col()
            country_check = color.country_col()
            e_mail_check = color.e_mail_col()
            phone_check = color.phone_col()
            job_check = color.job_col()
            company_check = color.company_col()

    with allure.step("Сравниваем цвета ячеек с заданными цветами"):
        assert zip == zip_check
        assert first == first_check
        assert last == last_check
        assert address == address_check
        assert city == city_check
        assert country == country_check
        assert e_mail == e_mail_check
        assert phone == phone_check
        assert job == job_check
        assert company == company_check

    with allure.step("Закрываем браузер"):
        browser.quit()
