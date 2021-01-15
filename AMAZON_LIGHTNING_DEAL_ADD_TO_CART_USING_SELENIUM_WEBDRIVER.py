from selenium import webdriver
import time
from time import sleep
deal_id=input("Enter Deal ID :")
print('\n')
webdriver_path =r"Your Webdriver Path"
options = webdriver.ChromeOptions()
#options.add_argument('--headless') 
options.add_argument('start-maximized') 
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
options.add_argument('--disable-popup-blocking')
driver=webdriver.Chrome(webdriver_path,options=options)
driver.get("https://amazon.in")
sign_up = driver.find_element_by_id("nav-link-accountList")
sign_up.click()
email_id = driver.find_element_by_id('ap_email')
email_id.send_keys("YOUR MAIL ID")
proceed1 = driver.find_element_by_id('continue')
proceed1.click()
password = driver.find_element_by_id('ap_password')
password.send_keys("YOUR PASSWORD")
proceed2 = driver.find_element_by_id('signInSubmit')
proceed2.click()
sleep(20)
print("login success")
sleep(3)
driver.get("https://www.amazon.in/gp/goldbox/All-deals?gb_edi="+deal_id)
sleep(2)
def add_to_cart():
        while(True):
            try:
                add = driver.find_element_by_id('100'" "*1+deal_id+'-announce')
                add.click()
            except:
                print("trying to add")
add_to_cart() 


