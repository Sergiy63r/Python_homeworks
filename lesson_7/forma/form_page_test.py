from page.colorPage import ColorPage
from page.data_typesPage import DataTypesPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_form():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))    # noqa: E501

    forma = DataTypesPage(browser)
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

    color = ColorPage(browser)
    zip = color.zip_color()
    zip_check = color.zip_col()

    first = color.first_color()
    first_check = color.first_col()

    last = color.last_color()
    last_check = color.last_col()

    address = color.address_color()
    address_check = color.address_col()

    city = color.city_color()
    city_check = color.city_col()

    country = color.country_color()
    country_check = color.country_col()

    e_mail = color.e_mail_color()
    e_mail_check = color.e_mail_col()

    phone = color.phone_color()
    phone_check = color.phone_col()

    job = color.job_color()
    job_check = color.job_col()

    company = color.company_color()
    company_check = color.company_col()

    browser.quit()

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
