
#--*-- coding:  utf-8 --*--

import os, os.path

PICUTRE = ['jpg']
VIDEO = ['mpt']

class SortData():
    def __init__(self,datapath):
        self.datapath = datapath
    
    #��datapathĿ¼�������µ�Ŀ¼
    def generateDir(self):
        pass
    
    # ����datapath
    def walkdir(self):
        for file in os.listdir(path):
            filepath = os.path.join(path,file)
            if not os.path.isdir(filepath):
                print(filepath)
            else:
                walkdir(filepath)
                
    
            
           

            
if __name__ == '__main__':
    walkdir('D:\\Nobia')
        
            
    
    