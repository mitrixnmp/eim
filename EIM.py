from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import informacije
import sys


class otvaranje:
    def __init__(self, usernameeref, passworderef, usernamemoodle, passwordmoodle):
        self.driver = webdriver.Firefox()
        self.driver.get("https://eref.vts.su.ac.rs/sr/default/eboard/index")
        sleep(2)
        self.driver.find_element_by_xpath('//input[@name=\"username\"]')\
            .send_keys(usernameeref)
        self.driver.find_element_by_xpath('//input[@name=\"password\"]')\
            .send_keys(passworderef)
        self.driver.find_element_by_xpath(
            '//input[@value="Prijava / Bejelentkezés"]').click()
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/ul/li[2]/a').click()
        self.driver.execute_script(
            "window.open('https://moodle2.vts.su.ac.rs/login/index.php','_blank')")
        sleep(2)
        self.driver.switch_to_window(self.driver.window_handles[1])
        self.driver.find_element_by_xpath('//*[@id="username"]')\
            .send_keys(usernamemoodle)
        self.driver.find_element_by_xpath('//*[@id="password"]')\
            .send_keys(passwordmoodle)
        self.driver.find_element_by_xpath('//*[@id="loginbtn"]').click()
        sleep(3)


otvaranje(informacije.ueref, informacije.peref,
          informacije.umoodle, informacije.pmoodle)

sys.exit()
