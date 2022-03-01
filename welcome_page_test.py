from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_welcome_page_header():
    #Given
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #When
    driver.get("https://benneleszek.github.io/python-2022-02-28/")
    #Then
    header = driver.find_element(By.TAG_NAME, "h1").text
    assert header == 'Welcome'