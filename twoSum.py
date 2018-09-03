import ast
import sys

# https://leetcode.com/problems/two-sum/description/
def twoSum( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    nums = sorted(nums) # O(nlog(n)) time with merge sort
    result = []
    linear_val = None
    
    
    for val in nums:
        complement_index = recursiveBinarySearch(nums, target - val, 0, len(nums)-1)
        print("complement_index", complement_index, val)
        if complement_index != None:
            linear_val = val
            break
    
    result.append(complement_index)
    result.append(nums.index(linear_val))
    result = sorted(result)
    return result

# log(n) time
def recursiveBinarySearch( nums, target, start, end):
    print("call me to find ", target, "from", start, "to", end)
    if start < 0 or end > len(nums) - 1: # index out of bound
        return None
    
    # only two elements
    if start + 1 == end and nums[start] != target and nums[end] != target:
        return None # not found
    elif nums[start] == target:
        return start
    elif nums[end] == target:
        return end
    
    # binary search
    mid_index = int((end-start)/2) + start
    mid_val = nums[mid_index]
    if (mid_val == target):
        return mid_index
    elif mid_val > target:
        return recursiveBinarySearch( nums, target, start, mid_index - 1) # search left half
    else: # search right half
        return recursiveBinarySearch( nums, target, mid_index + 1, end) # search right half

if __name__ == '__main__':
    nums = ast.literal_eval(sys.argv[1])
    target = int(sys.argv[2])
    result = twoSum(nums, target)
    print(result)
