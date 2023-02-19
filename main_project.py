import json
from automation_Project import Automation_Project
from dotenv import load_dotenv
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest
import sys
sys.path.insert(0, r'c:\\Users\\Chani\\Desktop\\bootcamp\\project_2')
from locators.locator import HomepageLocators
from nextpage import Nextpage

os.chdir(r'C:\\Users\\Chani\\Desktop\\bootcamp\\project_2\\test')
load_dotenv()


class TestRunner(unittest.TestCase):
    def __init__(self):
        pass

    def run_tests(self):
        with open('data.json', 'r') as f:
            data = json.load(f)
        page1 = Automation_Project(
            webdriver.Chrome(), os.getenv("MAIN_PAGE_PATH"))
        page1.run(data)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
