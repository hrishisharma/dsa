def insertionSort(arr1):

	
	for i in range(1, len(arr1)):
                key = arr1[i]
		j = i-1
		while j >=0 and key < arr1[j] :
				arr1[j+1] = arr1[j]
				j -= 1
		arr1[j+1] = key

arr1= [12, 11, 13, 5, 6]
insertionSort(arr1)
print ("Sorted array is:")
for i in range(len(arr1)):
	print ("%d" %arr1[i])
