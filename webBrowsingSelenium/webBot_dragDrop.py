'''
Building a bot for drag and drop operations in the web.
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
sd_dict = {
    '//*[@id="box5"]' : '//*[@id="box105"]',
    '//*[@id="box3"]' : '//*[@id="box103"]',
    '//*[@id="box7"]' : '//*[@id="box107"]',
    '//*[@id="box6"]' : '//*[@id="box106"]',
    '//*[@id="box4"]' : '//*[@id="box104"]',
    '//*[@id="box2"]' : '//*[@id="box102"]',
    '//*[@id="box1"]' : '//*[@id="box101"]'
}

for key, value in sd_dict.items():
    source = driver.find_element_by_xpath(key)
    destination = driver.find_element_by_xpath(value
    )
    actions = ActionChains(driver)
    actions.drag_and_drop(source, destination).perform()
