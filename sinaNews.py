#使用Selenium也可以進行Cookies操作
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
#C:\Program Files\Python36\Lib\site-packages\selenium\webdriver\common\service.py文件，
#添加代碼from win32process import CREATE_NO_WINDOW
#在start 方法中stderr=self.log_file,後面加上代碼：creationflags=CREATE_NO_WINDOW,
#//*[@id="liveList01"]/div[1]
#//*[@id="liveList01"]/div[2]

class SinaNews():
      def __init__(self):
            self.count = 1
            self.url='http://finance.sina.com.cn/7x24/'
            option = webdriver.ChromeOptions()
            option.add_argument("headless")
            self.driver = webdriver.Chrome(chrome_options=option)#使用以下方法在运行的时候可以不打开浏览器，运行速度杠杠的
            self.spider()
      def __close__(self):
            print('spider will be closed.')
            print("**"*50)
            self.dirver.close()

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
                  time.sleep(random.choice(range(45,145)))
                  #self.spider()
      
      
      def read_file(self):
            MPP = {}
            with open("data/news",'r',1,'gbk') as file:
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
                  
                        
      
