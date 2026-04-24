def Array_sum(nums):
    s = 0
    for i in range(len(nums)-1,-1,-1):
        s += nums[i]
        return s
print(Array_sum([10,20,30,40]))#100


def Array_sum_recursion(nums):
    if len(nums) == 0:
        return 0
    return nums[-1] + Array_sum_recursion(nums[:-1])
print(Array_sum_recursion([10,20,30,40]))#100

#create a function to reverse a array using recursion
def reverse_array(nums,i,j):
    if i >= j:
        return
    nums[i], nums[j] = nums[j], nums[i]
    reverse_array(nums, i + 1, j - 1)
arr = [1, 2, 3, 4, 5]
reverse_array(arr, 0, len(arr) - 1) 
print(arr)#[5, 4, 3, 2, 1]  


#create a function to reverse a string using recursion
def reverse_string(s):  
    if len(s) == 0:
        return s
    return s[-1] + reverse_string(s[:-1])   
print(reverse_string("Hello"))#olleH


def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
print(is_palindrome("abc"))#True
print(is_palindrome("mam"))#False