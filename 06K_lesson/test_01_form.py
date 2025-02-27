import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))    # noqa: E501

browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")         # noqa: E501

f_name = browser.find_element(By.CSS_SELECTOR, '[name="first-name"]')
f_name.send_keys("Иван")

l_name = browser.find_element(By.CSS_SELECTOR, '[name="last-name"]')
l_name.send_keys("Петров")

address = browser.find_element(By.CSS_SELECTOR, '[name="address"]')
address.send_keys("Ленина, 55-3")

city = browser.find_element(By.CSS_SELECTOR, '[name="city"]')
city.send_keys("Москва")

country = browser.find_element(By.CSS_SELECTOR, '[name="country"]')
country.send_keys("Россия")

e_mail = browser.find_element(By.CSS_SELECTOR, '[name="e-mail"]')
e_mail.send_keys("test@skypro.com")

phone = browser.find_element(By.CSS_SELECTOR, '[name="phone"]')
phone.send_keys("+7985899998787")

job = browser.find_element(By.CSS_SELECTOR, '[name="job-position"]')
job.send_keys("QA")

company = browser.find_element(By.CSS_SELECTOR, '[name="company"]')
company.send_keys("SkyPro")

browser.find_element(By.CSS_SELECTOR, '[class="btn btn-outline-primary mt-3"]').click()              # noqa: E501

zip_color = browser.find_element(By.ID, 'zip-code').value_of_css_property("background-color")        # noqa: E501

first_color = browser.find_element(By.ID, 'first-name').value_of_css_property("background-color")    # noqa: E501
last_color = browser.find_element(By.ID, 'last-name').value_of_css_property("background-color")      # noqa: E501
address_color = browser.find_element(By.ID, 'address').value_of_css_property("background-color")     # noqa: E501
city_color = browser.find_element(By.ID, 'city').value_of_css_property("background-color")           # noqa: E501
country_color = browser.find_element(By.ID, 'country').value_of_css_property("background-color")           # noqa: E501
e_mail_color = browser.find_element(By.ID, 'e-mail').value_of_css_property("background-color")       # noqa: E501
phone_color = browser.find_element(By.ID, 'phone').value_of_css_property("background-color")         # noqa: E501
job_color = browser.find_element(By.ID, 'job-position').value_of_css_property("background-color")             # noqa: E501
company_color = browser.find_element(By.ID, 'company').value_of_css_property("background-color")     # noqa: E501

browser.quit()


@pytest.mark.filterwarnings
def test_zip_color():
    assert zip_color == "rgba(248, 215, 218, 1)"


def test_first_color():
    assert first_color == "rgba(209, 231, 221, 1)"


def test_last_color():
    assert last_color == "rgba(209, 231, 221, 1)"


def test_addres_color():
    assert address_color == "rgba(209, 231, 221, 1)"


def test_city_color():
    assert city_color == "rgba(209, 231, 221, 1)"


def test_country_color():
    assert country_color == "rgba(209, 231, 221, 1)"


def test_e_mail_color():
    assert e_mail_color == "rgba(209, 231, 221, 1)"


def test_phone_color():
    assert phone_color == "rgba(209, 231, 221, 1)"


def test_job_color():
    assert job_color == "rgba(209, 231, 221, 1)"


def test_company_color():
    assert company_color == "rgba(209, 231, 221, 1)"
