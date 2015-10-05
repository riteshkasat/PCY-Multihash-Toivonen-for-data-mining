mport itertools
import sys
from itertools import combinations

#takes :  single itemset. For ex [a,b,c]
#return : bucket to which the itemset is hashed
def generateHash(singleItemset, primeNumber):
	total = primeNumber #intialised with a prime number
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
def generateHashTable(baskets, size, primeNumber):
	hashTable={}
	for line in baskets:
		subsets = []
		for subset in itertools.combinations(line, size):
	 		subsets.append(subset)
		
		for ele in subsets:
			hashKey = generateHash(ele, primeNumber)
			hashTable.setdefault(hashKey,0)
			hashTable[hashKey]+=1	
	return hashTable


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
		

		if size==1:
			frequentItemsets= generateFrequentSingletons(baskets)
			print (frequentItemsets); print
			size +=1;	
		
		if size==2:
			bitmap1 = generateBitMap(hashTable1)
			bitmap2 = generateBitMap(hashTable2)
			previousFrequentItemsets=frequentItemsets
			frequentItemsets= generateFrequentItemsets(baskets,size,bitmap1,bitmape2, previousFrequentItemsets)
			
			if len(frequentItemsets)==0:
			 	sys.exit()
			print (frequentItemsets)
		
		hashTable1 = generateHashTable(baskets, size,41)
		hashTable2 = generateHashTable(baskets, size,53)
		print (hashTable1);
		print (hashTable2); 
		if size!=1: 
			print;
		size +=1;


	