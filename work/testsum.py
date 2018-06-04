import sys
import requests
def check_location(url,times):
	list =[]
	for i in range(times):
		r = requests.get(url, allow_redirects=False)
		if r.status_code == 302:
			list.append(r.headers['location'])
	return list
def Probability(lists):
	list_new = list(set(lists))
	for i in list_new:
		print i,":",lists.count(i)
if __name__ == '__main__':
	#strs ="0319"
	#lists = check_location("http://cmcdl.cmcm.com/download?cid=4",500)
	#Probability(lists,strs)
	#strs ="0319"
	#lists1 = check_location("http://cmcdl.cmcm.com/download?cid=5",500)
	#Probability(lists1,strs)
	strs ="20180509165339"
	lists2 = check_location("http://cmcdl.cmcm.com/download?cid=1",50)
	Probability(lists2)
	#strs ="opt"
	#lists3 = check_location("http://cmcdl.cmcm.com/download?cid=3",500)
	#Probability(lists3,strs)
