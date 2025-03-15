from selenium.webdriver.common.by import By


class DataTypesPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")                       # noqa: E501
        self.browser.maximize_window()

    def first_name(self, term):
        self.browser.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys(term)                         # noqa: E501

    def last_name(self, term):
        self.browser.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys(term)                         # noqa: E501

    def address(self, term):
        self.browser.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys(term)                          # noqa: E501

    def city(self, term):
        self.browser.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys(term)                              # noqa: E501

    def country(self, term):
        self.browser.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys(term)                           # noqa: E501

    def e_mail(self, term):
        self.browser.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys(term)                            # noqa: E501

    def phone(self, term):
        self.browser.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys(term)                             # noqa: E501

    def job(self, term):
        self.browser.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys(term)                      # noqa: E501

    def company(self, term):
        self.browser.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys(term)                           # noqa: E501

    def clik(self):
        self.browser.find_element(By.CSS_SELECTOR, '[class="btn btn-outline-primary mt-3"]').click()             # noqa: E501
