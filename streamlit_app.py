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

driver.implicitly_wait(10) # seconds


driver.get("https://app.powerbi.com/groups/me/datasets/d6d2d0f2-f1c7-429f-86e5-f594d17a3c3e/details")
user = 'savellaneda@promotive.com.ar'
password = 'Prombi23'


username = driver.find_element('id', value='email')

username.send_keys(user)
driver.find_element('id', "submitBtn").click()

driver.find_element('name', 'passwd').send_keys(password)

buttton = driver.find_element('id', 'idSIButton9')

buttton.click()

buttton = driver.find_element('id', 'idSIButton9')

buttton.click()

actualizacion = driver.find_element(By.XPATH, '//*[@id="content"]/dataset-related-reports-container/section/section/dataset-information/section/dataset-details-card/mat-card/mat-card-content/section/dataset-details-field[2]/mat-card-subtitle/section[2]/dataset-icon-container-modern/span[1]')

actual = actualizacion.text

st.write(f'Última actualización: {actual}')

buttton = driver.find_element(By.XPATH ,'//*[@id="content"]/dataset-related-reports-container/dataset-action-bar/action-bar/action-button[2]/button')
buttton.click()



actualizar_bot = driver.find_element(By.XPATH ,'//*[@id="mat-menu-panel-8"]/div/button[1]')

actualizar_bot.click()

actualizacion = driver.find_element(By.XPATH, '//*[@id="content"]/dataset-related-reports-container/section/section/dataset-information/section/dataset-details-card/mat-card/mat-card-content/section/dataset-details-field[2]/mat-card-subtitle/section[2]/dataset-icon-container-modern/span[1]')

el = WebDriverWait(driver, timeout=500).until(lambda d: actual != actualizacion.text)

st.success('Actualización extitosa!')
