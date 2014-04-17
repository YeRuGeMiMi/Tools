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
	
	if not os.path.exists(csvfile) :
		return False
	f=open(csvfile,'r')
	i=0
	j=0
	datas=[]
	for line in f :
		if i == 0:
			line=line.strip('\n')
			titles=line.split(sign)

		i=i+1
		if i<offset :
			continue
	
		if j<lines :
			j=j+1
			line=line.strip('\n')
			data=line.split(sign)
			if not len(titles) == len(data) :
				return False
			
			datas.append(dict(zip(titles,data)))

	return datas

