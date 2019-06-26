from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://web.whatsapp.com/")
name = input("Enter target user's name.")
count = int(input("Enter count."))
message = input("Enter message.")
input("Scan the QR through your smartphone and then press enter key to continue.")
searchBox = driver.find_element_by_xpath('//input[@title="Search or start new chat"]')
searchBox.clear()
searchBox.send_keys(name)
searchBox.send_keys(Keys.ENTER)
for i in range(count):
    messageBox = driver.find_element_by_xpath('//div[@spellcheck="true"][@contenteditable="true"]')
    messageBox.send_keys(message)
    messageBox.send_keys(Keys.ENTER)
driver.quit()
