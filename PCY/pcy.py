import sys
import traceback

def generateBasketsFromInput(rawdata):
  d={}
  baskets=[]
  lines = rawdata.readlines()
  for line in lines:
    line=line.strip().split(",")
    baskets.append(line)
    # for ele in line:
    #   d.setdefault(ele,0)
    #   d[ele]+=1
  return baskets    

def generateItemCountsTable(inputdata):
    
    d={}
    
    for line in inputdata:
      for ele in line:
        d.setdefault(ele,0)
        d[ele]+=1
    return d

def buildHashTable():
    print

if __name__ == '__main__':
  try:
    inputargs = (sys.argv[1], sys.argv[2], sys.argv[3])
    inputfile = open(sys.argv[1])
  
  except Exception, err:
    print("Invalid input! Try again!")
    sys.exit()

  
  try:  
    #reading input from file
    d = generateBasketsFromInput(inputfile)
    
    print d
    #generating item counts table
    itemcounttable = generateItemCountsTable(d)    
    print itemcounttable
  except Exception, err:
    print(traceback.format_exc())
  





