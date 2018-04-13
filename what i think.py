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

game_times=0    ##总游戏次数
min_times=999    ##最快猜出的轮数
total_times=0   ##总共猜过的轮数

print('请输入你的名字:')
username=input()
f=open('game.txt','r')


