# Append or Add a new element
friends = ["Batman", "Robin", "Wonderwoman", "Aquaman"]
friends.append("Superman")
print(friends)

# length of list
friends = ["Batman", "Robin", "Wonderwoman", "Aquaman"]
count = len(friends)
print(count)

# removing of list
friends = ["Batman", "Robin", "Wonderwoman", "Aquaman"]
friends.remove("Aquaman")
print(friends)

# get the lowest number in a list
nums = [12, 54, -24, 116]
print(min(nums))

# get the highest number
nums = [12, 54, -24, 116]
print(max(nums))

# element existence
friends = ["Batman", "Robin", "Wonderwoman", "Aquaman"]
print("Aquaman" in friends)

# combining two lists
first_nums = [1, 2, 3, 4, 5]
second_nums = [9, 8, 7, 6, 0]
all_nums = first_nums + second_nums
print(all_nums)

# taking out the last element of a list
nums = [1, 2, 3, 4, 5]
nums.pop()
print(nums)

# sorting list - string
friends = ["Batman", "Robin", "Wonderwoman", "Aquaman"]
friends.sort()
print(friends)

# sorting list
nums = [1, 2, 3, 4, 5, 44, -66, 47]
nums.sort()
print(nums)

# sort in reverse
friends = ["Batman", "Robin", "Wonderwoman", "Aquaman"]
friends.reverse()
print(friends)
