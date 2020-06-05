'''
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
'''
#solution
class Solution:

    def __init__(self, w: List[int]):
        self.w_cum = []
        self.sum =0
        for i in w:
            self.sum += i
            self.w_cum.append(self.sum)

    def pickIndex(self) -> int:
        idx = random.randint(1, self.sum)
        return self.binarySearch(idx)
    
    def binarySearch(self, val):
        l = 0 
        r = len(self.w_cum) -1
        while l < r:
            mid = (int)(l + (r-l)/2)
            if self.w_cum[mid] < val:
                l = mid + 1
            else:
                r = mid 
        return l
