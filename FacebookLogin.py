from selenium import webdriver
from getpass import getpass

user_name = input("Enter your username or mobile number : ")
your_password =  getpass("enter your password : ")
#print(your_password)
# connect to chrome
driver = webdriver.Chrome()
# go to facebook homepage
driver.get('https://www.facebook.com/')

# find username box and fill it
username_box = driver.find_element_by_id('email')
username_box.send_keys(user_name)
# find password box and fill it
password_box = driver.find_element_by_id('pass')
password_box.send_keys(your_password)

# find login box and submit
login_btn = driver.find_element_by_id('u_0_4')
login_btn.submit()

