def bubble(list1):  
    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp  
    return list1  
  
list1 = [53,43, 18, 76, 47, 22,11,6,99]  
print("The unsorted list is: ", list1)  
print("The sorted list is: ", bubble(list1))
