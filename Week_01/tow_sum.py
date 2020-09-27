#!/usr/bin/python3
# -*-coding:utf-8 -*-

'''
@Author  : Dan Yang
@Date    : 2020/9/27 01:29

'''

'''
1、两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

class Solution(object):
    def tow_sum(self, nums, target):
        '''
        :param nums: list[int]
        :param target: int
        :return: list[int]
        '''
        # 思路：空间换时间
        # 采用map保存以及遍历的数，及其索引，后续遍历中，可直接查找target-nums[i]是否在map中即可
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)

        buff_map = {}

        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in buff_map:
                return [buff_map[temp], i]
            else:
                buff_map[nums[i]] = i



if __name__ == '__main__':

    sl = Solution()

    test_cases = [[[2, 7, 11, 15], 9],[[0,1], 0], [[], 0]]

    for case in test_cases:
        print('input:', 'array:', case[0], 'target:', case[1])
        result = sl.tow_sum(case[0], case[1])
        print('output:', result)



