from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service()
driver = webdriver.Chrome(service=service)