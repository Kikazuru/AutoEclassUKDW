from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re


class Eclass:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def closeBrowser(self):
        self.driver.close()
    
    def login(self):
        driver = self.driver
        driver.get(f"https://eclass.ukdw.ac.id/")
        time.sleep(2)
        
        username = driver.find_element_by_xpath("//input[@name='id']")
        username.clear()
        username.send_keys(self.username)

        password = driver.find_element_by_xpath("//input[@name='password']")
        password.clear()
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
    
    def presensi(self, kode_matkul):
        driver = self.driver
        driver.get(f"https://eclass.ukdw.ac.id/e-class/id/kelas/presensi/{kode_matkul}")
        # edit bagian hadir
        try:
            hadir = driver.find_element_by_xpath("//input[@name='presensi_hadir']") 
        except:
            return False
        hadir.click()
        time.sleep(5)
        return True

    def scrapJadwalEclass(self):
        driver = self.driver
        kelas = driver.find_elements_by_xpath("//div[@class='kelas_box']")
        hasil = {}
        for item in kelas:
            temp = item.text
            hari = re.search(r"\w+,",temp).group(0)[:-1]
            date = re.findall(r"\d{2}:\d{2}",temp)
            kode = re.search(r"TI\d{4}",temp).group(0)
            nama = re.search(r"(?<=(]))[\w\s]*(?=(GRUP))", temp).group(0)
            if hari in hasil:
                hasil[hari].update({kode : {
                        "nama":nama, 
                        "mulai":date[0], 
                        "selesai":date[1]}})
            else:
                hasil[hari] = {
                    kode:{
                        "nama":nama, 
                        "mulai":date[0], 
                        "selesai":date[1]
                        }
                    }
        return hasil
