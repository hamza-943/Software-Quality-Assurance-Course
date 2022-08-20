# install the following packaages 

from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import unittest

#This code uses the google chrome browser to conduct a single test on the python.org website

class SeleniumTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def testGoogle(self):
        
        driver = self.driver
        driver.get('https://www.google.com/?client=chrome')

        
        searchbar = driver.find_element(By.CLASS_NAME, 'gLFyf')
        searchbar.send_keys("Apple")
        searchbar.submit()

        
        time.sleep(1)

    
        topResults = driver.find_elements(By.XPATH, ".//*[@id='rso']//div//h3/a")
        assert topResults != None, "Page not rendered fully"
        for childLink in topResults:
            print(childLink.get_attribute("href"))

    def test_api_calls(self):
        driver = self.driver

       
        driver.get("https://www.google.com")

        print()
    
        for request in driver.requests:
            if request.response:
                print("Request Method:", request.method)
                print("Request Host:", request.host)
                print("Request Status Code:", request.response.status_code)
                print("Request Time Stamp:", request.response.date)
        print()

    def test_api_call(self):
        driver = self.driver
        # all API calls made by the webdriver are recorded and can be retrieved using the following functions
        driver.get("http://www.google.com")
        assert driver.requests[0].response.status_code == 200 or driver.requests[0].response.status_code == 302, "status code is not 200 or 302"
        
        print('\n')
        print("API testing using Selenium")
        print("Format: method, host, status code, date and time")

        # gets the list of all API calls made by the webdriver and prints out the first 10 which include all get and post requests
        for each in driver.requests[:10]:
             if each.response:
                print(each.method, each.host, each.response.status_code, each.response.date, end='\n')
        print("______________________________________________________________")

    def main():
        unittest.main()

    if __name__ == "__main__":
        main()
