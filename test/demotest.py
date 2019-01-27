# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["deviceName"] = "asd"
caps["platformName"] = "android"
caps["appPackage"] = "de.bmw.connected.cn.int"
caps["appActivity"] = "de.bmw.connected.lib.eula.views.AcceptEulaActivity"
caps["noReset"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)


el1 = driver.find_element_by_id("de.bmw.connected.cn.int:id/eula_read_terms_compound_button")
el1.click()

el2 = driver.find_element_by_id("de.bmw.connected.cn.int:id/eula_accept_button")
el2.click()

driver.quit()