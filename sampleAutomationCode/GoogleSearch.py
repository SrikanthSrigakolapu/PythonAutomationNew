from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.common.keys import Keys

#below is the one for getting the current directory
parentdir=os.path.dirname(os.path.abspath(__file__))

print(os.path.dirname(parentdir)+"\LinuxDrivers\chromedriver.exe")
#invoking the chrome instance
driverchrome=webdriver.Chrome(executable_path=os.path.dirname(parentdir)+"\LinuxDrivers\chromedriver.exe")

print("Chrome invoked successfully")

#opening the url
driverchrome.get("https://www.google.com")

#verify the title
assert "Google" in driverchrome.title

print("Done hitting the url")
driverchrome.save_screenshot('sample.png')
searchElement=driverchrome.find_element_by_class_name('gsfi')
searchElement.send_keys("This is Srikanth")
searchElement.submit()

time.sleep(10)

print("process is done")

driverchrome.close()
