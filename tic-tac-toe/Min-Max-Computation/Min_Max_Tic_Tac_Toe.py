# TASK 2.2 - SECOND    #
# MINMAX COMPUTATION   #
# WITH MEMORY          #
########################
# Arash Nasirtafreshi  #
# Mana Azamat          #
# Mohammad Saifullah   # 
# Mudra Shah           #
# Tanya Agarwal        #
# Urmimala Majumdar    #
# Hasan Mahmud	       #
########################


import numpy as np

nodeDict = {}
nodeExplored=[]
scoreDoct = {}
nodeMaxUtilDict = {}
nodeMinUtilDict = {}
NextMaxMove = {}
NextMinMove = {}


succDict = {}


def findOccurence(d,v):
    l = [ k for k in d if d[k]==v ]
    return len(l),l

def maxNodeUtil(node):
	nextNodeUtils={}

	if node in nodeMaxUtilDict:
		return nodeMaxUtilDict[node],NextMaxMove[node]

	mmv = -np.inf
	maxnode = 0
	for s in succDict[node]:
		minvalue,minnode = minNodeUtil(s)
		nextNodeUtils[s] = minvalue

		mmmv = max(mmv, minvalue)
		if mmv != mmmv:
			maxnode = s
			mmv = mmmv 

	nodeMaxUtilDict[node] = mmv
	NextMaxMove[node] = maxnode
	times,indices = findOccurence(nextNodeUtils,mmv)

	mmmmv = -np.inf

	if times>1:
		for i in indices:
			mv, nd = maxNodeUtil(i)
			#print mv,nd
			if mmmmv<mv:
				mmmmv = mv
				maxnode = i
	return mmv,maxnode
	


def minNodeUtil(node):
	nextscore={}
	if node in nodeMinUtilDict:
		return nodeMinUtilDict[node],NextMinMove[node]
	mmv = np.inf
	minnode = 0

	for s in succDict[node]:
		maxvalue,maxnode=maxNodeUtil(s)
		nextscore[s] = maxvalue
		mmmv = min(mmv, maxvalue)
		if mmv != mmmv:
			minnode = s
			mmv = mmmv 

	nodeMinUtilDict[node] = mmv
	NextMinMove[node] = minnode
	times,indices = findOccurence(nextscore,mmv)
	mmmmv = np.inf

	if times>1:
		for i in indices:
			mv, nd = maxNodeUtil(i)
			#print mv,nd
			if mmmmv>mv:
				mmmmv = mv
				minnode = i
	return mmv,minnode
	


	
def treeGenerator():
	succ = []

	for i in range(0,20):
		nodeDict[i]=i
	addToSucc(0,1,4)
	addToSucc(1,5,9)
	addToSucc(2,10,11)
	addToSucc(3,12,14)
	addToSucc(4,15,16)
	#addToSucc(5,17,19)
	#print succDict

	return


def addToSucc(n,i,j):
	succ = []

	for ii in range(i,j+1):
		succ.append(nodeDict[ii])
	succDict[n] = succ

def defineUtil():
	nodeMaxUtilDict[nodeDict[5]] = 18
	nodeMaxUtilDict[nodeDict[6]] = 6	
	nodeMaxUtilDict[nodeDict[7]] = 16
	nodeMaxUtilDict[nodeDict[8]] = 6
	nodeMaxUtilDict[nodeDict[9]] = 5
	nodeMaxUtilDict[nodeDict[10]] = 7
	nodeMaxUtilDict[nodeDict[11]] = 1
	nodeMaxUtilDict[nodeDict[12]] = 16
	nodeMaxUtilDict[nodeDict[13]] = 16
	nodeMaxUtilDict[nodeDict[14]] = 5
	nodeMaxUtilDict[nodeDict[15]] = 10
	nodeMaxUtilDict[nodeDict[16]] = 2

	nodeMinUtilDict[nodeDict[5]] = 18
	nodeMinUtilDict[nodeDict[6]] = 6	
	nodeMinUtilDict[nodeDict[7]] = 16
	nodeMinUtilDict[nodeDict[8]] = 6
	nodeMinUtilDict[nodeDict[9]] = 5
	nodeMinUtilDict[nodeDict[10]] = 7
	nodeMinUtilDict[nodeDict[11]] = 1
	nodeMinUtilDict[nodeDict[12]] = 16
	nodeMinUtilDict[nodeDict[13]] = 16
	nodeMinUtilDict[nodeDict[14]] = 5
	nodeMinUtilDict[nodeDict[15]] = 10
	nodeMinUtilDict[nodeDict[16]] = 2

	NextMinMove[nodeDict[5]] = None
	NextMaxMove[nodeDict[5]] = None
	


	NextMinMove[nodeDict[6]] = None
	NextMaxMove[nodeDict[6]] = None

	NextMinMove[nodeDict[7]] = None
	NextMaxMove[nodeDict[7]] = None

	NextMinMove[nodeDict[8]] = None
	NextMaxMove[nodeDict[8]] = None

	NextMinMove[nodeDict[9]] = None
	NextMaxMove[nodeDict[9]] = None

	NextMinMove[nodeDict[10]] = None
	NextMaxMove[nodeDict[10]] = None

	NextMinMove[nodeDict[11]] = None
	NextMaxMove[nodeDict[11]] = None

	NextMinMove[nodeDict[12]] = None
	NextMaxMove[nodeDict[12]] = None

	NextMinMove[nodeDict[13]] = None
	NextMaxMove[nodeDict[13]] = None

	NextMinMove[nodeDict[14]] = None
	NextMaxMove[nodeDict[14]] = None

	NextMinMove[nodeDict[15]] = None
	NextMaxMove[nodeDict[15]] = None

	NextMinMove[nodeDict[16]] = None
	NextMaxMove[nodeDict[16]] = None




def mmv(node):
	#print node, succDict[0]
	print "Tree is:  ",succDict
	mmx, maxnode = maxNodeUtil(node)
	print "Next max move of ",node," is ",maxnode," and that has util: ",mmx
	mmn, minnode = minNodeUtil(node)
	print "Next min move of ",node," is ",minnode," and that has util: ",mmn


if __name__ == '__main__':

	

	treeGenerator()
	defineUtil()
	mmv(0)


