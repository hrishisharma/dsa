def selectionSort(array,s):
   
    for step in range(s):
        min_idx = step

        for i in range(step + 1, s):
         
            if array[i] < array[min_idx]:
                min_idx = i
         
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = [11,66,78,33,10,44,23,27]
print("Array:",data)
s = len(data)
selectionSort(data, s)
print('Sorted Array in Ascending Order:',data)

