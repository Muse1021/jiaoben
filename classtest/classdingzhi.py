__author__ = 'Muse'
class judgefloat(object):
    def __init__(self,var):
        assert isinstance(var,float)
        self.vlaue=round(var,2)
    def showvalue(self):
        print self.vlaue
try:
    test = judgefloat(2.1183)
    test.showvalue()
except AssertionError,value:
    print value
