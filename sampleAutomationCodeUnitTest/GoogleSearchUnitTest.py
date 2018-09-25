import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GoogleSearchUnitTest(unittest.TestCase):

    def setUp(self):
        parentdir = os.path.dirname(os.path.abspath(__file__))
        print(os.path.dirname(parentdir) + "\WindowsDrivers\chromedriver.exe")
        # invoking the chrome instance
        self.driverchrome = webdriver.Chrome(executable_path=os.path.dirname(parentdir) + "\WindowsDrivers\chromedriver.exe")

    def test_google_search(self):
        driverchrome=self.driverchrome
        driverchrome.get("https://www.google.com")
        self.assertEqual("Google",driverchrome.title)
        print("Done hitting the url")
        driverchrome.save_screenshot('sample.png')
        searchElement = driverchrome.find_element_by_class_name('gsfi')
        searchElement.send_keys("This is Srikanth")
        searchElement.submit()
        time.sleep(10)
        print("process is done")

    def tearDown(self):
        self.driverchrome.close()

if __name__ == '__main__':
    unittest.main()
