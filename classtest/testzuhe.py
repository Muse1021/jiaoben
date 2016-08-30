__author__ = 'Muse'
class community(object):
    def __init__(self,w,m,num):
        self.w=woman(w)
        self.m=man(m)
        self.num=num
    def showall(self):
        print self.w.showw()
        print self.m.showm()
        print self.num
class woman(object):
    def __init__(self,w):
        self.w=w
    def showw(self):
        return self.w
class man(object):
    def __init__(self,m):
        self.m=m
    def showm(self):
        return self.m
class town(community):
    def __init__(self,w,m,num,name):
        community.__init__(self,w,m,num)
        self.name=name
    def showtown(self):
        print self.name
        print self.w.showw()
        print self.m.showm()
        # super(community,self).showall()
        print self.num

# com=community("g","l","love")
# com.showall()
tn= town("g","l","love","forever")
tn.showtown()