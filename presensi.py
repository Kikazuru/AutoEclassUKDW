from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class PresensiEclass:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def closeBrowser(self):
        self.driver.close()
    
    def login(self, kode_matkul):
        driver = self.driver
        driver.get(f"https://eclass.ukdw.ac.id/e-class/id/kelas/presensi/{kode_matkul}")
        time.sleep(2)
        
        username = driver.find_element_by_xpath("//input[@name='id']")
        username.clear()
        username.send_keys(self.username)

        password = driver.find_element_by_xpath("//input[@name='password']")
        password.clear()
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
    
    def presensi(self):
        driver = self.driver
        # edit bagian hadir
        hadir = driver.find_element_by_xpath("//a[@class='menu sub ic_nilai']")
        hadir.click()
        time.sleep(5)

