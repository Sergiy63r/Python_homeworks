import allure

from selenium.webdriver.common.by import By


class ShopPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://www.saucedemo.com/")
        self.browser.implicitly_wait(10)

    def auth(self):
        with allure.step("user_name - standard_user"):
            self.browser.find_element(By.ID, 'user-name').send_keys("standard_user")     # noqa: E501
        with allure.step("passwor - secret_sauce"):
            self.browser.find_element(By.ID, 'password').send_keys("secret_sauce")      # noqa: E501
        self.browser.find_element(By.ID, 'login-button').click()

    def add_item(self):
        self.browser.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()    # noqa: E501
        self.browser.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()    # noqa: E501
        self.browser.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()       # noqa: E501

        self.browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()       # noqa: E501
        self.browser.find_element(By.ID, 'checkout').click()

    def delivery_address(self):
        self.browser.find_element(By.ID, 'first-name').send_keys("Сергей")
        self.browser.find_element(By.ID, 'last-name').send_keys("Максимов")
        self.browser.find_element(By.ID, 'postal-code').send_keys("445000")
        self.browser.find_element(By.ID, 'continue').click()

    def total(self) -> str:
        self.browser.find_element(By.CSS_SELECTOR, '[data-test="total-label"]').text     # noqa: E501

    def result(self):
        "Total: $58.29"
