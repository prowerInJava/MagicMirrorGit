import random
import time
import socket
import http.client as httplib
import requests

from model.getCityMessage import getCityMessage

#浏览器请求头，用于让网站识别是浏览器请求，避免反盗链将爬虫封杀
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3226.400 QQBrowser/9.6.11681.400'
}

class getUrlSource():
      def __init__(self,url):
            self.url = url
      def getUrlText(self):
            self.timeout = random.choice(range(40,60))
            try:
                 respons = requests.get(self.url, headers=HEADERS,timeout=self.timeout)  # 获取网页信息
                 self.text = respons.content.decode('utf-8')  # 解析网页
                 #print (self.text)
                 return self.text
            except socket.timeout as e:
                  time.sleep(random.choice(range(8,15)))
            except socket.error as e:
                  time.sleep(random.choice(range(10,20)))
            except httplib.BadStatusLine as e:
                  time.sleep(random.choice(range(4,8)))
            except httplib.IncompleteRead as e:
                  time.sleep(random.choice(range(30,40)))

if __name__ == "__main__":
      cityCode = getCityMessage('city.json','haimen').getCode()
      print(cityCode)
      url = 'http://www.weather.com.cn/weather1d/101190508.shtml'
      t = getUrlSource(url).getUrlText()
      print(t)
