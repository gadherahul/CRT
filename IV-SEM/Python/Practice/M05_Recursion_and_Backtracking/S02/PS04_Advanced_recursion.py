#Digit root
def digit_root(n):
    if n < 10:
        return n
    return digit_root(n // 10 + n % 10)

print(digit_root(456))  # Output: 6

def is sorted_Array(nums):
    if len(nums) <= 1:
        return True
    if nums[0] > nums[1]:
        return False
    return is_sorted_Array(nums[1:])    
print(is_sorted_Array([10, 20, 30, 40, 50]))#True
print(is_sorted_Array([10, 2, 30, 15, 50]))