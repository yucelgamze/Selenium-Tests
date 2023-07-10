from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://atilsamancioglu.com")
blog_page = driver.find_element(By.XPATH, "/html/body/div/header/div[1]/div[3]/nav/div/ul/li[3]/a")
WebDriverWait(driver,4).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/header/div[1]/div[3]/nav/div/ul/li[3]/a")))
blog_page.click()

WebDriverWait(driver,4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME , "button")))
#read_buttons = driver.find_elements(By.CLASS_NAME , "button")
read_button = driver.find_element(By.CLASS_NAME , "button")
read_button.click()

WebDriverWait(driver,4).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/aside[4]")))
article_list = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/aside[4]")
print(f"atilsamacioglu.com has {len(article_list.text.splitlines())} blog posts")
