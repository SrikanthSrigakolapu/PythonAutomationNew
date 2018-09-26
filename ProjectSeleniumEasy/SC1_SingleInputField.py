import unittest
import os
import time
from selenium import webdriver


class SingleInputField(unittest.TestCase):

    def setUp(self):
        #initiate the Chrome instance
        parentpath=os.path.dirname(os.path.abspath(__file__))
        self.chromeDriver=webdriver.Chrome(executable_path=os.path.dirname(parentpath)+"\WindowsDrivers\chromedriver.exe")
        self.chromeDriver.maximize_window()

    def test_OpenSingleFormDemo(self):
        chromedriver=self.chromeDriver
        chromedriver.get("https://seleniumeasy.com/test/")
        #self.assertEqual("Selenium Easy."chromedriver.title)

        #TODO: right now I am using print statements need to look for logging option in python
        print("Success: Opened the url in chrome")

        inputFromsElem=chromedriver.find_element_by_xpath("//a[normalize-space()=\"Input Forms\"]/b[@class=\"caret\"]")
        inputFromsElem.click()

        chromedriver.save_screenshot("snapshots/SC1_SingleInputField/InputFormsClick.png")
        print("SuccessFully clicked the InputFormsClick")

        SFDelem=chromedriver.find_element_by_xpath("//ul[@class=\"dropdown-menu\"]/li/a[text()=\"Simple Form Demo\"]")
        SFDelem.click()
        chromedriver.save_screenshot("snapshots/SC1_SingleInputField/SimpleFormDemoPage.png")

        print("entered the Simple Form Demo page")

    #def test_EnterSingleInput(self):
        chromedriver=self.chromeDriver
        singleInputFieldElement=chromedriver.find_element_by_xpath("//input[@id=\"user-message\"]")
        singleInputFieldElement.send_keys("Hello this is sentinel")

        showMessageButton=chromedriver.find_element_by_xpath("//button[text()=\"Show Message\"]")
        showMessageButton.click()
        chromedriver.save_screenshot("snapshots/SC1_SingleInputField/ShowMessage.png")


    def tearDown(self):
        self.chromeDriver.close()


if __name__ == '__main__':
    unittest.main()
