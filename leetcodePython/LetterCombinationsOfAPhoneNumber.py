'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

图片地址: https://assets.leetcode-cn.com/aliyun-lc-upload/original_images/17_telephone_keypad.png

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    # 深度优先遍历DFS
    def letterCombinations(self, digits: str) -> [str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']
                 }
        res = []
        def backtrack(combination,next_digits):
            if len(next_digits) == 0:
                res.append(combination)
            else:
                for letter in phone[next_digits[0]]:
                    backtrack(combination + letter,next_digits[1:])

        if digits:
            backtrack("",digits)
        return res