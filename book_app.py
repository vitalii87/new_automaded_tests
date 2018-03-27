from selenium import webdriver
import unittest
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait

class BookApp:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.base_url = "http://development.nxte.nl/Cadeau_Concepten/CACO1708-CadeauService"
        self.verificationErrors = []
        self.driver.get(self.base_url)

    def second_card(self, price, quantity, id_card, id_price, id_submit):
        driver = self.driver
        driver.find_element_by_id(id_card).clear()
        driver.find_element_by_id(id_card).send_keys(quantity)
        driver.find_element_by_id(id_price).send_keys(price)
        driver.find_element_by_id(id_submit).click()

    def first_card(self, quantity, price, css_select, id_card, id_price, id_submit):
        driver = self.driver
        driver.find_element_by_css_selector(css_select).click()
        driver.find_element_by_id(id_card).clear()
        driver.find_element_by_id(id_card).send_keys(quantity)
        driver.find_element_by_id(id_price).send_keys(price)
        driver.find_element_by_id(id_submit).click()

    def User_login(self, user, password, name, pswd, id_submit):
        driver = self.driver
        driver.find_element_by_name(name).send_keys(user)
        driver.find_element_by_name(pswd).send_keys(password)
        driver.find_element_by_id(id_submit).click()

    def destroy(self):
        sleep(2)
        self.driver.close()