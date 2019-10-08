from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

user_name = input("Enter user name : ")

input("Press any key after scanning QR code : ")

user_box = driver.find_element_by_xpath('//span[@title = "{}"]'.format(user_name))
user_box.click()

msg_box = driver.find_element_by_class_name('_13mgZ')
print("Press quit to exit chat\n")
while True:
    msg = input("Enter your message : ")
    if msg!='quit':
        msg_box.send_keys(msg)
        btn = driver.find_element_by_class_name('_3M-N-')
        btn.click()
        
    elif msg=='quit':
        print("Task compeleted")
        break