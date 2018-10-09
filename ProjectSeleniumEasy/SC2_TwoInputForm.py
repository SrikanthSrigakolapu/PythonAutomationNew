import os
import time
from selenium import webdriver
import unittest

class TwoInputForm(unittest.TestCase):

    def setUp(self):
        #initiate the Chrome instance
        parentpath=os.path.dirname(os.path.abspath(__file__))
        #self.chromeDriver=webdriver.Chrome(executable_path=os.path.dirname(parentpath)+"/LinuxDrivers/chromedriver")
        self.chromeDriver = webdriver.Chrome(executable_path=os.path.dirname(parentpath) + "/WindowsDrivers/chromedriver.exe")
        self.chromeDriver.maximize_window()


    def test_filltwoinput(self):
        chromedriver=self.chromeDriver
        chromedriver.get("https://www.seleniumeasy.com/test")
        # TODO: right now I am using print statements need to look for logging option in python
        print("Success: Opened the url in chrome")

        inputFromsElem = chromedriver.find_element_by_xpath("//a[normalize-space()=\"Input Forms\"]/b[@class=\"caret\"]")
        inputFromsElem.click()

        chromedriver.save_screenshot("snapshots/SC1_SingleInputField/InputFormsClick.png")
        print("SuccessFully clicked the InputFormsClick")

        SFDelem=chromedriver.find_element_by_xpath("//ul[@class=\"dropdown-menu\"]/li/a[text()=\"Simple Form Demo\"]")
        SFDelem.click()
        chromedriver.save_screenshot("snapshots/SC1_SingleInputField/SimpleFormDemoPage.png")

        print("entered the Simple Form Demo page")
        chromedriver.execute_script("window.scroll(0,document.body.scrollHeight)")
        time.sleep(10)
        sum1=chromedriver.find_element_by_id("sum1")
        sum1.send_keys("23")

        sum2=chromedriver.find_element_by_id("sum2")
        sum2.send_keys("27")

        chromedriver.find_element_by_xpath("//form[@id='gettotal']/button").click()

        time.sleep(10)

        verify=chromedriver.find_element_by_xpath("//span[@id='displayvalue']")

        self.assertEqual('50', verify.text)
        time.sleep(10)

    def tearDown(self):
        self.chromeDriver.close()

if __name__ == '__main__':
    unittest.main()
