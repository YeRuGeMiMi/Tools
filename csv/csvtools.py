#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Date    : 2014-04-17
# @Author  : yfl <yerugemimi@gmail.com>
# @Link    : https://github.com/YeRuGeMiMi
# @Version : 1.0

#CSV文件的操作工具类
#环境：python 2.7.5

import os.path


#csv_get_lines 读取CSV文件中指定行的数据,使用的是第一行是title的格式
#param: csvfile csv文件路径
#param：lines 读取指定行数
#param: offset 开始行数
#param: sign 分隔符
#return: []
def csv_get_lines(csvfile,lines,offset=0,sign=','):
	#判断文件是否存在
	if not os.path.exists(csvfile) :
		return False
	f=open(csvfile,'r')
	i=0
	j=0
	datas=[]
	for line in f :
		#读取title
		if i == 0:
			line=line.strip('\n')
			titles=line.split(sign)

		#跳到指定的开始行
		i=i+1
		if i<offset :
			continue
		
		#以[{title:data,title:data,title:data}]的格式输出数据
		if j<lines :
			j=j+1
			line=line.strip('\n')
			data=line.split(sign)
			#判断文件的格式是否正确
			if not len(titles) == len(data) :
				return False
			
			datas.append(dict(zip(titles,data)))

	return datas

