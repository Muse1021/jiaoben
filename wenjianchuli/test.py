# -*- coding:utf-8 -*-
import os,sys,time
os.chdir("D:\\jiaoben\\trunk\\wenjianchuli\\testfile\\")
def readfile(filename):
	try:
		with open(filename,"r") as f:
			print f.read()
	except Exception as e:
		print e
#打开可读写文件，若文件存在则文件长度清为零，即该文件内容会消失。若文件不存在则建立该文件。
def writefile(filename,strs):
	with open(filename,"w+") as f:
		f.write(strs)
#追加
def editfile(filename,strs):
	with open(filename,"a+") as f:
		f.write(strs)
		#读取之前将指针重置为文件头
		f.seek(0)
		print f.read()
if __name__ == "__main__":
#	readfile("test.txt")
	str = "\n"+str(time.time())
#	writefile("test.txt",str) 
	editfile("test.txt",str)