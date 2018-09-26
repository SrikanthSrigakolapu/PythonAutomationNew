import unittest
import os
import time
from selenium import webdriver


class SingleInputField(unittest.TestCase):

    def setUp(self):
        #initiate the Chrome instance
        parentpath=os.path.dirname(os.path.abspath(__file__))
        self.chromeDriver=webdriver.Chrome(executable_path=os.path.dirname(parentpath)+"\WindowsDrivers\chromedriver.exe")

    def test_OpenSingleFormDemo(self):
        chromedriver=self.chromeDriver
        chromedriver.get("httos://seleniumeasy.com/test/")
        self.assertEqual('Selenium Easy',chromedriver.title)

        #TODO: right now I am using print statements need to look for logging option in python
        print("Success: Opened the url in chrome")




