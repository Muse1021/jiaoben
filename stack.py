__author__ = 'Muse'
class pystack:
    def __init__(self,size=20):
        self.s=[]
        self.size=size
        self.loc=-1
    def into(self,value):
        if self.loc<self.size-1:
            self.s.append(value)
            self.loc+=1
        else:
            print"it is full !"
    def out(self):
        if self.loc==-1:
            print "it is empty !"
        else:
            element=self.s[self.loc]
            self.s=self.s[:-1]
            self.loc -= 1
            return  element
    def showloc(self):
        return  self.loc
    def empty(self):
        self.s=[]
if __name__=="__main__":
    S=pystack()
    for i in range(10):
        S.into(i)
    print S.showloc()
    for i in range(10):
        print S.out()