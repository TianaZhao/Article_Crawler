# -*- coding: utf-8 -*-
"""
@Author: zhaowantian
@Create Date:
@Description:
"""
from selenium import webdriver
import time
import pyautogui
import os
from bs4 import BeautifulSoup
import requests
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def write_into_file(content, path):
    # todo: write content to file with path
    pass

def tranverse_issues():
    try:
        issues = browser.find_elements("xpath",'.//*[@class="loi__cover_image"]')
        idx = 0
        # tranverse issue
        # for each issue, go in to it to get the articles
        while idx < len(issues):

            # comment this part or modify the parameter if using the monitor or window size is changed
            if (idx) % 3 == 0:
                browser.execute_script("window.scrollBy(0,300)")

            time.sleep(0.7)

            issues = browser.find_elements("xpath", './/*[@class="loi__cover_image"]')
            issue = issues[idx]
            issue.click()

            # try to scroll but these code doesn't work
            # issue.location_once_scrolled_into_view
            # issues = browser.find_elements("xpath", './/*[@class="loi__cover_image"]')
            # issue = issues[idx]
            # actions = ActionChains(browser)
            # actions.move_to_element_with_offset(issue, 5, 5)
            # actions.perform()

            # try to handle continue but the cutton is not interactable
            # continue_button = browser.find_element("xpath", './/*[@id="gdpr-con-btn"]')
            # if continue_button != None:
            #     print(continue_button)
            #     browser.execute_script("arguments[0].click();", continue_button)
                # continue_button.click()

            # parse data from html directly.
            # issue_item = []
            # page_src = browser.page_source
            # soup = BeautifulSoup(page_src, "html.parser")
            # traverse issue one by one
            # if soup.find_all(class_="issue-item clearfix") is None:
            #     print("is none")
            # else:
            #     issue_item = list(soup.find_all(class_="issue-item clearfix"))
            # for article in issue_item:
            #     time.sleep(0.8)
            #     print(article)
            # article_names = list(soup.find_all(class_="issue-item_title"))

            article_names = browser.find_elements("xpath", './/*[@class="issue-item_title"]//a[@title]')
            for article_name in article_names:
                print(article_name.get_attribute("title"))
            browser.back()
            idx += 1
            time.sleep(0.5)
    except Exception as e:
        print(e)




if __name__ == '__main__':
    # add extension to avoid windo0ws.navigator.webdriver anti-robot sys
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

    # open the website
    browser = webdriver.Chrome(chrome_options=chrome_options, executable_path="/usr/local/bin/chromedriver")

    # try modify window size but the zoom out doesn't work
    # browser.set_window_size(1500,1000)
    # browser.execute_script("document.body.style.zoom='0.5'")

    browser.get("https://pubs.acs.org/")
    time.sleep(2.1)

    # enable this if running in campus
    # login_button = browser.find_element("xpath",'.//*[@class="close paringAffClose"]')
    # if login_button != None:
    #     login_button.click()
    # time.sleep(1.1)

    # find the publication button and click it
    public_button = browser.find_element("xpath", './/*[@data-widget-id="6808faec-02bf-4a81-85d3-95e1fe96c4a4"]/div[1]/div[1]/div[2]/div[3]/a[1]')
    public_button.click()

    #find the acs journal button and click it
    time.sleep(1.2)
    acs_button = browser.find_element("xpath", './/*[@class="pub_journals journals cat_analytical cat_app cat_biological cat_matscieng "]')
    acs_button.click()

    #find all issue button and click it
    time.sleep(1.3)
    list_issue_button = browser.find_element("xpath",'.//*[@id="nav-loi"]')
    list_issue_button.click()

    time.sleep(1.5)
    tranverse_issues()


