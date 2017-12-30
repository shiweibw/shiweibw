'''
第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
'''
from PIL import Image, ImageDraw, ImageFont
import os.path
def test0000(input_img,**kw):
	if os.path.isabs(input_img):
		filename = os.path.basename(input_img)
	else:
		filename = input_img
	
	#默认在图像的右上角加上数字4
	text = kw.setdefault('text','4')

	#定义默认修改后的图像的保存位置
	output_image = kw.setdefault('output_image','new_'+filename)
    
    #打开一个jpg图像文件,即新建 Image 类的实例
	im = Image.open(input_img)
	width, height = im.size

	#实例化Draw类，在im文件上涂涂改改
	draw_im = ImageDraw.Draw(im)

	#定义字体格式
	my_font = ImageFont.truetype("C:\\Windows\\Fonts\\ARIALUNI.TTF", 60)

	#在im文件上添加数字4
	draw_im.text((width-30,0),text,font=my_font,fill='red')

	#保存文件
	im.save(output_image,"JPEG")

if __name__ == '__main__':
	test0000('D:\\Python\\Python_Xue_Xi_Bi_Ji_20160709\\CV0020938.jpg')