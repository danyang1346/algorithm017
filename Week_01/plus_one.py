#!/usr/bin/python3
# -*-coding:utf-8 -*-

'''
@Author  : Dan Yang
@Date    : 2020/10/30 10:08

'''

'''
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。

示例 2:
输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

链接：https://leetcode-cn.com/problems/plus-one
'''
class Solution(object):
    def plus_one(self, digits):
        # 解法一: 两边遍历，遍历一遍数组，转为数字，加1后，再遍历一遍对比是否一样，变化位置替换
        # 时间复杂度：O(2n)
        # 空间复杂度：O(1)

        # 解法二：1个指针，遍历一遍，从后往前遍历数组，如果加1大于等于10，
        # 则当前元素赋值为0，p--，判断--后位置，加1是否大于等于10
        # 时间复杂度: O(n)
        # 空间复杂度: O(1)
        if not digits:
            return []

        i = len(digits) - 1
        while i >= 0:
            if digits[i] + 1 >= 10:
                digits[i] = 0
                i -= 1
            else:
                digits[i] += 1
                return digits

        if i < 0:
            digits.insert(0, 1)

        return digits



if __name__ == '__main__':

    sl = Solution()

    test_cases = [[], [1,2,3], [4,3,2,1], [9], [9, 9, 9]]

    for case in test_cases:
        print('\ninput:', case)
        sl.plus_one(case)
        print(case)
        # sl.move_zeros_2(case)