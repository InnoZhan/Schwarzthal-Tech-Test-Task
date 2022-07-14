from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json 


class Parser():
    def __init__(self):
        self.browser = webdriver.Chrome('chromedriver')

    def get_cvrs(self, count = 1000):
        url = f'https://datacvr.virk.dk/soegeresultater?sideIndex=0&size={count}'    
        self.browser.get(url)
        timeout = 5
        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, 'soegeresultaterTabel'))
            WebDriverWait(self.browser, timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")

        cvrs = []
        soup = BeautifulSoup(self.browser.page_source, 'html.parser')
        
        for element in soup.find_all("div", string="CVR-nummer:"):
            cvrs.append(element.parent.find('div', {'class': 'value'}).string)
        return cvrs

    def get_company_info_by_cvr(self, CVR):
        url = f'https://datacvr.virk.dk/gateway/virksomhed/hentVirksomhed?cvrnummer={CVR}&locale=en'
        self.browser.get(url)
        soup = BeautifulSoup(self.browser.page_source, 'html.parser')
        jsondata = json.loads(soup.find('pre').string)
        return jsondata
