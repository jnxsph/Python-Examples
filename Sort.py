# Built in Sort in Python
arr1 = [2, 4, 5, 7, 6, 8, 1, 9, -1]

arr1.sort()
print(arr1)

###################################################################################################################

# Swap elements
a = 5
b = 7
print(a, b)

# swapping
temp = a
a = b
b = temp
print(a, b)

###################################################################################################################

# Bubble sort
def BubbleSort(list):
  n = len(list)
  for i in range(n):                        # nested loop for every element
      for j in range(n - 1):
          if list[j] > list[j + 1]:
              temp = list[j]
              list[j] = list[j + 1]
              list[j + 1] = temp
  return list           

# calling BubbleSort algorithm function
nums = [34, 23, 54, 67, 45, 78, 11, 22, -33, -66, -54]
sort_nums = BubbleSort(nums)
print(sort_nums)


###################################################################################################################

# Selection Sort
# run a simple for loop for all elements
def SelectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):            # inner loop starts from the index i + 1
            if arr[min_idx] > arr[j]:               # loop to find out the minimum number
                min_idx = j                         # minimum will be swapped with the element at the position i

        temp = arr[i]                               # swapping the current with the min element
        arr[i] = arr[min_idx]
        arr[min_idx] = temp
    return arr
    

# calling Selection Sort Algorithm
nums = [54, 56, 76, 23, 55, 1]
sort_nums = SelectionSort(nums)
print(sort_nums)


###################################################################################################################

# Insertion Sort
# current postiion is i
def InsertionSort(arr):
    for i in range(1, len(arr)):
        insert = arr[i]                     # current element to be inserted will be arr[i]
        j = i-1                             # if the insert is smaller, it will move the current element to the right
        while insert < arr[j] and j >= 0:   # will start from j = i-1 and also check if whether j is greater tha or equals to 0
            arr[j + 1] = arr[j]
            j = j-1
        arr[j + 1] = insert                 # adding element that will be inserted in the array/ wil be done by inserting one element
    
    return arr

# calling Insertion Sort
nums = [54, 56, 76, 23, 55, 1]
sort_nums = InsertionSort(nums)
print(sort_nums)

###################################################################################################################
