import allure

from selenium.webdriver.common.by import By


class DataTypesPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")                       # noqa: E501
        self.browser.maximize_window()

    @allure.step("Имя - {term}")
    def first_name(self, term: str):
        self.browser.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys(term)                         # noqa: E501

    @allure.step("Фамилия - {term}")
    def last_name(self, term: str):
        self.browser.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys(term)                         # noqa: E501

    @allure.step("Адрес {term}")
    def address(self, term: str):
        self.browser.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys(term)                          # noqa: E501

    @allure.step("Город - {term}")
    def city(self, term: str):
        self.browser.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys(term)                              # noqa: E501

    @allure.step("Страна - {term}")
    def country(self, term: str):
        self.browser.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys(term)                           # noqa: E501

    @allure.step("Емайл - {term}")
    def e_mail(self, term: str):
        self.browser.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys(term)                            # noqa: E501

    @allure.step("Телефон - {term}")
    def phone(self, term: int):
        """
            Вводим номер с '+' и что бы он отобразился в поле
            номер запечатываем в ковычки
        """
        self.browser.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys(term)                             # noqa: E501

    @allure.step("Должность - {term}")
    def job(self, term: str):
        self.browser.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys(term)                      # noqa: E501

    @allure.step("Компания - {term}")
    def company(self, term: str):
        self.browser.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys(term)                           # noqa: E501

    def clik(self):
        self.browser.find_element(By.CSS_SELECTOR, '[class="btn btn-outline-primary mt-3"]').click()             # noqa: E501
