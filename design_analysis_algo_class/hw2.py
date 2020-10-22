#insertion sort
def recursive_insertion_sort(array,length):
    #if theres a length of 1 just return
    if length < 2:
        return array
    recursive_insertion_sort(array,length-1)
    #find the last element
    last_element = array[length-1]
    #right pointer
    temp = length-2
    while (temp>=0 and array[temp]>last_element):
        #left pointer and increment
        array[temp+1] = array[temp]
        #right pointer and decrement
        temp = temp-1
    #switch last elements
    array[temp+1]=last_element
    return array

# merge sort 
def mergeSort(array): 
    if len(array) < 2:
        return array
    end_array = []
    #find the midpoint
    midpoint = int(len(array)/2)
    #split the array into two sub arrays
    right_sub_array = mergeSort(array[midpoint:])
    left_sub_array = mergeSort(array[:midpoint])
    while (len(left_sub_array) > 0) and (len(right_sub_array) > 0):
        if left_sub_array[0] > right_sub_array[0]:
            end_array.append(right_sub_array[0])
            right_sub_array.pop(0)
        else:
            end_array.append(left_sub_array[0])
            left_sub_array.pop(0)
    end_array = end_array + left_sub_array
    end_array = end_array + right_sub_array
    return end_array

# quick sort   
def partition(array, first_index, last_index):
    i = (first_index - 1)
    pivot = array[last_index]
    for j in range(first_index, last_index):
        if array[j] <= pivot:
            i += 1
            temp1 = array[i]
            temp2 = array[j]
            array[i] = temp2
            array[j] = temp1
    temp3 = array[i+1]
    temp4 = array[last_index]
    array[i+1] = temp4
    array[last_index] = temp3
    return (i+1)
     
def quick_sort(array, first_index, last_index):
    if first_index < last_index:
        pivot_index = partition(array, first_index, last_index)
        quick_sort(array, pivot_index+1, last_index)
        quick_sort(array, first_index, pivot_index-1)
    return array

#main program to run
#file_path is where the the test file needs to be
def main(file_path):
    file=open(file_path, "r")
    contents = file.read().split()
    for i in range(len(contents)):
        contents[i] = int(contents[i])
    print("recursive_insertion_sort")
    print(recursive_insertion_sort(contents,len(contents)))
    print("merge sort")
    print(mergeSort(contents))
    print("quick  sort")
    print(quick_sort(contents, 0, len(contents)-1))
    

