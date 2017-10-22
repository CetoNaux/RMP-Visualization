# Web scrapper of 'RateMyProfessor' made for OSU students
# This program is used to scrape all OSU professors corresponding to departments.  It outputs a text file that would be used 
# to build a data base file
# Author: Yanbo Du, Ruihan Tong, Hui Li, Shichun Xuan
from selenium import webdriver
from ProfClass import Prof
import time
import os
import random


if __name__ == '__main__':
    #open an ouput file
    f = open('osuRate.txt', 'w')
    start =time.clock()
    #set up chrome driver
    path_to_chrome = '/Users/Ruihan Tong/Desktop/chromedriver.exe'
    browser = webdriver.Chrome(executable_path = path_to_chrome);
    url = 'http://www.ratemyprofessors.com/search.jsp?queryBy=schoolId&schoolName=Brigham+Young+University&schoolID=135&queryoption=TEACHER'
    #open the webpage
    browser.get(url)
    browser.maximize_window()
    #scapeInfo is an list that contains 152 list elements
    scrapeInfo=[]
    #depts is a list that contains all department
    depts=[]
    browser.refresh
    #scape all departments name and save them in depts
    if(browser.find_element_by_xpath('//*[@id="cookie_notice"]/a[1]').is_displayed()):
        browser.find_element_by_xpath('//*[@id="cookie_notice"]/a[1]').click()
        browser.refresh()

        # click dropdown button
        cross = browser.find_element_by_xpath('//*[@id="mainContent"]/div[1]/div/div[3]/div/div/span/span[2]')
        if(cross.is_displayed()):
            cross.click()
        browser.find_element_by_xpath('//*[@id="mainContent"]/div[1]/div/div[3]/div/div/span').click()

        # select dept names
        deptNames = browser.find_elements_by_class_name("dropdown-menu")
        for dept in deptNames:
            depts=dept.text  
    depLists=depts.split('\n')
    print (depLists[1])
    i=1
    browser.refresh()

    #literates all department to get professors info
    while(i<50):
        try:
            browser.refresh()

            

            # click dropdown button
            cross = browser.find_element_by_xpath('//*[@id="mainContent"]/div[1]/div/div[3]/div/div/span/span[2]')
            if(cross.is_displayed()):
                cross.click()
            browser.find_element_by_xpath('//*[@id="mainContent"]/div[1]/div/div[3]/div/div/span').click()

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
            profList=[]
            str1=[]
            for name in names:
                str1=name.text.split("\n")
            m=0

            if (len(str1)>1):
                while(m<len(str1)/3):
                    profInfo = Prof(depLists[i-1],str1[3*m],str1[3*m+1],str1[3*m+2])
                    f.write(profInfo.department+" "+profInfo.name+" "+profInfo.score+" "+profInfo.numberRate+"\n")
                    profList.append(profInfo)
                    m+=1
                scrapeInfo.append(profList)

            time.sleep(3)
            i = i + 1
        except:
            browser.refresh()        
    end = time.clock()
    print('Running time: %s Seconds'%(end-start))
    f.close(