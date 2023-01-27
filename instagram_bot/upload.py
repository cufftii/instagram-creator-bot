from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time
from dotenv import load_dotenv
import os
import pyautogui

def upload_on_instagram(nickname):
    load_dotenv()
    id = os.getenv('ID')
    password = os.getenv('PASSWORD')
    base_url = os.getenv('base_url')

    f = open("results/daily_post.txt",'r', encoding="utf-8")
    daily_post = f.readlines()
    f.close()

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://www.instagram.com/')
    time.sleep(3)

    id_form = driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label')
    id_form.send_keys(id)

    password_form = driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label')
    password_form.send_keys(password)

    login_button = driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button')
    login_button.click()
    time.sleep(5)

    driver.get('https://www.instagram.com/{}/'.format(nickname))
    time.sleep(3)

    create_button = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/div/a')
    create_button.click()
    time.sleep(3)

    select_button = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button')
    select_button.click()
    time.sleep(3)

    pyautogui.write(base_url+'results\\post_image.png')
    pyautogui.press('enter')

    time.sleep(3)
    next_button = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/button')
    next_button.click()
    time.sleep(3)
    next_button = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/button')
    next_button.click()
    time.sleep(3)

    post_input = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea')
    post_input.send_keys(daily_post)
    time.sleep(3)

    share_button = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/button')
    share_button.click()
    time.sleep(3)