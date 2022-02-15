import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import string
import time

driver = webdriver.Chrome()
url = 'https://www.instagram.com/'
credit_print = ['email', 'password']


def open_file(row):


    f = open('file.txt', 'r')

    time.sleep(1)
    get_creditials(f, row)


def get_creditials(file, row):

    lines = file.readlines()

    line = lines[row]
    splitted = line.split(':')
    email = splitted[0]
    password = splitted[1]

    setup(email, password, row)


def setup(email, password, row):


    time.sleep(1)

    driver.get(url)
    login(email, password, row);


def login(email, password, row):
    time.sleep(3)


    while(True):

        try:

            email_field = driver.find_element(By.NAME, 'username')
            # Deletes old Email in Field
            email_field.send_keys(Keys.CONTROL, "a")
            email_field.send_keys(Keys.DELETE)
            # enters Email
            email_field.send_keys(email)

            credit_print[0] = email
            time.sleep(1)
            # submit
            #driver.find_element(By.CLASS_NAME, 'primary-button').click()

            # enters Password
            pass_field = driver.find_element(By.NAME, 'password')
            pass_field.send_keys(password)

            credit_print[1] = password
            pass_field.send_keys(Keys.ENTER)
            time.sleep(1)

            print(credit_print)

            time.sleep(2)

            open_file(row + 1)
        except:
            print("There was a problem. Take a look at the Window and see whats wrong.")
            time.sleep(10)


open_file(1)
