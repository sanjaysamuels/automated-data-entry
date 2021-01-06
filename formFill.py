from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

URL = "https://docs.google.com/forms/d/e/1FAIpQLScWohpEaAIe5-k9NWnCc_mCa3GOo_FC2HiCmilitGIL9xORTA/viewform"
CHROME_DRIVER_PATH = "INSERT YOUR CHROME DRIVER PATH HERE"


class FillForm():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def new_form(self):
        self.driver.get(URL)

    def fill_address(self, address):
        time.sleep(2)
        address_input = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_input.send_keys(address)

    def fill_price(self, price):
        price_input = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_input.send_keys(price)

    def fill_link(self, link):
        link_input = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_input.send_keys(link)
        submit = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
        time.sleep(2)
        submit.click()
