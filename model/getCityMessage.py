import json

class getCityMessage():
      def __init__(self,path,city):
            self.path = path
            self.city = city
            return None
      
      def loadFile(self):
            with open (self.path,'r',1,'gbk') as file:
                  data = json.load(file)
            return data

      def getCode(self):
            data = self.loadFile()
            for i in range(len(data)):
                  if self.city in (data[i].values()) :
                        self.cityCode = data[i]['cityCode']
                        break  #获取到需要的数据后跳出for循环
                  else: self.cityCode=None
            return self.cityCode
      def getCName(self):
            data = self.loadFile()
            for i in range(len(data)):
                  if self.city in (data[i].values()):
                        self.cityCName = data[i]['cityName']
                        break
                  else: self.cityCName = None
            return self.cityCName
      def getPinyin(self):
            data = self.loadFile()
            for i in range(len(data)):
                  if self.city in (data[i].values()):
                        self.cityPinyin = data[i]['cityPinyin']
                        break
                  else: self.cityPinyin = None
            return self.cityPinyin
      def getProvince(self):
            data = self.loadFile()
            for i in range(len(data)):
                  if self.city in (data[i].values()):
                        self.cityProvince = data[i]['province']
                        break
                  else: self.cityProvince = None
            return self.cityProvince

if __name__=='__main__':
      d = getCityMessage('city.json','浦东').getProvince()
      print(d)
