#!/bin/env python2.7

# Uses a webdriver
# Place chrome driver binary on Desktop
# Binary used here: https://www.sendspace.com/file/b5bkei
# Binary/Chrome version may give errors - try different binaries here: http://chromedriver.storage.googleapis.com/index.html
import os, json, requests
from selenium import webdriver
from requests.utils import dict_from_cookiejar
email=raw_input('Email: ')
tokenContainer=[]
driverBin=os.path.expanduser("~/Desktop/chromedriver")
driver=webdriver.Chrome(driverBin)
driver.get('https://accounts.snapchat.com/accounts/password_reset_request')
field=driver.find_element_by_name('emailaddress')
field.clear()
field.send_keys(email)
driver.switch_to_frame('undefined')
token_value = driver.find_element_by_id('recaptcha-token').get_attribute('value')
driver.switch_to_default_content()
print 
print 'User must solve Captcha!!'
print 'Come back to this terminal once it has been solved and press Enter'
print
raw_input('')
count=0
flag=True
while flag==True:
	driver.switch_to.frame(count)
	try:
		tokenContainer.append(driver.find_element_by_id('recaptcha-token').get_attribute('value'))
		if len(tokenContainer)>1:
			flag=False
	except:
		pass
	driver.switch_to_default_content()
	count+=1
"""
for i in tokenContainer:
    print i
"""
new_token_value= tokenContainer[-1]
driver.switch_to_default_content()
print new_token_value
xsrfObj=driver.find_element_by_id('reset-password-root')
xsrf_token=xsrfObj.get_attribute('data-xsrf')
print xsrf_token
driver.quit()

session=requests.session()
session.cookies.clear();
url='https://accounts.snapchat.com/accounts/password_reset_request'
print "Making recaptcha POST with email..."
headers={
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'accept-encoding':'gzip, deflate, sdch, br',
    'accept-language':'en-US,en;q=0.8',
    'content-type':'application/x-www-form-urlencoded',
    'cookie':'xsrf_token='+xsrf_token,
    'origin':'https://accounts.snapchat.com',
    'referer':'https://accounts.snapchat.com/',
    'upgrade-insecure-requests':'1',
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    #'x-api-key':'88f3559a58cc43f59f6f2f35af663470'  --not always needed? check if response is good without - make second attempt with if needed
}
data={
    'emailaddress':email,
    'g-recaptcha-response':new_token_value,
    'xsrf_token':xsrf_token
}
r=session.post(url,data=data,headers=headers)
print r.status_code
print r.url
print r.content
