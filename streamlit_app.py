import streamlit as st
import time
"""
## Web scraping on Streamlit Cloud with Selenium

[![Source](https://img.shields.io/badge/View-Source-<COLOR>.svg)](https://github.com/snehankekre/streamlit-selenium-chrome/)

This is a minimal, reproducible example of how to scrape the web with Selenium and Chrome on Streamlit's Community Cloud.

Fork this repo, and edit `/streamlit_app.py` to customize this app to your heart's desire. :heart:
"""

with st.echo():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By




    @st.experimental_singleton
    def get_driver():
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    options = Options()
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    driver = get_driver()

    def login_linkedin(username, password):
    # Setting up the Chrome driver
    

        try:
            # Go to LinkedIn
            driver.get('http://www.linkedin.com/')
    
            # Wait for the page to load
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'session_key')))
    
            # Find the username and password fields and enter the data
            driver.find_element(By.ID, 'session_key').send_keys(username)
            driver.find_element(By.ID, 'session_password').send_keys(password)
    
            # Find the submit button and click it
            driver.find_element(By.CSS_SELECTOR, "[data-id='sign-in-form__submit-btn']").click()
    
            # Wait for the page to load after clicking the button
            WebDriverWait(driver, 10).until(EC.title_contains("LinkedIn"))
    
        except Exception as e:
            st.write(f"An error occurred: {e}")
    
        finally:
            time.sleep(10)
            st.write("it worked!")
            # Always ensure the browser gets closed
    login_linkedin("Maxbladt@outlook.com", "mama12!")
