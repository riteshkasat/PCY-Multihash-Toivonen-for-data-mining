import itertools
import sys
from itertools import combinations

#takes :  single itemset. For ex [a,b,c]
#return : bucket to which the itemset is hashed
def generateHash(singleItemset):
	total = 41 #intialised with a prime number
	for item in singleItemset:
		total+=ord(item)
	return total%bucketCount

def generateBitMap(hashTable):
	bitmap = 0
	for k,v in hashTable.iteritems():		
		if v >= int(support):	
			bitmap = bitmap | 1<<int(k)
	return bitmap

#takes : list of baskets. For ex: [['a','d'],['f','g']]
#return : hashTable
def generateHashTable(baskets, size):
	hashTable={}
	for line in baskets:
		subsets = []
		for subset in itertools.combinations(line, size):
	 		subsets.append(subset)
		
		for ele in subsets:
			hashKey = generateHash(ele)
			hashTable.setdefault(hashKey,0)
			hashTable[hashKey]+=1	
	return hashTable


def generateFrequentItemsets(baskets,size,bitmap,previousFrequentItemsets):
	frequentItemsetsCandidates ={}
	subsets = set()
	result=[]
	for line in baskets:
		for subset in itertools.combinations(line, size):
	 		subsets.add(subset)

	for subset in subsets:
		count = 0
		temp = itertools.combinations(subset, size-1)
		for item in temp:  
			if item in previousFrequentItemsets:
				count+=1

		if bitmapLookup(bitmap,list(subset)) and count==len(list(temp)):	
			frequentItemsetsCandidates.setdefault(subset,0)
			
	for line in baskets:
		for subset in itertools.combinations(line, size):
			if subset in frequentItemsetsCandidates.keys():
				frequentItemsetsCandidates[subset] +=1

	for k,v in frequentItemsetsCandidates.iteritems():
		if int(v)>=support:
			result.append(list(k))
	return sorted(result)
	
def bitmapLookup(bitmap,itemSet):
	hashValue = 1<<int(generateHash(itemSet))	
	return True if hashValue & bitmap != 0 else False

def generateFrequentSingletons(baskets):
	d={}
	result=[]
	for line in baskets:
		for ele in line:
			d.setdefault(ele,0)
			d[ele]+=1
	
	for k,v in d.iteritems():
		if v>=int(support):
			result.append(k)

	return sorted(result)
		
if __name__ == '__main__':
		support = int(sys.argv[2])
		bucketCount = int(sys.argv[3])
		inputfile = open(sys.argv[1])
		baskets=[]
		#reading input from file
		lines = inputfile.readlines()
		for line in lines:
			line=line.strip().split(",")
			baskets.append(sorted(line))
		
		size=1; hashTable={}
		frequentItemsets= generateFrequentSingletons(baskets)
		bitmap=0;previousFrequentItemsets=[]
		while len(frequentItemsets)>0 or size==1:
			if size==1:
				frequentItemsets= generateFrequentSingletons(baskets)
				print (frequentItemsets); print
			else:
				bitmap = generateBitMap(hashTable)
				previousFrequentItemsets=frequentItemsets
				frequentItemsets= generateFrequentItemsets(baskets,size,bitmap,previousFrequentItemsets)
				print (frequentItemsets); print
			
			
			size +=1
			hashTable = generateHashTable(baskets, size)
			if len(frequentItemsets)==0:
				 	sys.exit()
			print (hashTable); 
			
			