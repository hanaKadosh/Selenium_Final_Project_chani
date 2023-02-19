from basePage import Base_Page
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Nextpage(Base_Page):
    def __init__(self,driver):
        pass


    def test_change_title(self):
        driver = webdriver.Chrome()
        driver.get('file:///C:/Users/Chani/Downloads/nextpage.html')
        button = driver.find_element(By.TAG_NAME, 'button')
        button.click()
        wait = WebDriverWait(driver, 10)
        title = wait.until(EC.text_to_be_present_in_element((By.ID, 'newTitle'), 'Finish'))
        assert title, "Title did not change to 'Finish' within 10 seconds"
        driver.quit()
