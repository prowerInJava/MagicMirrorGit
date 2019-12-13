import html5lib
from bs4 import BeautifulSoup as bs
import datetime
from datetime import time

from model.getCityMessage import getCityMessage
from model.getUrlSource import getUrlSource

class bs4GetWeatherToday():
      def __init__(self,text):
            self.text = text
            return None
      def getToday(self):
            soup = bs(self.text,'html5lib')
            div_tag = soup.find('div',{'id':'today'}).find('div',{'class':'t'})
            ul = div_tag.find('ul','clearfix')
            lis = ul.findAll('li',{'class' : None})
            today = []
            for li in lis :
                  sun = li.find_all('p')[3]
                  temp = {}
                  temp[li.find('h1').string.split(r'日')[1]] = li.find('p',{'class':'wea'}).text.strip()
                  if li.find('h1').string.split(r'日')[1] =='白天':
                        temp['高温'] = li.find('p',{'class':'tem'}).text.strip()
                  elif li.find('h1').string.split(r'日')[1] =='夜间':
                        temp['低温'] = li.find('p',{'class':'tem'}).text.strip()
                  temp['风向'] = li.find('p',{'class':'win'}).find('span').attrs['title']
                  temp['风力'] = li.find('p',{'class':'win'}).text.strip()
                  temp[sun.text.split(' ')[0].strip()] = sun.text.split(' ')[1].strip()
                  today.append(temp)
            return today
      def getLifeTips(self):
            soup = bs(self.text,'html5lib')
            div_tag = soup.find('div',{'class':'livezs'})
            ul = div_tag.find('ul',{'class':'clearfix'})
            lis = ul.find_all('li')
            tips = []
            for li in lis:
                  if li.find('span').string != None:
                        temp = {}
                        temp[li.find('em').string.strip()] = li.find('span').string.strip() +' '+li.find('p').string.strip()
                        tips.append(temp)        
            return tips
if __name__ == '__main__':
      code = getCityMessage('model/city.json','haimen').getCode()
      #print(code)
      url = 'http://www.weather.com.cn/weather1d/{}.shtml'.format(code)
      #print(url)
      text = getUrlSource(url).getUrlText()
      print(bs4GetWeatherToday(text).getToday())
      print(bs4GetWeatherToday(text).getLifeTips())
