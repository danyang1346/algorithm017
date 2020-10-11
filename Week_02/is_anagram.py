#!/usr/bin/python3
# -*-coding:utf-8 -*-

'''
@Author  : Dan Yang
@Date    : 2020/10/11 17:27

'''

'''
242. 有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:
输入: s = "anagram", t = "nagaram"
输出: true

示例 2:
输入: s = "rat", t = "car"
输出: false

说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
链接：https://leetcode-cn.com/problems/valid-anagram
'''


class Solution(object):
    '''
    解法罗列：
    方法1: 排序 + 比较
          时间复杂度：O(nlogn)
          空间复杂度：O(1)

    方法2：空间换时间, 1个dict 先保存s结果，遍历t，对应减；遍历dict,判断是否有非0值
    方法3：空间换时间， 两个dict，分别保存s和t的结果，最终判断是否相等
    方法4: 空间换时间, 两个数组（共26个字母，分别对应一位），分别保存s和t的结果，最终判断是否相等
    方法5: 空间换时间，1个数组，保存s的结果，遍历t，对应减；遍历数组,判断是否有非0值
    时间复杂度：O(n)
    空间复杂度：O(1) 固定大小
    '''

    def is_anagram1(self, s, t):

        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)


    def is_anagram2(self, s, t):

        if len(s) != len(t):
            return False

        count_dict = {}
        for i in s:
            count_dict[i] = count_dict.get(i, 0) + 1

        for j in t:
            if j not in count_dict:
                return False
            else:
                count_dict[j] -= 1

        for value in count_dict.values():
            if value != 0:
                return False

        return True


    def is_anagram3(self, s, t):

        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}

        for i in s:
            count_s[i] = count_s.get(i, 0) + 1

        for j in t:
            count_t[j] = count_t.get(j, 0) + 1

        return count_s == count_t


    def is_anagram4(self, s, t):

        if len(s) != len(t):
            return False

        count_s, count_t = [0]*26, [0]*26
        for i in s:
            count_s[ord(i) - ord('a')] += 1

        for j in t:
            count_t[ord(j) - ord('a')] += 1

        return count_s == count_t


    def is_anagram5(self, s, t):

        if len(s) != len(t):
            return False

        count = [0]*26
        for i in s:
            count[ord(i) - ord('a')] += 1

        for j in t:
            count[ord(j) - ord('a')] -= 1

        for value in count:
            if value != 0:
                return False

        return True


if __name__ == '__main__':
    sl = Solution()
    test_cases = [['rat', 'car'], ['anagram', 'nagaram'], ['aa', 'a']]

    for case in test_cases:
        print('\n\ninput:', '\ns:', case[0], '\nt:', case[1])
        result = sl.is_anagram1(case[0], case[1])
        print('output:', result)
    pass