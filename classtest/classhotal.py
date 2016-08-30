__author__ = 'Muse'
class hotelprice(object):
    def __init__(self,rp,rrate=0.085,srate=0.1):
        self.romeprice = rp
        self.romerate = rrate
        self.staterate = srate
    def thefinnalprice(self,days):
        preprice=round(self.romeprice*(1+self.romerate+self.staterate),2)
        return preprice*days
Muse = hotelprice(135)
print Muse.thefinnalprice(3)
print  Muse.__dict__