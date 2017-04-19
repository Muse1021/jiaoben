import sys
import requests
def check_location(url,times):
	list =[]
	for i in range(times):
		r = requests.get(url, allow_redirects=False)
		if r.status_code == 302:
			list.append(r.headers['location'])
	return list
def Probability(lists,str):
	A = 0
	B = 0
	for i in lists:
		if str in i:
			A+=1
		else:
			B+=1
	print A,"-----",B
if __name__ == '__main__':
	strs ="0319"
	lists = check_location("http://cmcdl.cmcm.com/download?cid=4",500)
	Probability(lists,strs)
	strs ="0319"
	lists1 = check_location("http://cmcdl.cmcm.com/download?cid=5",500)
	Probability(lists1,strs)
	strs ="f0"
	lists2 = check_location("http://cmcdl.cmcm.com/download?cid=1",500)
	Probability(lists2,strs)
	strs ="opt"
	lists3 = check_location("http://cmcdl.cmcm.com/download?cid=3",500)
	Probability(lists3,strs)
