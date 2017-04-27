import sys
import requests
def check_location(url,times):
	list =[]
	for i in range(times):
		r = requests.get(url, allow_redirects=False)
		if r.status_code == 302:
			list.append(r.headers['location'])
	return list
def Probability(lists,*str):
	count = len(str)
	A= [0]*count
	for i in lists:
		for j in str:
			if j in i:
#				print j,"======",i,"====",str.index(j)
				A[str.index(j)] +=1

	print A	
if __name__ == '__main__':
	strs =["A","B","C"]
	lists3 = check_location("http://cmcdl.cmcm.com/download?cid=3",500)
	Probability(lists3,"_opt_","_B")
