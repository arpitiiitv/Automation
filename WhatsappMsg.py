from selenium import webdriver
from time import sleep

# Connecting to Chrome
driver = webdriver.Chrome()
# opening whatsapp web
driver.get('https://web.whatsapp.com/')

# taking name of group or user whom we want to send sms
name = input('Enter the name of user or group   :  ')
# taking what sms we want to send
msg = input("Enter the message you want to send  :  ")
# taking howmany times we want to send
connt = int(input('Howmany msg  :  '))

# verification of QR code scanning
input('Input anything after scanning QR code : ')

# finding our target user or group
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
# finding msg box
msg_box = driver.find_element_by_class_name('_13mgZ')

#i=0
for i in range(connt):
#while True:
    msg_box.send_keys(i+1,'th time ', msg)
    btn = driver.find_element_by_class_name('_3M-N-')
    btn.click()
    sleep(1)
    #i=i+1
    
