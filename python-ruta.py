import time
import selenium
import os
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
# Seleccionando el directorio donde esta el chromedriver
# Seleccionando el directorio donde esta el chromedriver
os.chdir("C:/Users/hp/Desktop/Certus/dataops/sesion03/jenkins-python")
os.getcwd()

# Crenado el objeto chrome_options
chrome_options = webdriver.ChromeOptions()

# Crear una instancia del controlador Chrome
driver = webdriver.Chrome(options=chrome_options)
# Maximizando
driver.maximize_window()
# Abriendo la pagina https://www.worldometers.info/world-population/population-by-country/
driver.get("https://www.worldometers.info/world-population/population-by-country/")
