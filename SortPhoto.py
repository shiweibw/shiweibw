
#--*-- coding:  utf-8 --*--

import os, os.path, shutil

PICUTRE = ['.jpg']
VIDEO = ['.mp4']

class SortData():
    def __init__(self,dst_dir):
        self.dst_dir = dst_dir
    
    #在datapath目录下生成新的目录
    def movePicture(self,year,month,type,file):
        #在datapath目录下创建年度目录
        year_dir = os.path.join(self.dst_dir,year)
        month_dir = os.path.join(year_dir,month)
        video_dir = os.path.join(month_dir,'VIDEO')
        picture_dir = os.path.join(month_dir,'PICTURE')
        
        '''for dir in [year_dir, month_dir, video_dir, picture_dir]:
            if not os.path.isdir(dir):
                os.mkdir(dir)
        '''        
        if type in PICUTRE:
            # move pciture to right dir
            if not os.path.isdir(picture_dir):
                os.makedirs(picture_dir)
            shutil.move(file, picture_dir)
        elif type in VIDEO:
            if not os.path.isdir(video_dir):
                os.makedirs(video_dir)
            shutil.move(file, video_dir)
        else:
            print("Doesn't move %s" % file)
            
            

        
        
        
    #分析照片，得出照片的年份 月份和类型。
    def AnalyPhoto(self,picture):
        file = os.path.basename(picture)
        filename,type = os.path.splitext(file)
        pic = filename.split('_')[1]
        assert len(pic[:4]) == 4, "the length of the YEAR must be 4 "
        assert int(pic[4:6]) < 13, "MONTH must be 0 ~ 12 "
        
        return pic[:4],pic[4:6],type
    
    # 遍历datapath
    def walkdir(self,datapath):
        for file in os.listdir(datapath):
            filepath = os.path.join(datapath,file)
            if os.path.isfile(filepath):
                year,month,type = self.AnalyPhoto(filepath)
                self.movePicture(year,month,type,filepath)
                
            else:
                self.walkdir(filepath)
                
    
            
           

            
if __name__ == '__main__':
    a = SortData('D:\\Nobia')
    a.walkdir('D:\\Nobia')
    #a.generateDir('2018','02')
    #y,m,t = a.AnalyPhoto('IMG_20170613_134101.jpg')
    #print(y,m,t)
    
        
            
    
    