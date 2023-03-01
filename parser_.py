import requests
from selenium import webdriver
from decouple import config

url = config('URL')
driver_path = config('DRIVERPATH')

class Parser:

    def __init__(self, url) -> None:
        self.url = _URL
        self.driver =  driver = webdriver.Chrome(
            executable_path=driver_path
        )
    
    def _check_status(self, url):
        return requests.get(url).status_code
    
    def _get_html(self, url):
       
        driver.maximize_window()
        driver.get(url)
        driver.close()
        driver.quit()

    
    def run(self):
        status = self._check_status(self.url)
        if status == 200:
            print(f'status {status}, running parser')
            self._get_html(self.url)
        else:
            print(f'status {status}, shut down') 
        
parser = Parser(_URL)

parser.run()



