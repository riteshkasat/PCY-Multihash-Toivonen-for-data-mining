import sys

if __name__ == '__main__':
  try:
    inputargs = (sys.argv[1], sys.argv[2], sys.argv[3])
    inputdata = open(sys.argv[1])
    print inputdata

  except:
    print "-"*60
    print "Problem with your command line input. Please try again."
    print "Hint:"
    print "1)Check if your Input file name is proper."
    print "2)Check if you passed 3 arguements to the program." 
    print "-"*60

  




