
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locations_waits import table_has_rows

class locationsPage:

    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)
        self.driver.get("http://127.0.0.1:8080")

    def click_on_create_location(self):
        """Ez rákklikel a create location linkre"""
        self.driver.find_element(By.LINK_TEXT, "Create location").click()
        
    def fill_create_form(self, name, coord):
        self.driver.find_element(By.ID, "location-name").send_keys(name)
        self.driver.find_element(By.ID, "location-coords").send_keys(coord)

    def click_on_create_location_submit(self):
        self.driver.find_element(By.CLASS_NAME, "btn-primary").click()

    def wait_for_message(self, message):
        self.wait.until(EC.text_to_be_present_in_element((By.ID, "message-div"), message))

    def wait_for_name_message(self, message):
        self.wait.until(EC.text_to_be_present_in_element((By.ID, "location-name-feedback"), message))

    def get_first_location_table(self):
        row = self.driver.find_element(By.CSS_SELECTOR, "#locations-table-tbody > tr")
        name = row.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
        coords = row.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text
        return (name, coords)

    def has_name_red_boarder(self):
        input_field = self.driver.find_element(By.ID, "location-name")
        return "is-invalid" in input_field.get_attribute("class").split()

    def wait_for_table_has_rows(self, number):        
        self.wait.until(table_has_rows(number))

    def click_on_first_edit_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, "#locations-table-tbody > tr > td:nth-child(6) > button.btn.btn-link").click()

    def fill_update_form(self, name, coord):
        name_field = self.driver.find_element(By.ID, "update-location-name")
        name_field.clear()
        name_field.send_keys(name)

        coords_field = self.driver.find_element(By.ID, "update-location-coords")
        coords_field.clear()
        coords_field.send_keys(coord)

    def click_on_update_location_submit(self):
        self.driver.find_element(By.CSS_SELECTOR, "[value='Update location']").click()

    def click_on_delete_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, "#locations-table-tbody > tr > td:nth-child(6) > button.btn.btn-danger").click()

    def wait_for_delete_confirm_message(self, message):
            self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#delete-location-form > p:nth-child(1)"), message))

    def click_on_delete_location_confirm_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, "[value='Delete location']").click()