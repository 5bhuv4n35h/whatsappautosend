
from selenium import webdriver
b = webdriver.Firefox()
b.get('http://web.whatsapp.com')
input("contact name")
elem = b.find_element_by_xpath('//span[contains(text(),"contact name")]')
elem.click()
elem1 = b.find_elements_by_class_name('input')
counter =0
while counter < 900:
    counter= counter +1
    elem1[1].send_keys('sorry')
    b.find_element_by_class_name('send-container').click()
