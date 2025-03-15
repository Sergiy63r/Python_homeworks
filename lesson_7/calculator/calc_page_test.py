from calcPage import CalcPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_calc():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))    # noqa: E501

    calc = CalcPage(browser)
    calc.delay("45")
    ca = calc.calc()
    an = calc.answer()

    assert ca == an
