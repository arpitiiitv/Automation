from selenium import webdriver
from getpass import getpass

usr = input("Enter Email/Mobile number   : ")
psw = getpass("Enter password   :")
# connect to chrome
driver = webdriver.Chrome()
# go to flipkart homepage
driver.get('https://www.flipkart.com/')