def binarysearch(mylist, key):
	if mylist == None:
		return -1

	mid = int(len(mylist)/2)

	if mylist[mid] == key:
		return mid

	if mylist[mid]>key:
		return binarysearch(mylist[mid+1:],key)

	else
		return binarysearch(binarysearch[:mid-1],key)



if __name__ == 'main':
	a= [12,34,56,78,90]

	print binarysearch(a,90)