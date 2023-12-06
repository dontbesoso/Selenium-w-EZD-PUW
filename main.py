import unittest

from App import App

from selenium import webdriver
from selenium.webdriver.common.by import By

class testTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close()

    def test_scenario_001(self):
        self.app = App()
        driver = self.driver

        driver.get(self.app.getAuthPath())

        link = driver.find_element(By.LINK_TEXT, 'Nowe pisma')
        link.click()

        link = driver.find_element(By.LINK_TEXT, 'Nowa koszulka')
        link.click()

        link = driver.find_element(By.CLASS_NAME, 'txtNowePismo')
        link.send_keys("Testowa koszulka")

        link = driver.find_element(By.ID, "btnDodajNowePismo")
        link.click()


if __name__ == "__main__":
    unittest.main()