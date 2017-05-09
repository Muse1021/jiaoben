import sys
import requests
import yaml
def createurl(lists):
    url =[]
    for i in lists:
        print i
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
def Probability(lists,*str):
	count = len(str)
	print len(lists)
	A= [0]*count
	for i in lists:
		for j in str:
			if j in i:
#				print j,"======",i,"====",str.index(j)
				A[str.index(j)] +=1
				#print i

	print A
if __name__ == '__main__':
    f = open('data.yaml')
    x = yaml.load(f)
    print x.keys()
    print createurl(x.keys())
#   strs =["A","B","C"]
#	lists3 = check_location("http://cmcdl.cmcm.com/download?cid=3",100)
#	Probability(lists3,"http://dl.cm.ksmobile.com/static/res/f1/dc/CleanMaster_v51721068_new_sign_20170508183344_2010006647.apk")
