import re
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import json
from basePage import Base_Page
import sys
sys.path.insert(0, r'c:\\Users\\Chani\\Desktop\\bootcamp\\project_2')
from util.log_class import Log
from locators.locator import HomepageLocators
os.chdir(r'C:\\Users\\Chani\\Desktop\\bootcamp\\project_2\\test')
locat = HomepageLocators()
l = Log()

class Automation_Project(Base_Page):

    def __init__(self,driver ,base_url):
        super().__init__(self.driver)
        self.driver = driver
        self.base_url = base_url
        self.driver.get(base_url)

    def test_check_first_name(self, firstname):
        '''
        chani kadosh
        19-02-2023
        The function checks the correctness of the first name - that it does not contain numbers,
        that it is not empty
        '''
        try:
            firstname_locator = self.driver.find_element(
                *locat.firstname_locator)
            if firstname_locator.get_attribute("value") != "":
                firstname_locator.clear()
            assert firstname.isalpha(), "Name should contain only letters"
            firstname_locator.send_keys(firstname)
            time.sleep(2)
        except:
            assert False, "test_check_first_name failed"

    def test_check_last_name(self, lastname):
        '''
        chani kadosh
        19-02-2023
        The function checks the correctness of the last name - that it does not contain numbers,
        that it is not empty
        '''
        try:
            lastname_locator = self.driver.find_element(
                *locat.lastname_locator)
            assert lastname.isalpha(), "Last name should contain only letters"
            if lastname_locator.get_attribute("value") != "":
                lastname_locator.clear()
            lastname_locator.send_keys(lastname)
            time.sleep(2)
        except Exception as e:
            raise Exception("test_check_last_name-failed: " + str(e))

    def test_check_mail(self, email):
        '''
        chani kadosh
        19-02-2023
        The function checks the integrity of the email, and that it is not empty
        '''
        email_regex = r"[^@]+@[^@]+\.[^@]+"
        try:
            email_locator = self.driver.find_element(*locat.email_locator)
            if email != "NON":
                if re.match(email_regex, email):
                    if email_locator.get_attribute("value") != "":
                        email_locator.clear()
                    email_locator.send_keys(email)
                    self.assertEqual(email_locator.get_attribute("value"), email)
                else:
                    raise ValueError("Invalid email address")
        except Exception as e:
            raise Exception(f"test_check_mail failed with error: {str(e)}")

    def test_check_genus(self, gender):
        '''
        chani kadosh
        19-02-2023
        The function checks the correctness of the gender selection - that only one option is selected,
        and that it is the correct option
        '''
        if gender != "NON":
            match gender:
                case "F":
                    gender_options = self.driver.find_elements(*locat.female_locator)
                case "M":
                    gender_options = self.driver.find_elements(*locat.male_locator)
                case "O":
                    gender_options = self.driver.find_elements(*locat.other_locator)

            for option in gender_options:
                if option.get_attribute("value") == gender:
                    option.click()
                    break
            is_checked = False
            for option in gender_options:
                if option.get_attribute("value") == gender:
                    is_checked = option.is_selected()
                    break
            self.assertTrue(is_checked, f"{gender} option is not checked")
            time.sleep(20)
        else:
            print("Gender is not provided")  

    def test_check_city(self, city):
        '''
        chani kadosh
        19-02-2023
        The function receives a city and it selects that city in the record
        '''
        if city != "NON":
            try:
                select_elem = self.driver.find_element(*locat.city_locator)
                select_options = Select(select_elem).options
                assert any(option.get_attribute('value') == city for option in select_options), f"No option with value '{city}' was found"
                for option in select_options:
                    if option.get_attribute('value') == city:
                        option.click()
                        assert option.is_selected(), f"Option with value '{city}' was not selected"
                        return
            except:
                raise Exception(f"test_check_city failed for '{city}'")

    def test_select_area_code(self, prefix):
        '''
        chani kadosh
        19-02-2023
        The function receives the prefix of the phone number and checks if it exists and marks it
        '''
        try:
            select_elem = self.driver.find_element(*locat.area_locator)
            select = Select(select_elem)
            select.select_by_value(prefix)
            selected_option = select.first_selected_option
            assert selected_option.get_attribute("value") == prefix, f"Expected prefix '{prefix}', but got '{selected_option.get_attribute('value')}'"
        except:
            print(f"Element not found for prefix {prefix}")

    def test_input_numberphon(self, phone_number):
        '''
        chani kadosh
        19-02-2023
        The function receives a number and checks whether it contains 9 digits
        '''
        try:
            digits_only = "".join([c for c in phone_number if c.isdigit()])
            select_elem = self.driver.find_element(*locat.phone_locator)
            if select_elem.get_attribute("value") != "":
                select_elem.clear()

            if len(digits_only) == 9:
                select_elem.send_keys(phone_number)
        except Exception as e:
            raise AssertionError(f"Failed to input phone number {phone_number}. Error: {str(e)}")
        selected_value = select_elem.get_attribute("value")
        assert selected_value == phone_number, f"Expected '{phone_number}', but got '{selected_value}'"
   
    def click_available_checkboxes(self):
        '''
        chani kadosh
        19-02-2023
        The function marks all the math and physics checkboxes
        '''
        try:
            math_button = self.driver.find_element(*locat.physics_locator)
            physics_button = self.driver.find_element(*locat.math_locator)
            if math_button.is_enabled() and physics_button.is_enabled():
                math_button.click()
                physics_button.click()
            else:
                raise Exception
        except:
            return False

    def check_and_click_buttons(self):
        '''
        chani kadosh
        19-02-2023
        The function marks all available check boxes and if one is not available the function fails
        '''
        buttons = self.driver.find_elements(*locat.all_checkbox_locator)
        for button in buttons:
            if button.is_enabled():
                button.click()
            else:
                raise Exception
        time.sleep(20)

    def check_buttons_available_and_click_by_id(self, buttons_names):
        """
        chani kadosh
        19-02-2023
        The function receives an array of words and marks them
        """
        for button_name in buttons_names:
            try:
                button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, f"//input[@name='{button_name}']")))
                button.click()
                print(f"Button '{button_name}' was found and clicked")
                assert button.is_selected(), f"Button '{button_name}' was not selected"
            except:
                print(f"Button '{button_name}' was not found or not clickable")

    def test_clear_fields(self):
    # find all relevant form fields
        try:
            first_name = self.driver.find_element(*locat.firstname_locator)
            last_name = self.driver.find_element(*locat.lastname_locator)
            city = self.driver.find_element(*locat.city_locator)
            email = self.driver.find_element(*locat.email_locator)
            area_code = self.driver.find_element(*locat.area_locator)
            phone = self.driver.find_element(*locat.phone_locator)
            gender = self.driver.find_element(*locat.firstname_locator)
            math = self.driver.find_element(*locat.math_locator)
            physics = self.driver.find_element(*locat.physics_locator)
            pop = self.driver.find_element(*locat.pop_locator)
            dud = self.driver.find_element(*locat.dud_locator)
            bio = self.driver.find_element(*locat.biology_locator)
            chem = self.driver.find_element(*locat.chem_locator)
            eng = self.driver.find_element(*locat.english_locator)

            clear = self.driver.find_element(*locat.clear_locator)
            clear.click()

        except:
            print("Failed to find and click element")

        # assert that all fields are empty
        try:
            assert first_name.get_attribute('value') == ''
            assert last_name.get_attribute('value') == ''
            assert city.get_attribute('value') == ''
            assert email.get_attribute('value') == ''
            assert area_code.get_attribute('value') == ''
            assert phone.get_attribute('value') == ''
            assert not gender.is_selected()
            assert not math.is_selected()
            assert not physics.is_selected()
            assert not pop.is_selected()
            assert not dud.is_selected()
            assert not bio.is_selected()
            assert not chem.is_selected()
            assert not eng.is_selected()
        except:
            print("Failed to assert that fields are empty")

    def run(self,data):
        for test_data in data['tests_Data']:
                self.test_check_first_name(test_data['First Name'])
                self.test_check_last_name(test_data['Last Name'])
                # self.test_check_mail(test_data['Email'])
                self.test_check_city(test_data['City'])
                self.test_select_area_code(test_data['prefix_Mobile'])
                self.test_input_numberphon(test_data['Mobile'])
                self.check_buttons_available_and_click_by_id(test_data['list'])
                self.test_check_genus(test_data['type'])
                
        self.test_clear_fields()
      
    def test_link_windy_locator(self):
        try:
            link = self.driver.find_element(*locat.windy_locator)
            response = requests.get(link)
            self.assertEqual(response.status_code, 200)
        except:
            # self.driver.save_screenshot("C:\Users\Chani\Desktop\bootcamp\project_2\screenshots\test_test_link_windy_locator.jpg")
            l.writeLog("test_link_windy_locator-error")
            raise Exception

