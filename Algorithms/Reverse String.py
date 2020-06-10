'''
example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''
#solution
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left =0
        right = len(s) -1
        while left < right:
            tmp = s[left]
            s[left] = s [right]
            left += 1
            s[right] = tmp
            right -= 1
        #s[left], s[right] = s[right], s[left]
