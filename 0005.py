'''
**第 0005 题：**你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

iPhone5 的分辨率：1136 * 640 像素
把一张纵向（即 宽 < 高）的图的宽度调整到 640 像素是最具性价比的，但是对于一张横向（即 宽 > 高）
的图片这样调整的话就太“失真”了，比如 16：9 的图片就只有 640 * 360 分辨率了。所以，对于横向的
图片直接把它的高按 640 调整，到手机上可以旋转浏览。
'''
import os,os.path
from PIL import Image
inputdir="D:\\Python\\Python_Xue_Xi_Bi_Ji_20160709\\photo_for_5"
outputdir="D:\\Python\\Python_Xue_Xi_Bi_Ji_20160709\\new_photo_for_5"

images = [ inputdir+"\\"+image for image in os.listdir(inputdir)]

resize_image = lambda image : (image if image.width < 640   #宽度小于640的,不处理
                              else image.resize((640,int(image.height*640/image.width)))
                              if image.width < image.height #纵向
                              else image.resize((int(image.width*640/image.height),640)) #横向
)

if not os.path.exists(outputdir):
	os.mkdir(outputdir)

for input_img in images :
	img_name = os.path.basename(input_img)
	image = Image.open(input_img)
	resize_image(image).save(outputdir+"\\"+img_name,"JPEG")
	#image.save(outputdir+"\\"+img_name,"JPEG")
	new_image = Image.open(outputdir+"\\"+img_name)
	print(new_image.size)



