class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s, h, k = 0, {0: -1}, abs(k)
        for i, num in enumerate(nums):
            s += num
            if k > 0:
                s %= k
            if s in h:
                if i - h[s] > 1:
                    return True
            else:
                h[s] = i
        return False
            
        
