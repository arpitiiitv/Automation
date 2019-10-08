from selenium import webdriver

# Connecting to Chrome
driver = webdriver.Chrome()
# opening whatsapp web
driver.get('https://web.whatsapp.com/')

# taking number of users
no_of_users = int(input("Enter number of users :"))
names=[]
for i in range(no_of_users):
    print("Enter ",i+1, "th user name : ")
    x=input()
    names.append(x)
    

# verification of QR code scanning
input('Input anything after scanning QR code')

for i in range(len(names)):
    users = driver.find_element_by_xpath('//span[@title = "{}"]'.format(names[i]))
    users.click()
    msg_box = driver.find_element_by_class_name('_13mgZ')
    print('Message for ', names[i] + "  : ",end=" ")
    msg = input()
    msg_box.send_keys(msg)
    btn = driver.find_element_by_class_name('_3M-N-')
    btn.click()

