#First partition the input array into two groups
# Partitioning alogorithm creates smaller array with elements on left and 
# right being smaller and greater than the pivot

def partiton(a, left, right):
	i = left + 1 # Initialiase i to one more assuming pivot is at position left
	pivot = a[left]

	for j in range(left+1, right+1): #Iterate over the remaining array
		if (a[j] < pivot):
			a[i], a[j] = a[j], a[i] #Swap the values
			i = i+1 #Increment i


	pos = i - 1
	a[left], a[pos] =  a[pos], a[left]
	return pos



def quickSort(a, left, right):
	if(left <  right):
		pivot = partiton(a, left, right)
		quickSort(a, left, pivot-1)
		quickSort(a, pivot+1, right)


if __name__ == '__main__':
	a = [3, 4, 8, 0, 6, 7, 4, 2, 1, 9, 4, 5]
	quickSort(a ,0 , len(a)-1)
	print a
