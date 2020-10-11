#!/usr/bin/python3
# -*-coding:utf-8 -*-

'''
@Author  : Dan Yang
@Date    : 2020/10/11 20:53

'''
'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

https://leetcode-cn.com/problems/two-sum

'''

class Solution(object):

    def two_sum1(self, nums, target):

        '''
        :param nums:
        :param target:
        :return:
        '''
        # 暴力解法：两层循环查找目标值
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(1)

        if not nums or len(nums) < 2:
            return []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def two_sum2(self, nums, target):
        '''

        :param nums:
        :param target:
        :return:
        '''
        # 空间换时间
        # 采用dict保存已访问的数据
        # 时间复杂度O(n)
        # 空间复杂度O(n)

        if not nums or len(nums) < 2:
            return []

        buff = {}
        for i in range(len(nums)):
            sub = target - nums[i]
            if sub in buff:
                return [buff[sub], i]
            else:
                buff[nums[i]] = i

if __name__ == '__main__':
    sl = Solution()

    test_cases = [[[2, 7, 11, 15], 9],[[0,1], 0], [[], 0]]

    for case in test_cases:
        print('input:', 'array:', case[0], 'target:', case[1])
        result = sl.two_sum1(case[0], case[1])
        print('output:', result)
