import datetime
import os
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

# https://testrail.stage.mozaws.net/index.php?/cases/view/330155
#build:
driver: WebDriver=webdriver.Firefox()
print ("Firefox build:" + driver.capabilities['moz:buildID'])
# Open a website
driver.get('about:config')
acceptButton = driver.find_element(By.ID,"warningButton")
acceptButton.click()
delay = 3 # seconds to wait until config searchbox is displayed
myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'about-config-search')))
print ("Page is ready!")
configSearchBox=driver.find_element(By.ID, "about-config-search")
configSearchBox.click()
# write config you want to modify in firefox.In this case is media.autoplay.default
configSearchBox.send_keys("media.autoplay.default")
#define edit config button
time.sleep(5)
editConfigBtn = driver.find_element(By.CSS_SELECTOR, "#prefs tr:nth-child(1) td.cell-edit button")
editConfigBtn.click()
editConfigTxtBox = driver.find_element(By.CSS_SELECTOR,"#form-edit input")
editConfigTxtBox.send_keys(Keys.BACKSPACE)
#alow video and audio
editConfigTxtBox.send_keys("0")
saveConfigBtn = driver.find_element(By.CSS_SELECTOR, "#prefs tr:nth-child(1) td.cell-edit button")
saveConfigBtn.click()
#reload about:preferences#privacy url
driver.get("about:preferences#privacy")
#find autoplay settings button
autoplaySetngsBtn = driver.find_element(By.ID,"autoplaySettingsButton")
autoplaySetngsBtn.click()
driver.get("https://www.mlb.com/video/rockies-black-agree-on-extension")
time.sleep(5)
ROOT_DIR = os.path.dirname(os.path.dirname(__file__)) # This is your Project Root ehere we save the screenshot
timeOfScreenshot = datetime.now()
timeOfScreenshot.isoformat()
timeOfScreenshot = datetime.datetime.now()
timeOfScreenshot.now()
driver.save_screenshot("/Users/865419/PycharmProjects/TutorialTestAutoplaySettingsWorking/AllowedVideo&Audio -"+timeOfScreenshot.isoformat()+".png")
driver.quit()