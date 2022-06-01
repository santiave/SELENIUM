import glob
import os

import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--disable-features=NetworkService")
options.add_argument("--window-size=1920x1080")
options.add_argument("--disable-features=VizDisplayCompositor")






driver = webdriver.Chrome(options=options, service_log_path='selenium.log')
driver.implicitly_wait(3)
driver.get('https://cuenta.docturno.com/ingresar')
mail= driver.find_element(By.XPATH,'//*[@id="email"]')
mail.send_keys('Info@athentun.org')
mail.submit()
time.sleep(1)  


passw=driver.find_element(By.XPATH, '//*[@id="password"]')
time.sleep(1)  
passw.send_keys('44528765')

boton = driver.find_element(By.CLASS_NAME, 'signin-password-action')
boton.click()
st.write(driver.driver.get_screenshot_as_png())
