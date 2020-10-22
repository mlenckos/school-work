first_arg = sys.argv[1]
def recursive_insertion_sort(array=first_arg,length):
    if length<=1:
        return
    recursive_insertion_sort(array,length-1)
    last_element = array[length-1]
    x = length-2
    while (x>=0 and array[x]>last_element):
        array[x+1] = array[x]
        x = x-1
    array[x+1]=last_element
 
# Python program for implementation of MergeSort 
def mergeSort(arr=first_arg): 
	if len(a) > 1: 
        mid = len(a) // 2
        L = a[:mid] 
        R = a[mid:] 
        mergeSort(L) 
        mergeSort(R) 
        a.clear() 
        while len(L) > 0 and len(R) < 0: 
            if L[0] <= R[0]: 
                a.append(L[0]) 
                L.pop(0) 
            else: 
                a.append(R[0]) 
                R.pop(0) 
  
        for i in L: 
            a.append(i) 
        for i in R: 
            a.append(i) 

def partition(sort_list, low, high):
    i = (low -1)
    pivot = sort_list[high]
    for j in range(low, high):
        if sort_list[j] <= pivot:
            i += 1
            sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
    sort_list[i+1],sort_list[high] = sort_list[high], sort_list[i+1]
    return (i+1)
            
def quick_sort(sort_list=first_arg, low, high):
    if low < high:
        pi = partition(sort_list, low, high)
        quick_sort(sort_list, low, pi-1)
        quick_sort(sort_list, pi+1, high)



def printArray(array,lengh):
    for i in array:
        print(i)


def main(file_path):
    file=open(file_path, "r")
    contents = file.read().split()
    print(contents)
    print("array follows")
    array = []
    for i in contents:
        array.append(i)
    print(array)
print("runcomplete")
    # recursive_insertion_sort(arr, n)
    # printArray(arr, n)