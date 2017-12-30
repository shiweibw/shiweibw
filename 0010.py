'''
第 0010 题：使用 Python 生成类似于下图中的字母验证码图片
'''
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

#生成随机字母
def ranChar():
	return chr(random.randint(65,90))

#生成随机颜色1
def ranColor1():
	return(random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

#生成随机颜色2
def ranColor2():
	return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

#生成字母验证码图片
def Create_aut_code():
	#生成一个240x60大小的空白图片	
	width = 60*4
	height = 60
	image = Image.new('RGB',(width,height),(255,255,255))

	#创建Draw对象
	draw_image = ImageDraw.Draw(image)

	#为每个像素填充颜色
	for x in range(width):
		for y in range(height):
			draw_image.point((x,y),fill=ranColor1())

	#定义字体格式
	my_font = ImageFont.truetype("ARIALUNI.TTF", 36)

	#生成随机字母
	for i in range(4):
		draw_image.text((60*i+10,10),ranChar(),font=my_font,fill=ranColor2())
	
	#模糊
	image = image.filter(ImageFilter.BLUR)
	image.save('code.jpg', 'jpeg')
	return image

if __name__ == '__main__':
	Create_aut_code()

