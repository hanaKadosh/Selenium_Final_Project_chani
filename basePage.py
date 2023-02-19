# class Base
import unittest


class Base_Page(unittest.TestCase):
    def __init__(self, driver):
        self.driver = driver

    def chack_titel(self, title):
        try:
            current_title = self.driver.title
            self.assertEqual(title, current_title)
            return True
        except:
            raise Exception('not is the correct web page')

    # def get_title(self):
    #     return self.driver.title
    
    # def get_url(self):
    #     return self.driver.current_url