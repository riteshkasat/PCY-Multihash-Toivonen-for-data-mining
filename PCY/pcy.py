import sys
import traceback
import itertools
from itertools import combinations

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
    for line in baskets:
      for ele in line:
        d.setdefault(ele,0)
        d[ele]+=1
    return d

def buildHashTable(baskets):
    hashtable={}
    for basket in baskets:
      for subset in itertools.combinations(basket, 2):
        #-------TODO : REPLACE 20 BY BASKET COUNT-------------
        key = (ord(subset[0])+ord(subset[1]))%20

        hashtable.setdefault(key,[])
        if len(hashtable[key])>0:
          hashtable[key][0]+=1
        
        else:
          hashtable[key].append(1)

        hashtable[key].append(subset)

    for k in hashtable:
      print (k,hashtable[k])   

    return hashtable 

def getFrequentPairs(hashtable,baskets):
    candidatepairs=set()
    for k in hashtable:
      #-------TODO : REPLACE 4 BY SUPPORT COUNT-------------
      if hashtable[k]>4:
        


if __name__ == '__main__':
  try:
    inputargs = (sys.argv[1], sys.argv[2], sys.argv[3])
    support = sys.argv[2]
    bucket = sys.argv[3]
    inputfile = open(sys.argv[1])
    

  except Exception, err:
    print("Invalid input! Try again!")
    sys.exit()

  
  try:  
    #reading input from file
    d = generateBasketsFromInput(inputfile)
    
    #generating item counts table
    itemcounttable = generateItemCountsTable(d)    
    hashtable = buildHashTable(d)
    


  except Exception, err:
    print(traceback.format_exc())
  





