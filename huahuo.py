# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import random
import time

url = "https://www.say-huahuo.com/answer/#/"

option = webdriver.ChromeOptions()
# 防止检测
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option("useAutomationExtension", False)
driver = webdriver.Chrome(r".\chromedriver.exe", options=option)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                       {"source": "Object.defineProperty(navigator,'webdriver',{get:()=>undefined})"})
driver.get(url)
condition = EC.visibility_of_element_located(
    (By.XPATH, '//h2[@id="start-exam"]'))  # 看看有没有加载完成
WebDriverWait(driver=driver, timeout=5, poll_frequency=0.5).until(condition)  # 记载完成

start_exam = driver.find_element_by_xpath('//h2[@id="start-exam"]')
start_exam.click()  # 点击开始答题
buttons = ['//*[@id="router-view-wrapper"]/div/label[2]/span[1]/span',
           '//*[@id="router-view-wrapper"]/div/label[3]/span[1]/span',
           '//*[@id="router-view-wrapper"]/div/label[4]/span[1]/span',
           '//*[@id="router-view-wrapper"]/div/label[5]/span[1]/span']
# //*[@id="router-view-wrapper"]/div/label[2]/span[1]/span
driver.implicitly_wait(5)
while True:
    # 一共20选项
    try:
        ele = driver.find_element_by_xpath('//h3[@id="maple-h2" and @style="cursor: pointer;"]')
        ele.click()  # 点击再来一次
        driver.implicitly_wait(5)
        break  # 找到再来一次就退出
    except NoSuchElementException:
        #
        pass

    xpath = random.choice(buttons)
    button = driver.find_element_by_xpath(xpath)
    button.click()
    # 点击下一题
    next_button = driver.find_element_by_xpath('//*[@id="next-btn"]/span')
    next_button.click()
    time.sleep(0.1)
