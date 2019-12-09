#! /usr/bin/env python3
import threading
import platform
from time import sleep

import magicMirrorLinux
import weaInfo2file as wea2file

sysstr = platform.system()
def t1():
      if sysstr =='Windows':
            import sinaNews as wsina
      else:
            import sinaLinuxNews as wsina
      wsina.SinaNews()
      return None
def t2():
      wea2file.weaInfo2files()
      return None
def t3():
      magicMirrorLinux.magicMirror()
      return None
      
threads = []
t1 = threading.Thread(target=t1)
threads.append(t1)
t2 = threading.Thread(target=t2)
threads.append(t2)
t3 = threading.Thread(target=t3)
threads.append(t3)

if __name__=='__main__':
      for t in threads:
            t.start()
      for t in threads:
            t.join()
print("退出") 
