# Linear Search
# Finding an element
nums = [10, 14, 34, 54, 65, 67, 36, 23, 33, 45, 786, 78, 12, 17, 15]
# loop for finding number 33
for num in nums:
    if num == 33:
      print("I got the 33")
    
###############################################################################################################

# Binary Search
# defining binary search
def binary_search(list, find_value):
    low = 0
    high = len(list)
    while low <= high:
        mid = (low + high) // 2     # using floor division to find the mid value of the index
        if list[mid] < find_value:
            low = mid
        elif list[mid] > find_value:
            high = mid
        else:
            return mid
          
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index = binary_search(nums, 7)
print(index)
          
###############################################################################################################
