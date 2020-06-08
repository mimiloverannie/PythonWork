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


# username & password
# <label class="custIdType" for="personlType">身分證</label>
# <input class="idmember pid form-input" maxlength="10" type="text" id="pid" name="pid" value="">
# <input id="startStation" type="text" name="startStation" data-autocomplete="station" class="startStation ui-autocomplete-input" placeholder="出發站" value="" autocomplete="off">
# <input id="endStation" type="text" name="endStation" data-autocomplete="station" class="endStation ui-autocomplete-input" placeholder="抵達站" value="" autocomplete="off">
# <label class="btn btn-lg btn-linear active"> <input type="radio" name="tripType" value="ONEWAY" title="單程" checked="checked"></label>
# <label class="btn btn-lg btn-linear"><input type="radio" value="ROUNDTRIP" title="去回" id="tripType1" name="tripType"></label>
# <input class="normalSeat seatQty" maxlength="3" id="normalQty" name="normalQty" value="1" aria-required="true" aria-invalid="false">

# <input type="text" data-plugin="datepicker" class="rideDate" placeholder="YYYY/MM/DD" id="rideDate1" data-date-start-date="+0d" name="ticketOrderParamList[0].rideDate" value="2019/08/13" aria-required="true" aria-invalid="false">
# <select id="startTime1" class="form-control timeRng" data-trip="1" name="ticketOrderParamList[0].startTime" aria-invalid="false"> <option value="00:00">00:00</option><option value="00:30">00:30</option>
# <select id="endTime1" class="form-control timeRng" data-trip="1" name="ticketOrderParamList[0].endTime"><option value="00:00">00:00</option>
# <label for="ticketOrderParamList0.trainTypeList1" class="btn btn-lg btn-linear"><input type="checkbox" class="trainTypeList" autocomplete="off" value="1" id="ticketOrderParamList0.trainTypeList1" name="ticketOrderParamList[0].trainTypeList" aria-required="true" aria-describedby="ticketOrderParamList[0].trainTypeList-error"><input type="hidden" name="_ticketOrderParamList[0].trainTypeList" value="on">太魯閣</label>
# <label for="ticketOrderParamList0.trainTypeList2" class="btn btn-lg btn-linear"><input type="checkbox" class="trainTypeList" autocomplete="off" value="2" id="ticketOrderParamList0.trainTypeList2" name="ticketOrderParamList[0].trainTypeList"><input type="hidden" name="_ticketOrderParamList[0].trainTypeList" value="on">普悠瑪</label>


# <input type="text" data-plugin="datepicker" class="rideDate" placeholder="YYYY/MM/DD" id="rideDate2" data-date-start-date="+0d" name="ticketOrderParamList[1].rideDate" value="">
# <select id="startTime2" class="form-control timeRng" data-trip="2" name="ticketOrderParamList[1].startTime" aria-invalid="false"><option value="00:00">00:00</option>
# <select id="endTime2" class="form-control timeRng" data-trip="2" name="ticketOrderParamList[1].endTime" aria-invalid="false"><option value="00:00">00:00</option>



Userid = ('F123456789')
startStation = ('0990')
endStation = ('6000')
number = 4
date1 = "20200729"
time1 = "06:00"
time2 = "12:00"
date2 = "20200802"
time3 = "13:30"
time4 = "17:00"


Browser.get(WebUrl)
Browser.find_element_by_id('pid').send_keys(Userid)
Browser.find_element_by_id('startStation').send_keys(startStation)
Browser.find_element_by_id('endStation').send_keys(endStation)
Browser.find_element_by_xpath('//*[@id="queryForm"]/div[1]/div[1]/div[5]/div[2]/label[2]').click()
Browser.find_element_by_xpath('//*[@id="queryForm"]/div[1]/div[1]/div[6]/div[2]/label[2]').click()
Browser.find_element_by_id('normalQty').clear()
Browser.find_element_by_id('normalQty').send_keys(number)

Browser.find_element_by_id('rideDate1').clear()
Browser.find_element_by_id('rideDate1').send_keys(date1)
s = Select(Browser.find_element_by_id('startTime1'))
s.select_by_value(time1)
s = Select(Browser.find_element_by_id('endTime1'))
s.select_by_value(time2)
Browser.find_element_by_xpath('//*[@id="queryForm"]/div[2]/div[3]/div[1]/div[2]/label[1]').click()
Browser.find_element_by_xpath('//*[@id="queryForm"]/div[2]/div[3]/div[1]/div[2]/label[2]').click()
Browser.find_element_by_xpath('//*[@id="queryForm"]/div[2]/div[3]/div[1]/div[2]/label[3]').click()

Browser.find_element_by_id('rideDate2').clear()
Browser.find_element_by_id('rideDate2').send_keys(date2)
s = Select(Browser.find_element_by_id('startTime2'))
s.select_by_value(time3)
s = Select(Browser.find_element_by_id('endTime2'))
s.select_by_value(time4)
Browser.find_element_by_xpath('//*[@id="queryForm"]/div[3]/div[3]/div[1]/div[2]/label[1]').click()
Browser.find_element_by_xpath('//*[@id="queryForm"]/div[3]/div[3]/div[1]/div[2]/label[2]').click()
Browser.find_element_by_xpath('//*[@id="queryForm"]/div[3]/div[3]/div[1]/div[2]/label[3]').click()
