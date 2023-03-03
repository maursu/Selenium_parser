import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from decouple import config
from db_settings import save_to_db, post, engine


url = config('URL')
driver_path = config('DRIVER_PATH')

class Parser:
    def __init__(self, url) -> None:
        self.url = url
        self.driver = webdriver.Chrome(
            executable_path=driver_path
        )
    
    def _check_status(self, url):
        return requests.get(url).status_code

    def _parse_all_pages(self, url):
        url = url
        for page in range(2,101):
            self._get_elements(url)
            url = self.url[:-11] + f'page-{page}/' +self.url[-11::]
            print('page:', page)

    def _get_elements(self, url):
        self.driver.get(url)
        elements = self.driver.find_elements(By.CLASS_NAME, 'search-item')
        for element in elements:
            title = element.find_element(By.CLASS_NAME, 'title').text.strip()
            desctiption = element.find_element(By.CLASS_NAME,'description').text.strip()
            price = element.find_element(By.CLASS_NAME, 'price').text
            image = element.find_element(By.CLASS_NAME, 'image').find_element(By.TAG_NAME,'img').get_attribute('data-src')
            city = element.find_element(By.CLASS_NAME, 'location').find_element(By.TAG_NAME, 'span').text
            date = element.find_element(By.CLASS_NAME, 'location').find_element(By.CLASS_NAME, 'date-posted').text
            print(title, price, image, city, date, desctiption)
            try:
                save_to_db([
                    {
                    'title':title,
                    'description':desctiption,
                    'price':price,
                    'image':image,
                    'city':city,
                    'time_added':date
                    }
                ])
            except Exception:
                post.create(engine)
                save_to_db([
                    {
                    'title':title,
                    'description':desctiption,
                    'price':price,
                    'image':image,
                    'city':city,
                    'time_added':date
                    }
                ])
    
    def run(self):
        status = self._check_status(self.url)
        if status == 200:
            print(f'status {status}, running parser')
            self._parse_all_pages(self.url)
        else:
            print(f'status {status}, shut down') 
        
parser = Parser(url)
parser.run()



