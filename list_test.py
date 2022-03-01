from msilib.schema import CheckBox
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

@pytest.fixture
def driver():
    #Given
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #When
    driver.get("http://127.0.0.1:5500/docs/index.html")
    return driver

def test_list(driver: webdriver.Chrome):
    listelements = driver.find_elements(By.TAG_NAME, "li")

    toolnames = []
    for element in listelements:
        toolnames.append(element.text)

    assert toolnames == ['Python', 'PIP', 'Webdriver', 'Selenium']



def test_checkbox(driver: webdriver.Chrome):
    checkbox = driver.find_element_by_name('accept-license')
    checkbox.click()
    print("End")


def test_select(driver: webdriver.Chrome):
    select = Select(driver.find_element_by_name('car-type'))
    select.select_by_visible_text("Opel")
    print("End")
