# -*- coding: utf-8 -*-
import os
def file_traversal(path):
	sumsize = 0
	try:
		filename = os.walk(path)
		for root, dirs, files in filename:
			for fle in files:
				print fle,"-----",root,"------",dirs
				size = os.path.join(path + fle)
				print size
	except Exception as err:
		print(err)
if __name__ =='__main__':
#	file_traversal('D:\\jiaoben\\trunk\\wenjianchuli')
