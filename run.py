import threading
import platform
from time import sleep



import magicMirror
import weaInfo2file.weaInfo2files as wea2file
import sinaNews as wsina
class mainRun:
      def __init__(self):
            self.t1 = wsina.SinaNews()
            self.t2 = wea2file.weaInfo2files()
            self.t3 = magicMirror.magicMirror()
      
      
def main ():
      
      while True:
            mm = threading.Thread(target=magicMirror.magicMirror())
            if platform.system().upper() == 'WINDOWS':
                  
                  print ('GO。。。。。')
                  sina = threading.Thread(target=wsina.SinaNews())
                  wea = threading.Thread(target=wea2file.weaInfo2files())
                  
            else:
                  import sinaLinuxNews as lsina
                  sina = threading.Thread(target=wsina.SinaNews())
                  wea = threading.Thread(target=wea2file.weaInfo2files())
            sina.start()
            wea.start()
            mm.start()
      
