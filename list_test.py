from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_list():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:5500/docs/index.html")

    listelements = driver.find_elements(By.TAG_NAME, "li")

    toolnames = []
    for element in listelements:
        toolnames.append(element.text)

    assert toolnames == ['Python', 'PIP', 'Webdriver', 'Selenium']
