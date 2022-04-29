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


def delete_selenium_log():
    if os.path.exists('selenium.log'):
        os.remove('selenium.log')


def show_selenium_log():
    if os.path.exists('selenium.log'):
        with open('selenium.log') as f:
            content = f.read()
            st.code(content)


# not required anymore:
# def get_chromedriver_path():
#     results = glob.glob('/**/chromedriver', recursive=True)  # workaround on streamlit sharing
#     return results[0]


def run_selenium():
    name = str()
    with webdriver.Chrome(options=options, service_log_path='selenium.log') as driver:
        url = "https://www.unibet.fr/sport/football/europa-league/europa-league-matchs"
        driver.get(url)
        xpath = '//*[@class="ui-mainview-block eventpath-wrapper"]'
        # Wait for the element to be rendered:
        element = WebDriverWait(driver, 10).until(lambda x: x.find_elements(by=By.XPATH, value=xpath))
        name = element[0].get_property('attributes')[0]['name']
    return name


if __name__ == "__main__":
    delete_selenium_log()
    st.set_page_config(page_title="Selenium Test", page_icon='✅',
        initial_sidebar_state='collapsed')
    st.title('🔨 Selenium Test for Streamlit Sharing')
    st.markdown("""
        This app is only a very simple test for **Selenium** running on **Streamlit Sharing** runtime. <br>
        The suggestion for this demo app came from a post on the Streamlit Community Forum.  <br>
        <https://discuss.streamlit.io/t/issue-with-selenium-on-a-streamlit-app/11563>  <br>
        In rare cases this app has deployment issues on Streamlit Cloud and the deployment fails, but usually it works.

        This is just a very very simple example and more a proof of concept.
        A link is called and waited for the existence of a specific class and read it. If there is no error message, the action was successful.
        Afterwards the log file of chromium is read and displayed.

        ---
        """, unsafe_allow_html=True)

with st.spinner(text="Actualizando Dasboard..."):



    driver = webdriver.Chrome()

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
