#!/usr/bin/python3
# -*-coding:utf-8 -*-

'''
@Author  : Dan Yang
@Date    : 2020/9/30 09:44

'''

'''
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2
链接：https://leetcode-cn.com/problems/container-with-most-water
'''

class Solution(object):
    # 解法一：遍历罗列，双层循环
    #        时间复杂度O(n^2)
    #        空间复杂度O(1)
    # 解法二：双指针法
    #        求面积最大，即宽度与高度乘积值最大，可以两边夹击，不断找最大面积
    #         左右height，目前小的，可以移动找较大的、
    #       时间复杂度O(n)
    #       空间复杂度O(1)

    def max_area_1(self, height):
        '''
        :param height:
        :return: 最大面积值
        '''
        if not height:
            return height

        max_area = 0
        for i in range(len(height)-1):
            for j in range(i+1, len(height)):
                area = (j - i)* min(height[i], height[j])
                max_area = max(max_area, area)
        return max_area

    def max_area_2(self, height):
        '''
        :param height:
        :return:
        '''
        if not height:
            return

        left, right = 0, len(height)-1

        max_area = 0
        while left < right:
            area = (right - left) * min(height[right], height[left])
            max_area = max(max_area, area)

            if height[right] < height[left]:
                right -= 1
            else:
                left += 1

        return max_area


if __name__ == '__main__':

    sl = Solution()

    test_cases = [[2, 7, 11, 15],[0,1], [], [1,8,6,2,5,4,8,3,7]]

    for case in test_cases:
        print('input:', 'array:', case)
        result = sl.max_area_2(case)
        print('output:', result)
