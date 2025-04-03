import allure

from selenium.webdriver.common.by import By


class ColorPage:
    def __init__(self, browser):
        self.browser = browser

    @allure.step("Цвет ячейки zip-code")
    def zip_color(self) -> int:
        self.browser.find_element(By.ID, 'zip-code').value_of_css_property("background-color")        # noqa: E501

    @allure.step("Цвет для сравнения ячейки zip-code")
    def zip_col(self):
        "rgba(248, 215, 218, 1)"

    @allure.step("Цвет ячейки first-name")
    def first_color(self) -> int:
        self.browser.find_element(By.ID, 'first-name').value_of_css_property("background-color")    # noqa: E501

    @allure.step("Цвет для сравнения ячейки first-name")
    def first_col(self):
        "rgba(209, 231, 221, 1)"

    @allure.step("Цвет ячейки last-name")
    def last_color(self) -> int:
        self.browser.find_element(By.ID, 'last-name').value_of_css_property("background-color")      # noqa: E501

    @allure.step("Цвет для сравнения ячейки last-name")
    def last_col(self):
        "rgba(209, 231, 221, 1)"

    @allure.step("Цвет ячейки address")
    def address_color(self) -> int:
        self.browser.find_element(By.ID, 'address').value_of_css_property("background-color")     # noqa: E501

    @allure.step("Цвет для сравнения ячейки address")
    def address_col(self):
        "rgba(209, 231, 221, 1)"

    @allure.step("Цвет ячейки city")
    def city_color(self) -> int:
        self.browser.find_element(By.ID, 'city').value_of_css_property("background-color")           # noqa: E501

    @allure.step("Цвет для сравнения ячейки city")
    def city_col(self):
        "rgba(209, 231, 221, 1)"

    @allure.step("Цвет ячейки country")
    def country_color(self) -> int:
        self.browser.find_element(By.ID, 'country').value_of_css_property("background-color")           # noqa: E501

    @allure.step("Цвет для сравнения ячейки contry")
    def country_col(self):
        "rgba(209, 231, 221, 1)"

    @allure.step("Цвет для сравнения ячейки e-mail")
    def e_mail_color(self) -> int:
        self.browser.find_element(By.ID, 'e-mail').value_of_css_property("background-color")       # noqa: E501

    @allure.step("Цвет для сравнения ячейки e-mail")
    def e_mail_col(self):
        "rgba(209, 231, 221, 1)"

    @allure.step("Цвет ячейки phone")
    def phone_color(self) -> int:
        self.browser.find_element(By.ID, 'phone').value_of_css_property("background-color")         # noqa: E501

    @allure.step("Цвет для сравнения ячейки phone")
    def phone_col(self):
        "rgba(209, 231, 221, 1)"

    @allure.step("Цвет ячейки job")
    def job_color(self) -> int:
        self.browser.find_element(By.ID, 'job-position').value_of_css_property("background-color")             # noqa: E501

    @allure.step("Цвет для сравнения ячейки job")
    def job_col(self):
        "rgba(209, 231, 221, 1)"

    @allure.step("Цвет ячейки company")
    def company_color(self) -> int:
        self.browser.find_element(By.ID, 'company').value_of_css_property("background-color")     # noqa: E501

    @allure.step("Цвет для сравнения ячейки company")
    def company_col(self):
        "rgba(209, 231, 221, 1)"
