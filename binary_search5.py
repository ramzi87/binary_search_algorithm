
mylist = [2,4,3,12,6,5,8,22,14,16,10,11,9,7,8,33,87,44]
item = 4

# ======= Linear Search =========
def linear_search(mylist,item):
	for x in range(len(mylist)):
		if mylist[x] == item:
			return True
	return False

print(linear_search(mylist,item))


# =========== Iterative Binary Search ===========
def binary_search(mylist,target):
	lower = 0
	higher = len(mylist) - 1
	mylist.sort()

	while lower <= higher:
		mid = (lower + higher) // 2
		if mylist[mid] == target:
			return("The number {} is in the list at"
			" the index {}".format(item,mylist.index(item)))
			#return True

		elif mylist[mid] < target:
			lower = mid + 1
		else:
			higher = mid - 1

	return False

print(binary_search(mylist,item))


# =========== Recursive Binary Search ===========
def rec_binary_search(lst,target,lower,higher):
	lst.sort()
	if lower > higher:
		return False
	else:
		mid = (lower + higher) // 2
		if lst[mid] == target:
			return True
		elif lst[mid] < target:
			return rec_binary_search(lst, target, mid+1, higher)
		else:
			return rec_binary_search(lst, target, lower, mid-1)

find_nnumber = rec_binary_search(mylist, item, 0, len(mylist)-1)

if find_nnumber:
	print("The number {} is in the list at the index {}".format(item,mylist.index(item)))
else:
	print("The number you are looking for in not in the list")


