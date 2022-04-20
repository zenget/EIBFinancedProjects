import os
import re
from datetime import datetime
from tempfile import mkdtemp
from decimal import Decimal

from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC


class EIBFinancedProjectsParser():

    BASE_URL = 'https://www.eib.org/en/projects/loans/index.htm'

    DROPDOWN_PAGINATION_CLASS = 'select__single-select-button-pagination'
    
    DROPDOWN_PAGINATION_VALUE = '100'

    def get_financed_projects(self):

        chrome_options = Options()
        chrome_options.add_argument("--enable-javascript")
        chrome_options.add_argument("--headless")
        
        driver = webdriver.Chrome(options=chrome_options)

        driver.get(self.BASE_URL,)

        #Check if all loading page completed
        WebDriverWait(driver, 20).until(
                 EC.presence_of_element_located(
                    (By.TAG_NAME, 'article'))
            )

        #Show First 100 records using dropdown pagination
        dropdown_pagination = Select( driver.find_element(by=By.CLASS_NAME, value=self.DROPDOWN_PAGINATION_CLASS) )
        dropdown_pagination.select_by_value(self.DROPDOWN_PAGINATION_VALUE)
        
        #Check if all loading page completed
        WebDriverWait(driver, 20).until(
                 EC.presence_of_element_located(
                    (By.TAG_NAME, 'article'))
            )
        # Get Countries        
        countries = self.get_countries(driver)
        # Get Sectors
        sectors = self.get_sectors(driver)

        # Get Loans
        loans =  self.get_loans(driver)
        
        return {'sectors' : sectors, 'countries':countries, 'loans':loans}


    def get_countries(self,driver):
        
        countries = []
        
        elem = driver.find_element(by=By.XPATH, value='//div[@data-filter-category="countries"]')

        if elem is None:
            raise Exception('Element not found!')
        
        elem_countries = elem.find_element(by=By.TAG_NAME, value='select')


        options = Select(elem_countries).options;
        
        for opt in options:
            
            countries.append({'code':opt.get_attribute('value') , 'name':  opt.get_attribute('text')})
        
        return countries

    def get_sectors(self,driver):
        sectors = []
        
        elem = driver.find_element(by=By.XPATH, value='//div[@data-filter-category="sectors"]')

        if elem is None:
            raise Exception('Element not found!')
        
        elem_sectors = elem.find_element(by=By.TAG_NAME, value='select')

        options = Select(elem_sectors).options;
        
        for opt in options:

            sectors.append({'code':opt.get_attribute('value') , 'name':  opt.get_attribute('text')})
        
        return sectors
        
    def get_loans(self,driver):
        
        loans = []

        table = driver.find_element(by=By.CLASS_NAME, value='search-filter__results')
        
        rows = table.find_elements(by=By.TAG_NAME, value='article')
        
        for row in rows[1:]:

            row_child = row.find_element(by=By.CLASS_NAME, value='row-list')
            
            cells = row_child.find_elements(by=By.XPATH, value="./*") 

            if(len(cells) == 5):
                loans.append({
                    'signature_date':datetime.strptime(cells[0].text, "%d %B %Y").date(),
                    'title':cells[1].text,
                    'country':cells[2].get_attribute('innerText'),
                    'sector':cells[3].get_attribute('innerText'),
                    'signed_amount': float(re.sub(r'[^\d.]', '', cells[4].text))
                }) 
                
        return loans

# t1 = EIBFinancedProjectsParser()

# print(t1.get_financed_projects())