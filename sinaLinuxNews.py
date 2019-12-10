#! /usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display
import time
import random


class SinaNews():
      def __init__(self):
            self.count = 1
            display = Display(visible=0, size=(800, 600))
            display.start()
            profile = webdriver.FirefoxProfile()
            profile.native_events_enabled = False
            self.url='http://finance.sina.com.cn/7x24/'
            self.driver = webdriver.Firefox(profile)
            self.spider()
      def __close__(self):
            print('spider will be closed.')
            print("**"*50)
            self.driver.close()

      def spider(self):
            try:
                  self.driver.get(self.url)#獲取頁面源碼
                  #self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')#拉動滾動條到底
                  self.wait = WebDriverWait(self.driver,10)
                  refresh = self.wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[6]/div/div[1]/div[2]/span/span')))
                  self.driver.set_page_load_timeout(30)
            except Exception as e:
                  print(e)
            while True:
                  with open('data/news','w') as file :
                        file.write("")
                        #print("OK")
                  for i in range (1,11):
                        xpath = '//*[@id="liveList01"]/div[%d]'%i
                        #print(xpath)
                        news = self.driver.find_elements_by_xpath(xpath)
                        #print(len(news))
                        with open('data/news','a') as file:
                              for new in news:
                                    #print(len(news))
                                    file.write(str(new.text)+'\n')
                                    #print(str(i) + new.text)
                  self.write_file()
                  sleeptime = random.choice(range(45,145))
                  print('sina: ',sleeptime)
                  time.sleep(sleeptime)
                  #self.spider()
      
      
      def read_file(self):
            MPP = {}
            with open("data/news",'r') as file:
                  lis = file.readlines()
                  for i in range(len(lis)):
                        if i%2==0:
                              MPP.fromkeys(lis[i].strip())
                              MPP[lis[i].strip()] = lis[i+1].strip()
            """
            for i in range(len(MPP)):
                  print(list(MPP.items())[i][0])
            """
            return MPP
      def write_file(self):
            mymap = self.read_file()
            with open("data/news.txt",'w') as file:
                  key = list(mymap.items())[0][0]
                  line = str(key)+ '***' + str(mymap[key])
                  #print(line)
                  file.write(line) 
                        
if __name__ == '__main__':
       SinaNews()     
