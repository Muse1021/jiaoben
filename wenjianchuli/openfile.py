__author__ = 'Muse'
import os,sys
class thefile(object):
    def __init__(self,file):
        self.file = file
    def openthefile(self,style)    :
        list = os.listdir(self.file)
        for i in range(len(list)):
            if style in list[i]:
                f = open(self.file+list[i],'r')
                print f.read()
                f.close()
    def writeline(self,strs,writefile):
        with open(writefile,'a') as f1:
			f1.writelines(strs)
			with open(writefile,'r') as f1:
				print f1.read()
			
    def writeline1(self,strs,writefile):
        f1 = open(writefile,'a')
        f1.writelines(strs)
        f1 = open(writefile,'r')
        print f1.read()
        f1.close()		
    def creatandwrite(self,file1,file2):
        fl1 = open(file1,'r')
        str1 = fl1.readline()
        fl2 = open(file2,'a')
        fl2.writelines(str1)
        fl2 = open(file2,'r')
        print fl2.read()


newfile = thefile("D:\\jiaoben\\trunk\\wenjianchuli\\testfile\\")
newfile.creatandwrite("D:\\jiaoben\\trunk\\wenjianchuli\\testfile\\testfile.txt","D:\\jiaoben\\trunk\\wenjianchuli\\testfile\\testfile1.doc")
# newfile.writeline("lixiao","E:\\workspace\\testfile\\testfile.txt")
# openthefile("txt","E:\\workspace\\testfile\\")