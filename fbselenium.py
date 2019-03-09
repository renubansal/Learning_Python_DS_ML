from selenium import webdriver

#initialize web driver 
driver = webdriver.Chrome()

driver.get("http://www.facebook.com")

elem = driver.find_element_by_name("email")
elem.send_keys("bansal2407@gmail.com");

elem = driver.find_element_by_id('pass')
elem.send_keys("@");

elem = driver.find_element_by_id('loginbutton')
elem.click();


