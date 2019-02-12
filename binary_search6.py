
def binary_search(mylist,item):
	lower = 0
	higher = len(mylist)-1
	mylist.sort()

	while lower <= higher:

		mid = (lower + higher) // 2
		if mylist[mid] == item:
			return ("The number {} is in the list"
				" at the index {}".format(item,mylist.index(item)))

		elif mylist[mid] < item:
			lower = mid + 1
		else:
			higher = mid - 1

	return False

lst = [2,3,6,4,12,10,11,9,8,7]
target = 12

find_number = binary_search(lst,target)

if find_number:
	print(binary_search(lst,target))
else:
	print("The number does not exist")