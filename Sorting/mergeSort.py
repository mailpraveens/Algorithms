#To run just type python mergeSort.py in the terminal, you can change the input at the last line of this file

# This is written after refering the CLRS book and hints from the site http://en.literateprograms.org/Merge_sort_(Python)

#The merge method takes in the two subarrays and creates a output array
def merge(left, right):
	result = []
	i , j = 0 , 0
	while i < len (left) and j < len (right): # iterate through both arrays and arrange the elements in sorted order
		if left[i] <= right [j]:
			result.append(left[i])
			i+=1
		else:
			result.append(right[j])
			j+=1

#The loop may break before all elements are copied hence append the remaining elements
	result += left[i:]
	result += right[j:]
	return result


#The mergesort method to split the arrays into smaller subarrays
def mergesort(lst):
	if len(lst) <= 1:
		return lst
	middle = int(len(lst) / 2)
	left = mergesort(lst[:middle])
	right = mergesort(lst[middle:])
	return merge(left, right)


if __name__ == '__main__':
	print mergesort([3, 4, 8, 0, 6, 7, 4, 2, 1, 9, 4, 5])
