import sys
import requests
import yaml
def createurl(lists):
    url =[]
    for i in lists:
        strall = "http://cmcdl.cmcm.com/download?cid="+i
        url.append(strall)
    return url
def check_location(url,times):
    list =[]
    for i in range(times):
        r = requests.get(url, allow_redirects=False)
        if r.status_code == 302:
            list.append(r.headers['location'])
    return list
def Probability(lists,str):
    count = len(str)
#    print count,len(lists)
    A= [0]*count
    for i in lists:
        for j in str:
            #print j,"======",i,"====",str.index(j)
            if j in i:
                #print j,"======",i,"====",str.index(j)
                A[str.index(j)] +=1
                #print i

    print A
def result(data,times):
    urllists = createurl(data.keys())
    j=len(urllists)
    for i in range(j):
        list = check_location(urllists[i],times)
        strs = data.values()[i].values()
        print data.values()[i].keys()
        Probability(list,strs)
if __name__ == '__main__':
    f = open('data.yaml')
    x = yaml.load(f)
    result(x,5)


#    strs =["http://dl.cm.ksmobile.com/static/res/f1/dc/CleanMaster_v51721068_new_sign_20170508183344_2010006647.apk","http://dl.cm.ksmobile.com/static/res/12/5e/CleanMaster_v51721068_old_sign_20170508183502_2010006647.apk"]
#    lists3 = check_location("http://cmcdl.cmcm.com/download?cid=3",10)
#    Probability(lists3,strs)
