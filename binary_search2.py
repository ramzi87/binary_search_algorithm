
def binary_search(lst,item):
	found = False
	lower = 0
	higher = len(lst)-1
	lst.sort()
	while lower <= higher and not found:
		mid = (lower + higher)//2

		print("Searching for the number :"+str(lst[lower:higher]))
		print("The lower number is: "+str(lst[lower])+"List index is: "+str(lower))
		print("The middle number is: "+str(lst[mid])+"List indexis: "+str(mid))
		print("The higher number is: "+str(lst[higher])+"List index is: "+str(higher))

		print("Is it ?"+str(lst[mid]))

		if lst[mid] == item:
			print("The number is found at the index {}".format(lst.index(item)))
			found = True

		elif lst[mid] < item:
			lower = mid + 1
			print("Higher")

		else:
			higher = mid - 1
			print("Lower")

	return found

mylist = [2,3,5,4,8,7,9,11,6,14,25,37]
myitem = 3

print(binary_search(mylist,myitem))