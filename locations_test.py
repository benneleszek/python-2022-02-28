import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locations_po import locationsPage
from locations_rest_api import create_location, delete_all_locations

@pytest.fixture
def driver():
    delete_all_locations()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    return driver

def test_create(driver: webdriver.Chrome):
    #Given
    ###requests.delete("http://127.0.0.1:8080/api/locations")
    
    page = locationsPage(driver)
    
    #When
    page.click_on_create_location()
    page.fill_create_form("Home", "1,1")
    page.click_on_create_location_submit()
    
    #Then
    page.wait_for_message("Location has been created")
   
    name, coords = page.get_first_location_table()
    assert name == "Home"
    assert coords == "1, 1"

def test_create_negative(driver: webdriver.Chrome):
    
    page = locationsPage(driver)

    page.click_on_create_location()
    page.click_on_create_location_submit()
    page.wait_for_name_message("Can not be empty name!")

    assert page.has_name_red_boarder()

    page.wait_for_table_has_rows(0)

def test_edit(driver: webdriver.Chrome):
       #Given: Legyen az adatbázisban egy Test... nevű location
       create_location("Test", "5,5")

       page = locationsPage(driver)
       page.wait_for_table_has_rows(1) 
       
       page.click_on_first_edit_btn()
       page.fill_update_form("Test2","8,8")
       page.click_on_update_location_submit()

       page.wait_for_message("Location has been modified")
       page.wait_for_table_has_rows(1)

       name, coords = page.get_first_location_table()
       assert name == "Test2"
       assert coords == "8, 8"

def test_delete(driver: webdriver.Chrome):
    
    create_location("Test", "5,5")

    page = locationsPage(driver)

    page.wait_for_table_has_rows(1)

    page.click_on_delete_btn()

    page.wait_for_delete_confirm_message("Are you sure to delete location?")

    page.click_on_delete_location_confirm_btn()

    page.wait_for_message("Location has been deleted")

    page.wait_for_table_has_rows(0)

    