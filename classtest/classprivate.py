__author__ = 'Muse'
class canopen(object):
    def __init__(self,file_name,mode='r',bef=-1):
        self.file = open(file_name,mode,bef)
    def __str__(self):
        return  str(self.file)
    def __repr__(self):
        return 'self.file'
    def write(self,line):
        self.file.write(line.upper())
    def __getattr__(self, attr):
        return getattr(self.file, attr)
CN=canopen(r'E:\workspace\jiaoben\classtest\test.txt',"r")
for eachline in CN:
    print eachline
