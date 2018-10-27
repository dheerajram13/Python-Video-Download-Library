import urllib
from urllib import urlopen
import os
import re
from selenium import webdriver
import time
import tqdm
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import selenium
import pytube
from selenium.webdriver.remote.webelement import WebElement
from math import ceil
print('\n\n\n\n\n###########Python Video Download Library###########\n\n\n')                    
print('Created By: \n Priyank Patel \n  S.Dheeraj \n Akkshansh Paul \n Rishab Pampattiwar \n###################################################\n') #title sequence

'''User Module'''

#url = input("Please enter the URL: ")
url = "https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos"

text = urlopen(url).read()                                             #accepting the course URL from the user
soup = BeautifulSoup(text, "lxml")
data = soup.findAll('div',attrs={'class':"mediatext"})

data_list=list()
link_list=list()
for div in data:
    links = div.findAll('a')
    for a in links:
        video_links = "https://ocw.mit.edu"+a['href']           #finding the video links using the href tag, here we use beautifulsoup
        link_list.append(video_links)




'''Scrapping module'''


print('.........Download Started..........')
driver=webdriver.Chrome('./chromedriver')               #starting google chrome using selenium webdriver

length=len(link_list)+1

progress_count=100/length
progress_percentage=progress_count


i=1

for link in link_list:
    driver.get(link)                                    # opening the video link
    time.sleep(0.2)
    srcs = driver.find_element_by_id("embed_1_youtube").get_attribute("src")  #finding the video element by its id
        #driver.get(srcs)
    path = '/Users/priyankpatel/Desktop/lecturevideos'              #setting the path for the download directory
    time.sleep(1)
    video_url=list()
    video_url.append(srcs)
    x=srcs.split('?')                       #generating the video url from the embeded video link
    y=x[0].split('/')                       #same
    url='https://youtu.be/'+y[4]            #same
        
    '''Content Module'''
    
    
        
    yt = pytube.YouTube(url)                        #implementig the pytube library
    video=yt.get_videos()
    video = yt.get('mp4','360p')                    #getting the video at desired settings
    l=length-1
    print('Downloading %s out of %s videos'%(i,l))
    i=i+1
    l2=length
    if (i==l2):
        print('progress:100 %')
    else:
        print('progress:'+str(progress_percentage)+'%')                 #used for progress report
        
        
    progress_percentage=progress_percentage+progress_count
    print('')
    video.download(path)                #downloading the video
print("Download complete!")                 #printing the download complete message after all videos are downloaded




