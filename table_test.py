import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    #Given
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #When
    driver.get("http://127.0.0.1:5500/docs/index.html")
    return driver

def test_table_cells(driver: webdriver.Chrome):
    elements = driver.find_elements_by_class_name("price")
    prices = []
    for element in elements:
        prices.append(int(element.text))
    assert prices == [100,400,150]