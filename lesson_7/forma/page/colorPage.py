from selenium.webdriver.common.by import By


class ColorPage:
    def __init__(self, browser):
        self.browser = browser

    def zip_color(self):
        self.browser.find_element(By.ID, 'zip-code').value_of_css_property("background-color")        # noqa: E501

    def zip_col(self):
        "rgba(248, 215, 218, 1)"

    def first_color(self):
        self.browser.find_element(By.ID, 'first-name').value_of_css_property("background-color")    # noqa: E501

    def first_col(self):
        "rgba(209, 231, 221, 1)"

    def last_color(self):
        self.browser.find_element(By.ID, 'last-name').value_of_css_property("background-color")      # noqa: E501

    def last_col(self):
        "rgba(209, 231, 221, 1)"

    def address_color(self):
        self.browser.find_element(By.ID, 'address').value_of_css_property("background-color")     # noqa: E501

    def address_col(self):
        "rgba(209, 231, 221, 1)"

    def city_color(self):
        self.browser.find_element(By.ID, 'city').value_of_css_property("background-color")           # noqa: E501

    def city_col(self):
        "rgba(209, 231, 221, 1)"

    def country_color(self):
        self.browser.find_element(By.ID, 'country').value_of_css_property("background-color")           # noqa: E501

    def country_col(self):
        "rgba(209, 231, 221, 1)"

    def e_mail_color(self):
        self.browser.find_element(By.ID, 'e-mail').value_of_css_property("background-color")       # noqa: E501

    def e_mail_col(self):
        "rgba(209, 231, 221, 1)"

    def phone_color(self):
        self.browser.find_element(By.ID, 'phone').value_of_css_property("background-color")         # noqa: E501

    def phone_col(self):
        "rgba(209, 231, 221, 1)"

    def job_color(self):
        self.browser.find_element(By.ID, 'job-position').value_of_css_property("background-color")             # noqa: E501

    def job_col(self):
        "rgba(209, 231, 221, 1)"

    def company_color(self):
        self.browser.find_element(By.ID, 'company').value_of_css_property("background-color")     # noqa: E501

    def company_col(self):
        "rgba(209, 231, 221, 1)"
