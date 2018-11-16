
#--*-- coding:  utf-8 --*--

import os, os.path

PICUTRE = ['jpg']
VIDEO = ['mpt']

class SortData():
    def __init__(self,datapath):
        self.datapath = datapath
    
    #在datapath目录下生成新的目录
    def generateDir(self):
        pass
    
    # 遍历datapath
    def walkdir(self):
        for file in os.listdir(path):
            filepath = os.path.join(path,file)
            if not os.path.isdir(filepath):
                print(filepath)
            else:
                walkdir(filepath)
                
    
            
           

            
if __name__ == '__main__':
    walkdir('D:\\Nobia')
        
            
    
    