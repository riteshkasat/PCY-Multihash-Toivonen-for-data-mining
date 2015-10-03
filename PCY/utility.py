import itertools
import sys
from itertools import combinations
numberOfBuckets = 8
support = 2

#takes :  single itemset. For ex [a,b,c]
#return : bucket to which the itemset is hashed
def generateHash(singleItemset):
	total = 103 #intialised with a prime number
	for item in singleItemset:
		total+=ord(item)
	return total%numberOfBuckets

#takes : list of itemset of same size. For ex [[a,b], [a,d], [b,c]]. Here size = 2
#returns : hashtable with  0<=bucketKey<numberOfBuckets 
def generateHashTable(listOfItemSet):
	hashTable = {}
	for itemSet in listOfItemSet:
		hashKey = generateHash(itemSet)
		hashTable.setdefault(hashKey,0)
		hashTable[hashKey] += 1
	return hashTable

#takes :  hashTable. Can be for pairs, triplets etc. But only one of them at a given time.
#return : bucket to which the itemset is hashed
def generateBitMap(hashTable):
	bitmap = 0
	print  "{0:b}".format(bitmap)
	for k,v in hashTable.iteritems():
		if v >= support:
			bitmap = bitmap | 1<<int(k)
			print ("key="+str(k),"support="+str(v),"{0:b}".format(bitmap))

	return bitmap


#takes : list. contains only singletons. For ex: ['a','d','f']
#return : all combinations of given size. For ex: size=2, then output = [['a','b'],['a','f'],['d','f']]
def generateItemCombinations(listOfSingletons, size):
	 subsets = []
	 listOfSingletons = sorted(listOfSingletons)
	 for subset in itertools.combinations(listOfSingletons, size):
	 	subsets.append(subset)
	 return subsets


def bitmapLookup(bitmap,itemSet):
	hashValue = 1<<int(generateHash(itemSet))
	return True if hashValue & bitmap > 0 else False


def generateBasketsFromInput(rawdata):
  d={}
  baskets=[]
  lines = rawdata.readlines()
  for line in lines:
    line=line.strip().split(",")
    baskets.append(sorted(line))
  return baskets

def generateItemCountsTable(baskets):
	d={}
	result=[]
	for line in baskets:
		for ele in line:
			d.setdefault(ele,0)
			d[ele]+=1
	
	for k,v in d.iteritems():
		print (k,v)
		if v>=int(support):
			result.append(k)

	return sorted(result)
		
if __name__ == '__main__':
	
		
		support = sys.argv[2]
		bucket = sys.argv[3]
		inputfile = open(sys.argv[1])
     
    	#reading input from file
		d = generateBasketsFromInput(inputfile)

    	#generating item counts table
		itemCountTable = generateItemCountsTable(d)     
		print itemCountTable
		size=2

		while len(itemcounttable)>0:
			listOfAllPossibleItemSets = generateItemCombinations(itemCountTable, size)	
			hashTable = generateHashTable(listOfAllPossibleItemSets,size)

