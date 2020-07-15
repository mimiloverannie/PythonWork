# !/usr/bin/python
# coding:utf-8

# /Users/pennylai/Documents/train.py
# to book train ticket


import pytest
import time
import json
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


Browser = webdriver.Chrome('./chromedriver')

# go to web
WebUrl = ('https://tip.railway.gov.tw/tra-tip-web/tip/tip001/tip121/query')
Browser.get(WebUrl)


Userid = ('F123456789')
startStation = ('6000')
endStation = ('1000')
number = 4
date1 = "20200802"
time1 = "13:30"
time2 = "20:00"



Browser.get(WebUrl)
Browser.find_element_by_id('pid').send_keys(Userid)
Browser.find_element_by_id('startStation').send_keys(startStation)
Browser.find_element_by_id('endStation').send_keys(endStation)
Browser.find_element_by_xpath('//*[@id="queryForm"]/div[1]/div[1]/div[5]/div[2]/label[1]').click()
Browser.find_element_by_xpath('//*[@id="queryForm"]/div[1]/div[1]/div[6]/div[2]/label[2]').click()
Browser.find_element_by_id('normalQty').clear()
Browser.find_element_by_id('normalQty').send_keys(number)

# ONE WAY content
Browser.find_element_by_id('rideDate1').clear()
Browser.find_element_by_id('rideDate1').send_keys(date1)
s = Select(Browser.find_element_by_id('startTime1'))
s.select_by_value(time1)
s = Select(Browser.find_element_by_id('endTime1'))
s.select_by_value(time2)
Browser.find_element_by_xpath('//*[@id="queryForm"]/div[2]/div[3]/div[1]/div[2]/label[1]').click()
Browser.find_element_by_xpath('//*[@id="queryForm"]/div[2]/div[3]/div[1]/div[2]/label[2]').click()
Browser.find_element_by_xpath('//*[@id="queryForm"]/div[2]/div[3]/div[1]/div[2]/label[3]').click()
