from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from shopPage import ShopPage
from webdriver_manager.chrome import ChromeDriverManager


def test_shop():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))    # noqa: E501

    sh = ShopPage(browser)
    sh.auth()
    sh.add_item()
    sh.delivery_address()
    tot = sh.total()
    res = sh.result()
    browser.quit()

    assert tot == res
