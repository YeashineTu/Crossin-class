#!/usr/bin/python
#-*- coding utf-8 -*-
#date:20171009 17:34
#author:tyx
def isEqual(value1,value2):
	if(value1<value2):
		print('%d is too small'%value)
		return False
	elif (value1>value2):
		print('%d is too large'%value)
		return False
	else:
		print('BINGO,%d is the right answer!'%value)
		return True
import  random
game_times=0    ##总游戏次数
min_times=999    ##最快猜出的轮数
total_times=0   ##总共猜过的轮数

print('请输入你的名字:')
f=open('game.txt','w')



username=input()
for i in range(1):
	game_times+=1
	min_times_this=0
	print('Guess what I think?')
	randvalue=random.randint(1,10)
	isRight=False   ##大写
	while(isRight==False):        ##False 和True都是大写的哦
		value=int(input())
		isRight=isEqual(value,randvalue)          ##本来想在函数里面的isright是局部的，不能用到循环里，参考了一下，返回值作为isright
		min_times_this+=1
	total_times=total_times+min_times_this
	min_times=min(min_times,min_times_this)

#avg_times=float(total_times)/game_times
result='%s %d %d %d'%(username,game_times,min_times,total_times)


#print('%s,你好！你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案' % (username,game_times,min_times,avg_times))

### 总游戏次数，最快猜出的轮数，和猜过的总轮数