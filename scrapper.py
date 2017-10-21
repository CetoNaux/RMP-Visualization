# Web scrapper of 'RateMyProfessor' made for OSU students
# Author: Yanbo Du
from selenium import webdriver
import time
import os
import random


if __name__ == '__main__':

    start =time.clock()

    path_to_chrome = '/Users/Dell/Desktop/chromedriver.exe'
    browser = webdriver.Chrome(executable_path = path_to_chrome);

    url = 'http://www.ratemyprofessors.com/search.jsp?queryBy=schoolId&schoolName=The+Ohio+State+University&schoolID=724&queryoption=TEACHER'
    browser.get(url)
    browser.maximize_window()

    if(browser.find_element_by_xpath('//*[@id="cookie_notice"]/a[1]').is_displayed()):
        browser.find_element_by_xpath('//*[@id="cookie_notice"]/a[1]').click()

    i = 1;
    while(i<153):

        browser.refresh()

        # click dropdown button
        cross = browser.find_element_by_xpath('//*[@id="mainContent"]/div[1]/div/div[3]/div/div/span/span[2]')
        if(cross.is_displayed()):
            cross.click()
        browser.find_element_by_xpath('//*[@id="mainContent"]/div[1]/div/div[3]/div/div/span').click()

        # select dept names
        #deptNames = browser.find_elements_by_class_name("dropdown-menu")
        #for dept in deptNames:
            #print(dept.text)

        #1-152 department
        browser.find_element_by_xpath('//*[@id="mainContent"]/div[1]/div/div[3]/div/div/ul/li[%s]' % i).click()

        # load all prof in thw department
        while(1):
            LoadMore = browser.find_element_by_xpath('//*[@id="mainContent"]/div[1]/div/div[5]/div/div[1]')
            # left side scroll down
            browser.execute_script("arguments[0].scrollIntoView();", LoadMore)
            if(LoadMore.text == 'LOAD MORE'):
                # load more prof
                LoadMore.click()
            else:
                break

            time.sleep(1)

        # select prof name
        names = browser.find_elements_by_class_name("result-list")

        for name in names:
            print(name.text)

        i = i + 1

        print('\n')
        time.sleep(random.random())

    end = time.clock()

    print('\n')
    print('Running time: %s Seconds'%(end-start))
