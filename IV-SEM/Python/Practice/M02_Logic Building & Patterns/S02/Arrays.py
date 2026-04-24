from typing import Mapping


def Reverse_list(li):
    res =[]
    for i in range(len(li)-1,-1,-1):
        res.append(li[i])
    return res

li = [1,2,3,4,5]
print(Reverse_list(li))     



def Reverse_list(li):
    for i in range(len(li)//2):
        li[i],li[len(li)-1-i] = li[len(li)-1-i],li[i]
    return li

def is_sorted(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False    
    return True
    pass
print(is_sorted([12,23,45,56,78]))#true
print(is_sorted([45,20,36,78,1]))#false

#Counting the frequency of elements 
input = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
freq = {}       
for i in input:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)
output = {1:3,2:3,3:3,4:3,5:3}
print(output)   
