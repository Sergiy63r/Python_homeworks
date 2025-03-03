import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))    # noqa: E501
browser.implicitly_wait(10)

browser.get("https://www.saucedemo.com/")

browser.find_element(By.ID, 'user-name').send_keys("standard_user")
browser.find_element(By.ID, 'password').send_keys("secret_sauce")
browser.find_element(By.ID, 'login-button').click()

browser.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
browser.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
browser.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()

browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()
browser.find_element(By.ID, 'checkout').click()

browser.find_element(By.ID, 'first-name').send_keys("Сергей")
browser.find_element(By.ID, 'last-name').send_keys("Максимов")
browser.find_element(By.ID, 'postal-code').send_keys("445000")
browser.find_element(By.ID, 'continue').click()

total = browser.find_element(By.CSS_SELECTOR, '[data-test="total-label"]').text

browser.quit()


@pytest.mark.filterwarnings
def test_total():
    assert total == "Total: $58.29"
