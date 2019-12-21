import tkinter as tk
from tkinter import ttk
import os
import time
import datetime
import sys
import platform
import pickle
import random
#import bs4GetWeatherToday as todayWea
#import bs4GetWeather7d as d7dayWea

class magicMirror:
      def __init__(self):
            self.title = "MagicMirror"
            self.weatherPng = 'png/rain.png'
            #self.get_WeatherInfo()
            while True:
                  self.Mirror()
                  #print('Main window')
                  time.sleep(500)
            return None
      #对dayLabel hourLabel miLabel实时显示时间
      def tick(self):
            self.t1 = ''
            localtime = time.strftime('%Y-%m-%d-%H-%M-%S')
            if localtime != self.t1:
                  timelist = localtime.split('-')
                  year = timelist[0]
                  mm = timelist[1]
                  day = timelist[2]
                  hour = timelist[3]
                  mi = timelist[4]
                  ss = timelist[5]
                  daystr = ('%s年%s月%s日'%(year,mm,day))
                  self.dayLabel.config(text = daystr)
                  self.hourLabel.config(text = hour)
                  #self.hourLabel.config(text='00')
                  self.miLabel.config(text = mi)
                  self.miLabel.after(1000,self.tick)
            return None
      #cityLabel 实时显示城市名称
      def get_city(self):
            self.c1 = ''
            #print(self.get_config())
            self.city = self.get_config()['city']
            if self.c1 != self.city:
                  self.cityLabel.config(text=self.city)
                  self.cityLabel.after(1000,self.get_city)
      #手动配置需要显示的城市，config/mycity.txt文件
      def get_config(self):
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
      #获取新浪写入的新闻资料，data/news.txt
      def get_sinaNews(self):
            first = ''
            with open('data/news.txt','r') as file:
                  texts = file.readline()
            if texts != first:
                  a = texts.split('***')
                  self.newsLabelTime.config(text = a[0])
                  self.newsLabel.config(text = a[1])
                  #print(a)
            self.newsLabel.after(1000,self.get_sinaNews)
      def get_WeatherInfo(self):
            w = ''
            mappd = {}
            list7d = []
            maptips = {}
            with open('data/todayWea','r',1,'gbk') as file:
                  data = file.readlines()
                  for i in data:
                        k = i.split("@")[0].strip()
                        v = i.split("@")[1].strip()
                        mappd[k] = v
            with open('data/tips','r',1,'gbk') as file:
                  data = file.readlines()
                  for i in data:
                        k = i.split(":")[0].strip()
                        v = i.split(":")[1].strip()
                        maptips[k] = v
                  #print (maptips)
            with open('data/7daysWea','r',1,'gbk') as file:
                  data = file.readlines()
                  #list1d = []
                  for i in data:
                        list7d.append(i.split(','))
                  
                  #print (list7d)
            daytime = mappd['白天']
            night = mappd['夜间']
            weekdate = time.strftime('%A') #获取今天是星期几
            #print(mappd)
            sunrise = mappd['日出'].strip()
            sundown = mappd['日落'].strip()
            if weekdate =='Monday':
                  mappd['日期'] = '星期一'
            elif weekdate =='Tuesday':
                  mappd['日期'] = '星期二'
            elif weekdate =='Wednesday':
                  mappd['日期'] = '星期三'
            elif weekdate =='Thursday':
                  mappd['日期'] = '星期四'
            elif weekdate =='Friday':
                  mappd['日期'] = '星期五'
            elif weekdate =='Saturday':
                  mappd['日期'] = '星期六'
            elif weekdate =='Sunday':
                  mappd['日期'] = '星期日'
            day = mappd['日期']
            #print(mappd)
            #high = list7d[0][2].split(':')[1]
            high = mappd['高温'].split('°')[0]
            #print(high)
            low = mappd['低温'].split('°')[0]
            #print(low)
            """
            mappd['最高温'] = high
            low = list7d[0][3].split(':')[1]
            mappd['最低温'] = low
            """
            wind = list7d[0][5].split(':')[1].strip()
            mappd['风向'] = wind
            windforce = list7d[0][4].split(':')[1].strip()
            mappd['风力'] = windforce
            aqi = maptips['空气污染扩散指数'].split(' ')[0]
            tip = maptips['空气污染扩散指数'].split(' ')[1]
            #print(tip)
            localtime = time.strftime('%H:%M')
            if day !=w:
                  self.todayLabel.config(text=day)
                  if high != 'None':
                        self.tump.config(text=high+'~'+low+'℃')
                  else:
                        self.tump.config(text=low+'℃')
                  self.wind.config(text=wind)
                  self.windforce.config(text=windforce)
                  self.sunriseL.config(text='日出 '+sunrise)
                  self.sundownL.config(text='日落 '+sundown)
                  self.outAirQ.config(text='室外空气质量指数:'+str(aqi))
                  self.outAirQtip.config(text=tip)
            if localtime>sunrise and localtime<sundown:
                  self.tWeather.config(text='白天:'+daytime)
                  if '雷阵雨' in daytime :
                        self.weatherPng='weather_tempest.png'
                  elif '阵雨' in daytime and '雷' not in daytime:
                        self.weatherPng='rain.png'
                  elif '中雨' in daytime or '大雨' in daytime:
                        self.weatherPng = 'rain.png'
                  elif '多云' in daytime:
                        self.weatherPng='Partly_Cloudy_Day_48px.png'
                  elif '小雨' in daytime:
                        self.weatherPng='weather_xiaoyu_48px.png'
                  elif '雪' in daytime:
                        self.weatherPng='weather_snow_48px.png'
                  elif '晴' in daytime:
                        self.weatherPng='sun.png'
                  elif '雾' in daytime:
                        self.weatherPng ='weather_fog_48px.png'
                  else :self.weatherPng='weather_cloud_32px.png'
                  self.weater = tk.PhotoImage(file='png/'+self.weatherPng)                        
            else:
                  self.tWeather.config(text='晚上:'+night)
                  if '雷阵雨' in night:
                        self.weatherPng='weather_tempest.png'
                  elif '阵雨' in night and '雷' not in night:
                        self.weatherPng='rain.png'
                  elif '中雨' in night or '大雨' in night:
                        self.weatherPng='rain.png'
                  elif '多云' in night:
                        self.weatherPng='Partly_Cloudy_Day_48px.png'
                  elif '小雨' in night:
                        self.weatherPng='weather_xiaoyu_48px.png'
                  elif '雪' in night:
                        self.weatherPng='weather_snow_48px.png'
                  elif '晴' in night:
                        self.weatherPng='sun.png'
                  elif '雾' in night:
                        self.weatherPng ='weather_fog_48px.png'
                  else :self.weatherPng='weather_cloud_32px.png'
                  self.weater = tk.PhotoImage(file='png/'+self.weatherPng)
                        
            self.pnglabel.config(image=self.weater)
            #TODO
            i = random.randint(0,len(list(maptips))-1)
            k = list(maptips)[i]
            v = maptips[k]
            
            self.tipsLabel.config(text=k+':'+v)
            self.todayLabel.after(18000,self.get_WeatherInfo)
      def get_featureWea(self):
            dayMap = {}
            dayMap['monday'] = '星期一'
            dayMap['tuesday'] = '星期二'
            dayMap['wednesday'] = '星期三'
            dayMap['thursday'] = '星期四'
            dayMap['friday'] = '星期五'
            dayMap['saturday'] = '星期六'
            dayMap['sunday'] = '星期日'
            list7d = []
            with open('data/7daysWea','r',1,'gbk') as file:
                  data = file.readlines()
                  #list1d = []
                  for i in data:
                        list7d.append(i.split(','))
            #index 1,2,3,4
            #第二天
            day = dayMap[list7d[1][0].split(":")[1].split(" ")[0].lower()]
            high = list7d[1][2].split(":")[1].strip().lower()
            low = list7d[1][3].split(":")[1].strip().lower()
            tump = list7d[1][1].split(":")[1].strip().lower()
            wind = list7d[1][5].split(":")[1].strip().lower()
            windforce = list7d[1][4].split(":")[1].strip().lower()
            #print(day,high,low,tump,wind,windforce)
            if day !='':
                  self.ffLabel.config(text=day)
                  self.fftLabel.config(text=high+'~'+low+'℃')
                  #self.ffaLabel.config(text=tip)
                  self.ffweLabel.config(text=tump)
                  self.ffwnLabel.config(text=wind)
                  self.ffwnFLabel.config(text=windforce)
            #第三天    
            day = dayMap[list7d[2][0].split(":")[1].split(" ")[0].lower()]
            #print (day)
            high = list7d[2][2].split(":")[1].strip().lower()
            low = list7d[2][3].split(":")[1].strip().lower()
            tump= list7d[2][1].split(":")[1].strip().lower()
            wind = list7d[2][5].split(":")[1].strip().lower()
            windforce = list7d[2][4].split(":")[1].strip().lower()
            #print (list7d[1],list7d[2],list7d[3],list7d[4])
            if day !='':
                  self.thLabel.config(text=day)
                  self.thtLabel.config(text=high+'~'+low+'℃')
                  #self.thaLabel.config(text=tip)
                  self.thweLabel.config(text=tump)
                  self.thwnLabel.config(text=wind)
                  self.thwnFLabel.config(text=windforce)
            #第四天    
            day = dayMap[list7d[3][0].split(":")[1].split(" ")[0].lower()]
            #print (day)
            high = list7d[3][2].split(":")[1].strip().lower()
            low = list7d[3][3].split(":")[1].strip().lower()
            tump = list7d[3][1].split(":")[1].strip().lower()
            wind = list7d[3][5].split(":")[1].strip().lower()
            windforce = list7d[3][4].split(":")[1].strip().lower()
            #print (list7d[1],list7d[2],list7d[3],list7d[4])
            if day !='':
                  self.ftLabel.config(text=day)
                  self.fttLabel.config(text=high+'~'+low+'℃')
                  #self.ftaLabel.config(text=tip)
                  self.ftweLabel.config(text=tump)
                  self.ftwnLabel.config(text=wind)
                  self.ftwnFLabel.config(text=windforce)
            #第五天    
            day = dayMap[list7d[4][0].split(":")[1].split(" ")[0].lower()]
            #print (day)
            high = list7d[4][2].split(":")[1].strip().lower()
            low = list7d[4][3].split(":")[1].strip().lower()
            tump = list7d[4][1].split(":")[1].strip().lower()
            wind = list7d[4][5].split(":")[1].strip().lower()
            windforce = list7d[4][4].split(":")[1].strip().lower()
            #print (list7d[1],list7d[2],list7d[3],list7d[4])
            if day !='':
                  self.fiLabel.config(text=day)
                  self.fitLabel.config(text=high+'~'+low+'℃')
                  #self.fiaLabel.config(text=tip)
                  self.fiweLabel.config(text=tump)
                  self.fiwnLabel.config(text=wind)
                  self.fiwnFLabel.config(text=windforce)
            self.fiwnFLabel.after(5000,self.get_featureWea)
            return None
      #主体
      def Mirror(self):
            self.mirror = tk.Tk()
            self.mirror.title(self.title)
            self.mirror.overrideredirect(True)
            w = self.mirror.winfo_screenwidth()
            h = self.mirror.winfo_screenheight()
            self.mirror.geometry("%dx%d"%(w,h))

            #定一个全局的黑色背景的Frame
            self.mainFrame = tk.Frame(width=w,height=h,bg = 'black').place(x=0,y=0)
            
            #显示日期
            self.dayLabel = tk.Label(self.mainFrame,text = ('%d年%d月%d日'%(2011,12,23)),
                                     font=('Times New Roman',42,'bold'),fg='darkgray',bg='black')
            self.dayLabel['height'] = 1
            self.dayLabel['width'] = 20
            self.dayLabel.place(x=28,y=28)

            #显示时间使用LCD字体DS-Digital
            self.hourLabel = tk.Label(self.mainFrame,font=('DS-Digital',110),fg='white',bg='black')
            self.sLabel = tk.Label(self.mainFrame,text=':',font=('DS-Digital',110),fg='white',bg='black')
            self.miLabel = tk.Label(self.mainFrame,font=('DS-Digital',110),fg='white',bg='black')
            self.hourLabel['height'] = 1
            self.hourLabel['width'] = 3
            self.sLabel['height'] = 1
            self.miLabel['height'] = 1
            self.miLabel['width'] = 3
            self.hourLabel.place(x=50,y=119)
            self.sLabel.place(x=275,y=110)
            self.miLabel.place(x=295,y=119)
            
            self.tick()

            #TODO 从天气信息中获取第一天的星期几信息
            #显示星期几 
            self.todayLabel = tk.Label(self.mainFrame,text = '星期五',background='black',
                                       foreground='darkgray',font=('宋体',42,'bold'))
            self.todayLabel['height'] = 1
            self.todayLabel.place(x=840,y=28)

            #显示当前配置的城市
            self.cityLabel = tk.Label(self.mainFrame,text='海门',font=('宋体',42,'bold'),fg='darkgray',bg = 'black')
            self.cityLabel['height'] = 1
            self.cityLabel.place(x=630,y=28)
            
            self.get_city()

            #TODO 获取当日天气与未来天气信息
            self.weather = tk.PhotoImage(file='png/weather_tempest.png')
            self.pnglabel = tk.Label(self.mainFrame,image=self.weather,borderwidth=0)
            self.tWeather = tk.Label(self.mainFrame,text='白天:雷雨',font=('宋体',20,'bold'),fg='white',bg='black')
            self.tump = tk.Label(self.mainFrame,text = '27℃~34℃',font=('宋体',20,'bold'),fg='white',bg='black')
            self.wind = tk.Label(self.mainFrame,text='东南风',font = ('宋体',20,'bold'),fg='white',bg = 'black')
            self.windforce = tk.Label(self.mainFrame,text='4 级',font = ('宋体',20,'bold'),fg='white',bg = 'black')
            self.sunriseL = tk.Label(self.mainFrame,text='日出:06:59',font = ('宋体',20,'bold'),fg='white',bg = 'black')
            self.sundownL = tk.Label(self.mainFrame,text='日落:18:59',font = ('宋体',20,'bold'),fg='white',bg = 'black')
            self.outAirQ = tk.Label(self.mainFrame,text='室外空气质量:优',font = ('宋体',20,'bold'),fg='white',bg = 'black')
            self.outAirQtip = tk.Label(self.mainFrame,text='适合户外活动',font = ('宋体',20,'bold'),fg='white',bg = 'black')
            self.pnglabel.place(x=640,y=126)
            self.tWeather.place(x=702,y=126)#742
            self.tump.place(x=896,y=126)
            self.wind.place(x=702,y=161)
            self.windforce.place(x=896,y=161)
            self.sunriseL.place(x=630,y=196)
            self.sundownL.place(x=889,y=196)
            self.outAirQ.place(x=630,y=231)
            self.outAirQtip.place(x=630,y=266)
            #每日贴士
            self.tipsLabel = tk.Label(self.mainFrame,text='避免长时间在日光下暴晒或在高温环境中工作。',
                                      font = ('楷体',22,'bold'),fg = 'white',bg = 'black',width = 84,height =4,
                                      wraplength = 980,anchor = 'nw',justify = 'left')
            self.tipsLabel.place(x=48,y=1344)
            
            self.get_WeatherInfo()

            #未来四天的天气预报
            self.ffLabel = tk.Label(text='星期三',font = ('楷体',20,'bold'),fg='gray',bg = 'black')
            self.fftLabel = tk.Label(text='36~28℃',font = ('楷体',20,'bold'),fg='gray',bg = 'black')
            #self.ffaLabel = tk.Label(text='差严重污染',font = ('楷体',14,'bold'),fg='gray',bg = 'black')
            self.ffweLabel = tk.Label(text='多云',font = ('楷体',20,'bold'),fg='gray',bg = 'black')
            self.ffwnLabel = tk.Label(text='东南风',font = ('楷体',20,'bold'),fg='gray',bg = 'black')
            self.ffwnFLabel = tk.Label(text='3-4级',font = ('楷体',20,'bold'),fg='gray',bg = 'black')
            self.ffLabel.place(x=490,y=329)
            self.fftLabel.place(x=595,y=329)
            #self.ffaLabel.place(x=445,y=235)
            self.ffweLabel.place(x=721,y=329)
            self.ffwnLabel.place(x=861,y=329)
            self.ffwnFLabel.place(x=987,y=329)
            
            self.thLabel = tk.Label(text='星期三',font = ('楷体',20,'bold'),fg='gray',bg = 'black')
            self.thtLabel = tk.Label(text='36~28℃',font = ('楷体',20,'bold'),fg='gray',bg = 'black')
            #self.thaLabel = tk.Label(text='差严重污染',font = ('楷体',14,'bold'),fg='gray',bg = 'black')
            self.thweLabel = tk.Label(text='多云',font = ('楷体',20,'bold'),fg='gray',bg = 'black')
            self.thwnLabel = tk.Label(text='东南风',font = ('楷体',20,'bold'),fg='gray',bg = 'black')
            self.thwnFLabel = tk.Label(text='3-4级',font = ('楷体',20,'bold'),fg='gray',bg = 'black')
            self.thLabel.place(x=490,y=364)
            self.thtLabel.place(x=595,y=364)
            #self.thaLabel.place(x=445,y=260)
            self.thweLabel.place(x=721,y=364)
            self.thwnLabel.place(x=861,y=364)
            self.thwnFLabel.place(x=987,y=364)

            self.ftLabel = tk.Label(text='星期三',font = ('楷体',20,'bold'),fg='gray',bg = 'black')
            self.fttLabel = tk.Label(text='36~28℃',font = ('楷体',20,'bold'),fg='gray',bg = 'black')
            #self.ftaLabel = tk.Label(text='差严重污染',font = ('楷体',14,'bold'),fg='gray',bg = 'black')
            self.ftweLabel = tk.Label(text='多云',font = ('楷体',20,'bold'),fg='gray',bg = 'black')
            self.ftwnLabel = tk.Label(text='东南风',font = ('楷体',20,'bold'),fg='gray',bg = 'black')
            self.ftwnFLabel = tk.Label(text='3-4级',font = ('楷体',20,'bold'),fg='gray',bg = 'black')
            self.ftLabel.place(x=490,y=399)
            self.fttLabel.place(x=595,y=399)
            #self.ftaLabel.place(x=445,y=285)
            self.ftweLabel.place(x=721,y=399)
            self.ftwnLabel.place(x=861,y=399)
            self.ftwnFLabel.place(x=987,y=399)

            self.fiLabel = tk.Label(text='星期三',font = ('楷体',20,'bold'),fg='gray',bg = 'black')
            self.fitLabel = tk.Label(text='36~28℃',font = ('楷体',20,'bold'),fg='gray',bg = 'black')
            #self.fiaLabel = tk.Label(text='差严重污染',font = ('楷体',14,'bold'),fg='gray',bg = 'black')
            self.fiweLabel = tk.Label(text='多云',font = ('楷体',20,'bold'),fg='gray',bg = 'black')
            self.fiwnLabel = tk.Label(text='东南风',font = ('楷体',20,'bold'),fg='gray',bg = 'black')
            self.fiwnFLabel = tk.Label(text='3-4级',font = ('楷体',20,'bold'),fg='gray',bg = 'black')
            self.fiLabel.place(x=490,y=434)
            self.fitLabel.place(x=595,y=434)
            #self.fiaLabel.place(x=445,y=310)
            self.fiweLabel.place(x=721,y=434)
            self.fiwnLabel.place(x=861,y=434)
            self.fiwnFLabel.place(x=987,y=434)
            self.get_featureWea()

            #新浪实时新闻显示
            self.newsLabelTime = tk.Label(self.mainFrame,text='新浪消息:10:27:37',font = ('宋体',25,'bold'),fg = 'white',bg='black')
            self.newsLabelTime.place(x=48,y=1533)
            self.newsLabel = tk.Label(self.mainFrame,text='【最高检：检察机关依法对鲁炜、莫建成、张杰辉三案提起公诉】',
                                      font = ('宋体',20,'bold'),fg = 'white',bg='black',width = 88,height=13,
                                      wraplength = 966,anchor = 'nw',justify = 'left',pady=4)
            self.newsLabel.place(x=48,y=1582)
            self.get_sinaNews()
            def func(event):
                  if event.char in ['q','Q']:
                        print('event')
                        self.mirror.destroy()
            def fune(event):
                  self.mirror.destroy()
            self.dayLabel.bind('<Button-1>',fune)
            self.mirror.bind("<Key>",func)#窗体绑定事件，按下q/Q键窗体会被destroy掉
            self.mirror.mainloop()
#magicMirror()

if __name__=='__main__':
      magicMirror()


            
            
            
      
            
