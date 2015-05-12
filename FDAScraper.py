__author__ = 'Aditya Trivedi'
import requests
from lxml import html
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
#from selenium.webdriver.common.keys import Keys

def USscraper():
    num = ['429489', '384921', '384618','333705']

    for number in num:
        url = 'http://www.fda.gov/MedicalDevices/Safety/ListofRecalls/ucm'+ number +'.htm'
        response = requests.get(url)
        tree = html.fromstring(response.text)
        recalls = tree.xpath('//tr/td/a/linktitle/text()')
        for recall in recalls:
            print recall.encode('utf-8')
    return

def CAscraper():
   nums = [None]*183
   for i in range(183):
       nums[i] = i*20
   for num in nums:
       url = 'http://www.healthycanadians.gc.ca/recall-alert-rappel-avis/search-recherche/simple?s=&plain_text=&f_c[]=41&f_mc=3&js_en=1&page=20&per_page=' + str(num)
       response = requests.get(url)
       tree = html.fromstring(response.text)
       recalls = tree.xpath('//div[@class="margin-bottom-medium word_wrap"]/a/text()')
       for recall in recalls:
           print recall.encode('utf-8')
   return

def UKscraper():
    url = 'https://www.gov.uk/drug-device-alerts?keywords=&alert_type%5B%5D=devices&issued_date%5Bfrom%5D=&issued_date%5Bto%5D='
    response = requests.get(url)
    tree = html.fromstring(response.text)
    recalls = tree.xpath('//li/h3/a/text()')
    for recall in recalls:
        print recall.encode('utf-8')
    return


def AUscraper():
    driver = webdriver.Firefox()
    driver.get("http://apps.tga.gov.au/PROD/SARA/arn-entry.aspx")
    driver.find_element_by_id("disclaimer-accept").click()
    driver.find_element_by_xpath("//select[@name='cmbProductType']/option[@value='d']").click()
    driver.find_element_by_id("submit-button").click()

    elem = driver.find_element_by_name("ctl00$body$PageNext")
    while driver is not None:
        recalls = driver.find_elements_by_xpath("//tr/td/a")
        for recall in recalls:
            print recall.text.encode('utf-8')
        elem.click()
        try:
            elem = driver.find_element_by_id("ctl00_body_PageNext")
        except NoSuchElementException:
            break
    return

CAscraper()