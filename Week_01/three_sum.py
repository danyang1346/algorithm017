#!/usr/bin/python3
# -*-coding:utf-8 -*-

'''
@Author  : Dan Yang
@Date    : 2020/9/30 16:08

'''
'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

链接：https://leetcode-cn.com/problems/3sum
'''

# 解题经典参考
# 双指针+图解  +  看国际站
# 看代码，尽量简洁
class Solution(object):

    def three_sum1(self, nums):
        # 求三数加和为0，可能的不重复的组合
        # 解法1：暴力求解，3层循环遍历，但因最终结果不重复，需要在找到时，对数值做排序操作，方便去重
        # 时间复杂度：O(n^3)
        # 空间复杂度：O(1)

        if not nums:
            return

        ret_values = []
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]+ nums[j] + nums[k] == 0:
                        temp = sorted([nums[i], nums[j], nums[k]])
                        if not temp in ret_values:
                            ret_values.append(temp)
        return ret_values


    def three_sum2(self, nums):

        # 解法2：先排序，再采用双指针法，逐渐逼近。第一次循环，遍历所有数值，第二次循环，双指针，找所有可能等于-x的组合，并保存
        # 时间复杂度: O(klogn) + O(n)
        # 空间复杂度: O(1)
        if not nums or len(nums) < 3:
            return []

        nums = sorted(nums)

        ret_values = []
        for i in range(len(nums)-2):
            if nums[i] > 0:
                return ret_values
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] + nums[i] == 0 :
                    ret_values.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left += 1

                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                else:
                    right -= 1

        return ret_values


if __name__ == '__main__':

    sl = Solution()

    test_cases = [[-1,0,1,2,-1,-4], [], [-1, 2], [2,3,1]]

    for case in test_cases:
        print('input:', 'array:', case)
        result = sl.three_sum2(case)
        print('output:', result)
    pass