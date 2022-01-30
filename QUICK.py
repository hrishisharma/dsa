def par(a, start, end):  
    i = (start - 1)  
    pivot = a[end]
      
    for j in range(start, end):  
         
        if (a[j] <= pivot):  
            i = i + 1  
            a[i], a[j] = a[j], a[i]  
      
    a[i+1], a[end] = a[end], a[i+1]  
  
    return (i + 1)  
      

def quick(a, start, end):
    if (start < end):  
        p = par(a, start, end)  
        quick(a, start, p - 1)  
        quick(a, p + 1, end)  
  
          
def printArr(a):  
    for i in range(len(a)):  
        print (a[i], end = " ")
a = [22,45,11,99,10,5,6,99,20]  
print("Before sorting array elements are - ")  
printArr(a)  
quick(a, 0, len(a)-1)  
print("\nAfter sorting array elements are - ")  
printArr(a)
  
      

