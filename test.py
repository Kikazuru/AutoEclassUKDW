from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re


driver = webdriver.Chrome()
driver.get(f"https://eclass.ukdw.ac.id/e-class/id/kelas/index")
time.sleep(2)

username = driver.find_element_by_xpath("//input[@name='id']")
username.clear()
username.send_keys("71190434")

password = driver.find_element_by_xpath("//input[@name='password']")
password.clear()
password.send_keys("926885")
password.send_keys(Keys.RETURN)

kelas = driver.find_elements_by_xpath("//div[@class='kelas_box']")
for item in kelas:
    temp = item.text
    
    hari = re.search(r"\w+,",temp).group(0)[:-1]
    date = re.findall(r"\d{2}:\d{2}",temp)
    kode = re.search(r"TI\d{4}",temp).group(0)
    nama = re.search(r"(?<=(]))[\w\s]*(?=(GRUP))", temp).group(0)
    print(hari)


driver.close()