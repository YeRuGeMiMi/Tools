#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-07-17 08:42:59
# @Author  : yfl (yerugemimi@gmail.com)
# @Link    : https://github.com/YeRuGeMiMi
# @Version : $Id$

import MySQLdb as db
import sys
import re
import pdb

reload(sys)
sys.setdefaultencoding('utf8')

#获取数据库连接
#parame: dbconf={}(host->数据库服务器host，user->用户，passwd->密码,db->数据库名,charset->字符集,port->端口)
#return: con 数据库连接对象
def getCon(dbconf):
	con = db.connect(host=dbconf['host'],user=dbconf['user'],passwd=dbconf['passwd'],db=dbconf['db'],charset=dbconf['charset'],port=dbconf['port'])
	return con

#获取一张表的DDL信息
#parame: table 数据库表名，con 数据库连接对象
#return: row 返回数据行元组（表名，DDL信息）
def exportTableInfo(table,con):
	cursor = con.cursor()

	sql ="SHOW CREATE TABLE "+table 
	cursor.execute(sql)
	row = cursor.fetchone()
	return row

	cursor.close()
	con.close()

#导出数据表的DDL信息到文件
#parame: tables 数据库表列表，export_file 导出文件路劲,con 数据对象
def exportDDL(tables,export_file,con):
	for vo in tables:
		row = exportTableInfo(vo,con)
		f = open(export_file,'a')
		f.write(row[1]+'\n\n')
	f.close()

#判断是否为key
def reKey(key):
	pattern = re.compile(r'^`\w*`$')
	match = pattern.match(key)

	return match

#判断是否为value
def reValue(value):
	pattern = re.compile(r'COMMENT')
	match = pattern.match(value)

	return match

#解析文件，取字段名和注释
def readFile(filepath):
	f = open(filepath)
	i=0
	result = []
	for line in f :
		if i == 0:
			i = i+1
			continue
		sl = line.split(' ')
		key = ''
		value =  ''
		j = 0 
		for v in sl:
			isKey = reKey(v)
			if(isKey):
				key = v
				j = j+1
				continue

			isValue = reValue(v)
			if(isValue):
				value = sl[j+1]
			j = j+1
		if(key != '' and value != ''):
			result.append({key:value})

		i = i+1

	f.close()

	return result


if __name__ == '__main__':
	# tables = ['member','member_info']
	# dbconf = {'host':'localhost','user':'root','passwd':'yflllb','db':'student_dev','charset':'utf8','port':3307}
	# con = getCon(dbconf)
	# exportDDL(tables,'info.txt',con)
	
	print readFile('info.txt')