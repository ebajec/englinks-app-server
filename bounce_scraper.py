from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json
from cryptography.fernet import Fernet

class PushStack:
    def __init__(self,size):
        self.size = size
        self.body = [None]*size

    def push(self,x):
        last = self.body[self.size-1]

        for i in range(0,self.size-1):
            self.body[i+1] = self.body[i]

        self.body[0] = x

        return last
    
    def get(self,n):
        return self.body[n]

def find_three_digits(eventTitle):

    for i in range(0,len(eventTitle) - 2):
        substring = eventTitle[i:i+3]

        if substring.isdigit():
            return substring
    return 'none'


#NOTE: this will not work unless it has a valid password for a bounce account
f = open('password-username.txt','r')

temp = f.read().split(',')

username = temp[0]
password = temp[1]

#open chrome
driver = webdriver.Chrome()

driver.get("https://www.bouncelife.com/login?from=%2Fprofile%2F5e87a4794829bb0011ce7480")
elem = driver.find_element(By.TAG_NAME, "input")
elem.clear()

#sign in
elem.send_keys(username)
elem.send_keys(Keys.RETURN)
time.sleep(5)

elem = driver.find_element(By.NAME, "password")

elem.send_keys(password)
elem.send_keys(Keys.RETURN)

time.sleep(3)

#find button    
elem = driver.find_element(By.CSS_SELECTOR, "[data-testid='button-skip']")

elem.click()

#find hosted tab
elem = driver.find_element(By.CSS_SELECTOR,'[class="EventContainer_tab__kxLkd"]')
elem.click()

html = driver.page_source

driver.close()

soup = BeautifulSoup(html,'lxml')

eventList = soup.find(id = 'eventList')

first_event_link = eventList.find_next()
other_events = first_event_link.find_next_siblings()
eventsHTML = [first_event_link] + other_events

eventData = [("events_misc.txt",[]),("events_first_year.txt",[]),("events_upper_year.txt",[])]



#this is for a bit of a hack to simplify things
year = 2023
date_stack = PushStack(2)

for event in eventsHTML:
    
    #first element is date + time, second is title, third is just "Hosted by EngLinks"
    data = event.find_next().find_next_siblings()

    eventInfo = {'title':'', 'date':'','month':'','year':'','time':''}

    title = data[1].string
    date = data[0].string[3:7]
    month = data[0].string[:3]    

    date_stack.push(month.lower())

    if (date_stack.get(1) == 'jan' and date_stack.get(0) != 'jan'):
        year -= 1

    eventInfo['title'] = title
    eventInfo['date'] = int(date.replace(' ',''))
    eventInfo['month'] = month
    eventInfo['year'] = year
    eventInfo['time'] = data[0].string[7:]
    
    course_code = find_three_digits(title)
    
    if (course_code == 'none'):
        eventData[0][1].append(eventInfo)
    elif (int(course_code[0])) <= 1:
        eventData[1][1].append(eventInfo)
    else:
        eventData[2][1].append(eventInfo)
    
for data in eventData:
    f = open(data[0],'w')
    json.dump(data[1],f)
    f.close()

    

    