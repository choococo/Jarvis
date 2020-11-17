# 两数之和
"""
拿到两个数和为9的索引

"""
nums = [2, 7, 11, 15]
target = 9
j = -1
for i in range(len(nums)):
    if target - nums[i] in nums:
        j = nums.index(target - nums[i], i + 1)
        break

