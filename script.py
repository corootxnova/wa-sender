# -*- coding: utf-8 -*-
try:
	from selenium import webdriver
	from time import sleep
	from colored import fg, attr
except:
	print(' >>> Install Selenium And Colored > pip install selenium - pip install colored')
	sleep(15)

print('''

db   d8b   db  .d8b.         .d8888. d88888b d8b   db d8888b. d88888b d8888b. 
88   I8I   88 d8' `8b        88'  YP 88'     888o  88 88  `8D 88'     88  `8D 
88   I8I   88 88ooo88        `8bo.   88ooooo 88V8o 88 88   88 88ooooo 88oobY' 
Y8   I8I   88 88~~~88 C8888D   `Y8b. 88~~~~~ 88 V8o88 88   88 88~~~~~ 88`8b   
`8b d8'8b d8' 88   88        db   8D 88.     88  V888 88  .8D 88.     88 `88. 
 `8b8' `8d8'  YP   YP        `8888Y' Y88888P VP   V8P Y8888D' Y88888P 88   YD 
                                                                              
                                                                              
''')
upload_num = input(fg('yellow_4b') + " >>> Enter Numbers List With Country Code : ")
upload_msg = input(fg('yellow_4b') + " >>> Enter Message Path : ")
delay = int(input(fg('yellow_4b') + " >>> Enter Delay : "))
numbers = open(upload_num, 'r')
message = open(upload_msg, 'r', encoding='utf-8').read()
ok = '\n'
msg = str(message) + str(ok)
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
input(fg('light_red') + " \n[>] Press Enter When You Login Successfully In Whatsapp [<]\n")
for num in numbers:
    driver.get("https://api.whatsapp.com/send/?phone=" + num)
    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div/a").click()
    sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div/a").click()
    sleep(15)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]").send_keys(msg)
    print(fg('dark_cyan') + " >>> Sent Successfully To " + num)
    sleep(int(delay))
driver.quit()
