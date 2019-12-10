from bs4GetWeatherToday import bs4GetWeatherToday
from bs4GetWeather7d import bs4GetWeather7d
from model.getUrlSource import getUrlSource
from model.getCityMessage import getCityMessage
import time
import random
def get_config():
      with open(r'config/mycity.txt','r',1,'gbk') as file:
            pcmap = {}
            for f in file.readlines():
                  try:
                        a = f.split(":")
                        pcmap.fromkeys(a[0])
                        pcmap[a[0]] = a[1]
                  except Exception as e:
                        continue
      return pcmap
class weaInfo2files:
      def __init__(self):
            self.city = get_config()['city']
            
            self.code = getCityMessage(r'model/city.json',self.city).getCode()
            self.url1d = 'http://www.weather.com.cn/weather1d/{}.shtml'.format(self.code)
            self.url7d = 'http://www.weather.com.cn/weather/{}.shtml'.format(self.code)
            self.text1d = getUrlSource(self.url1d).getUrlText()
            self.text7d = getUrlSource(self.url7d).getUrlText()
            self.tips_path = (r'data/tips')
            self.today_path = (r'data/todayWea')
            self.d7day_path = (r'data/7daysWea')
            while True:
                  self.writeTips()
                  self.write1dWea()
                  self.write7dWea()
                  sleeptime = random.choice(range(30,1000))
                  print(self.city,sleeptime)
                  time.sleep(sleeptime)
            return None
      
      def writeTips(self):
            tips = bs4GetWeatherToday(self.text1d).getLifeTips()
            try:
                  with open(self.tips_path,'w',1,'gbk') as file:
                        for i in tips:
                              for k,v in i.items():
                                    file.write(str(k)+':'+str(v)+'\n')
            except Exception as e:
                  print("生活tips出现某个异常")
      def write1dWea(self):
            temp = bs4GetWeatherToday(self.text1d)
            weather1d = temp.getToday()
            try:
                  with open(self.today_path,'w',1,'gbk') as file:
                        for i in weather1d:
                              for k,v in i.items():
                                    file.write(str(k)+'@'+str(v)+'\n')
                        #file.write(weather1d)
            except Exception :
                  print("获取当日天气出现某个问题")
      def write7dWea(self):
            weather7d = bs4GetWeather7d(self.text7d).get7d()
            try:
                  with open(self.d7day_path,'w',1,'gbk') as file:
                        for i in weather7d:
                              cot = 1
                              for k,v in i.items():
                                    if cot ==6: 
                                          file.write(str(k)+':'+str(v)+'\n')
                                    else:
                                          file.write(str(k)+':'+str(v)+',')
                                          cot += 1
                        #file.write(weather7d)
            except Exception:
                  print('获取7天天气出现某个问题')

if __name__ == '__main__':
      
      weaInfo2files()                  
                        
