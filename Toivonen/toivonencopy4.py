import itertools
import sys
from itertools import combinations
import random

negativeBorder = set()

def generateFrequentItemsets(baskets,size,previousFrequentItemsets):
	frequentItemsetsCandidates ={}
	result=[]
	for line in baskets:
		for subset in itertools.combinations(line, size):
			
			frequentItemsetsCandidates.setdefault(subset,0)
			frequentItemsetsCandidates[subset] +=1

	for k,v in frequentItemsetsCandidates.iteritems():
		if int(v)>=newSupport:
			result.append(list(k))
		else:
			if len(k)==1:
				negativeBorder.add(k)

			else:
				count =0;
				
				for subset in itertools.combinations(k, size-1):
					
					if  list(subset) not in previousFrequentItemsets:
						count+=1
						
				if count ==0:
					negativeBorder.add(k)		


	return sorted(result)


if __name__ == '__main__':
		p=0.5 #fraction of sample size
		support = int(sys.argv[2])
		inputfile = open(sys.argv[1])
		count = 0;
		baskets=[]
		lines = inputfile.readlines() #reading input from file
		for line in lines:
			line=line.strip().split(",")
			baskets.append(sorted(line))
			count+=1

		basketAfterSampling = []
		newSupport = int(0.8*p*support)
		listOfIndex= random.sample(range(count), int(p*count))
	
		for index in listOfIndex:
			basketAfterSampling.append(baskets[index])

		size = 1;
		frequenItemsets = []
		allFrequentItemsets = []

		start = True
		numberofiterations = 1
		while start:
			
			start = False
			for x in range(99):
				
				frequenItemsets =  generateFrequentItemsets(basketAfterSampling, size, frequenItemsets)
				if len(frequenItemsets)>0: 
					allFrequentItemsets.append(frequenItemsets)
					
				size+=1
				
				if frequenItemsets == []:
					d={}
					for basket in baskets:
						for ele in negativeBorder:
							if set(ele)<=set(basket):
								d.setdefault(ele,0)
								d[ele]+=1
					counter =0
					for k,v in d.iteritems():
						
						if v >= support:
							numberofiterations+=1
							
							counter +=1
							size = 1;frequentItemsets = [];allFrequentItemsets = [];basketAfterSampling=[];negativeBorder=set()
							listOfIndex= random.sample(range(count), int(p*count))
							for index in listOfIndex:
								basketAfterSampling.append(baskets[index])
							break;
									
					d1={}
					for basket in baskets:
						for ele1 in allFrequentItemsets:
							for ele2 in ele1:
								if set(ele2)<=set(basket):
									d1.setdefault(tuple(ele2),0)
									d1[tuple(ele2)]+=1

					d2 = sorted([ x for x in d1 if d1[x] >= support ])
					if counter == 0:
						print numberofiterations
						print "0.5"
						d3={}
						for x in d2:
							d3.setdefault((len(x)),[])
							d3[len(x)].append(list(x))

						for x in d3:
							print d3[x]		
						sys.exit();				
			start = True
			
			break
						