
#?22. Write a Python program to count the number 4 in a given list.

def list_count_4(nums):
    count = 0
    for nums in nums:
        if nums == 4:
            count += 1

    return count

print(list_count_4([1, 2, 3, 4, 5]))
print(list_count_4([4, 2, 4, 5, 6]))