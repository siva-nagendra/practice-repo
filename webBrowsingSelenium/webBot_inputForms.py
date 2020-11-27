'''
Building a bot for filling forms in the web.
'''
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
messgeBox = driver.find_element_by_xpath('//*[@id="user-message"]')
messgeBox.send_keys("Hey Watup")
showButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showButton.click()

message1Box = driver.find_element_by_xpath('//*[@id="sum1"]')
message1Box.send_keys("100")
message2Box = driver.find_element_by_xpath('//*[@id="sum2"]')
message2Box.send_keys("25000")
totalButton = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
totalButton.click()