from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys

//below is the one for getting the current directory
parentdir=os.path.dirname(os.path.abspath(__file__))

print(os.path.dirname(parentdir)+"\WindowsDrivers\chromedriver.exe")
#invoking the chrome instance
driverchrome=webdriver.Chrome(executable_path=os.path.dirname(parentdir)+"\WindowsDrivers\chromedriver.exe")

#opening the url
driverchrome.get("https://www.google.com")

#verify the title
assert "Google" in driverchrome.title

print("process is done")

driverchrome.close()