from PIL import Image
#import argparse

#string_char = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft^|()1{}[]?-_+~<>i!Ll;:,/EFG '
#string_char = ' ,.,iIJCDOSQGFE#&@ '   头像图片，照片
string_char = ' ,.,iIJCDOSQGFE#&@ '
# 把RGB转为灰度值，并且返回该灰度值对应的字符标记
def rgb_to_char(r, g, b):
	length = len(string_char)
	gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
	##灰度区间
	unit = (256 + 1) / length
	##灰度对应的字符索引
	idx = int(gray / unit)
	return string_char[idx]

#预处理（将图片尺寸压缩，并转为灰度图）
def reprocess(imagepath,delta=100):
	img = Image.open(imagepath)
	##获取图片尺寸  size没有括号
	(width,height) = img.size
	print(img.size)
	##获取最大长度
	if width > height:
		max = height
	else:
		max = width
	##伸缩倍数
	scale = max / delta
	width, height = int(width / scale), int(height / scale)
	#改变图片像素width*height  因为发现高度太高，有拉长效果，所以高度减半了
	img = img.resize((width,int(height/2)))
	return img

##图片转字符
def img_to_char(img_obj,savepath):
	txt = ''
	width, height = img_obj.size
	##获取像素点元组，并转化成字符
	for i in range(height):
		line = ''
		for j in range(width):
			line += rgb_to_char(*img_obj.getpixel((j, i))[:3])
		txt = txt + line + '\n'
	##保存
	with open(savepath,'w+',encoding='utf-8') as f:
		f.write(txt)


img_obj = reprocess('tree1.jpg',90)
img_to_char(img_obj, 'tree2.txt')

# f = open('tree2.txt')
# for i in f.readlines():
# 	print(i)
# f.close()