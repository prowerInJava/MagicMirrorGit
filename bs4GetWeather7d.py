import html5lib
from bs4 import BeautifulSoup as bs
import datetime
from datetime import time

from model.getCityMessage import getCityMessage
from model.getUrlSource import getUrlSource

class bs4GetWeather7d():
      def __init__(self,text):
            self.text = text
            return None
      def get7d(self):
            soup = bs(self.text,'html5lib')
            div_tag = soup.find('div','c7d')
            ul = div_tag.find('ul','t clearfix') #find('ul',{'class':'t clearfix'})
            li  = ul.find_all('li')
            final7d = []
            ds = 0
            #now = datetime.datetime.now().strftime('%A %Y-%m-%d %H:%M:%S')
            for day in li:
                  temp = {}
                  #date = day.find('h1').string.split('日')[0] #找到日期.split('(')[0]
                  delta = datetime.timedelta(days = ds)
                  date = datetime.datetime.now() + delta
                  temp['日期'] = date.strftime('%A %Y-%m-%d').lower()
                  ds += 1
                  inf = day.find_all('p')
                  windf = inf[0].string
                  temp['天气']=windf #将第一个p中的内容天气情况加到temp中
                  if inf[1].find('span') is None:
                        tem_highest = None
                  else :
                        tem_highest = inf[1].find('span').string
                  tem_lowest = inf[1].find('i').string.replace('℃','')
                  temp['最高温'] = tem_highest
                  temp['最低温'] = tem_lowest
                  wind = inf[2].find('i').string
                  if '转' in wind:
                        wind = wind.split('转')[0]
                  windx = inf[2].find('em').find_all('span')[0].attrs['title']
                  temp['风力'] = wind
                  temp['风向'] = windx
                  final7d.append(temp)    
            return final7d
if __name__ == '__main__':
      code = getCityMessage('model/city.json','haimen').getCode()
      #print(code)
      url = 'http://www.weather.com.cn/weather/{}.shtml'.format(code)
      print(url)
      text = getUrlSource(url).getUrlText()
      #print(text)
      w7d = bs4GetWeather7d(text).get7d()
      print (w7d)
            
            
