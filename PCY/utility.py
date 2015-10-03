import itertools
import sys
from itertools import combinations
numberOfBuckets = 20
support = 4

#takes :  single itemset. For ex [a,b,c]
#return : bucket to which the itemset is hashed
def generateHash(singleItemset):
	total = 103 #intialised with a prime number
	for item in singleItemset:
		total+=ord(item)
	return total%numberOfBuckets


def generateBitMap(hashTable):
	bitmap = 0
	print ("hashtable in bitmap", hashTable)
	print  "{0:b}".format(bitmap)
	for k,v in hashTable.iteritems():
		#print ("v="+str(v),"support="+str(support),"type of v=",type(v),"type of support=",type(support))
		

		if v >= int(support):
			
			bitmap = bitmap | 1<<int(k)
			#print ("key="+str(k),"support="+str(v),"{0:b}".format(bitmap))

	print ("bitmap",bitmap);
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
			print ("ele",ele,"hashkey=",hashKey,"hashCount=",hashTable[hashKey])	

	return hashTable


def generateFrequentItemsets(bitmap,baskets,size,previousFrequentItemsets):
	frequentItemsetsCandidates ={}
	subsets = set()
	result=[]
	for line in baskets:
		print ("line=",line)
		for subset in itertools.combinations(line, size):
	 		#print("subset",subset)
	 		subsets.add(subset)

	print ("previousFrequentItemsetsssssssssssssssssssssssss",previousFrequentItemsets)
	#print ("subsets",subsets,"size=",size);
	for subset in subsets:
		
		'''a=[]
		for item in itertools.combinations(subset, size-1):
	 		a.append(item)
		'''	
		print ("paaaaaas=",size,"subset",subset)
		
		count = 0
		temp = itertools.combinations(subset, size)
		for item in temp:  
			if item in previousFrequentItemsets:
				count+=1

		if bitmapLookup(bitmap,list(subset)) and count==len(list(temp)):	
			
			frequentItemsetsCandidates.setdefault(subset,0)
			#frequentItemsetsCandidates[subset]+=1

	#print ("frequentItemsets candidates", frequentItemsetsCandidates)
	
	for line in baskets:
		
		for subset in itertools.combinations(line, size):
			if subset in frequentItemsetsCandidates.keys():
				
				frequentItemsetsCandidates[subset] +=1

	#print ("freqent itemset keys",frequentItemsetsCandidates.keys(),"frequency",size)
	for k,v in frequentItemsetsCandidates.iteritems():
		
		print ("candidate key",k,"frequency",v)
		if int(v)>=int(support):
			result.append(k)

	#print ("result=",sorted(result))
	return sorted(result)
	
def bitmapLookup(bitmap,itemSet):
	hashValue = 1<<int(generateHash(itemSet))
	#print ("hashValue=","{0:b}".format(hashValue),"bitmap=","{0:b}".format(bitmap), hashValue & bitmap > 0)
	
	return True if hashValue & bitmap != 0 else False


def generateBasketsFromInput(rawdata):
  d={}
  baskets=[]
  lines = rawdata.readlines()
  for line in lines:
    line=line.strip().split(",")
    baskets.append(sorted(line))
  return baskets

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
		bucket = int(sys.argv[3])
		inputfile = open(sys.argv[1])
     
    	#reading input from file
		baskets = generateBasketsFromInput(inputfile)
		
		size=2
		Pass=1
		hashTable={}

		while len(hashTable.keys())>0 or Pass==1:
			if Pass ==1:
				frequentItemsets= generateFrequentSingletons(baskets)
			else:
				bitmap = generateBitMap(hashTable)

				previousFrequentItemsets=frequentItemsets
				#print ("previous",previousFrequentItemsets)
				frequentItemsets= generateFrequentItemsets(bitmap, baskets, size-1,previousFrequentItemsets)
				
			print ("frequent itemsets for pass=",size-1,frequentItemsets)
			hashTable = generateHashTable(baskets, size)
			print ("hashtable", hashTable,"pass",size)
			Pass +=1
			size+=1