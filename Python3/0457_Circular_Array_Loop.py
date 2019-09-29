class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        def getI(i):
            return (i + nums[i]) % n
        for i in range(n):
            if nums[i]:
                c, j, k = 0, i, getI(i)
                while nums[i] * nums[k] > 0 and nums[getI(k)] * nums[i] > 0:
                    if j == k:
                        if nums[j] % n == 0:
                            break
                        return True
                    j, k = getI(j), getI(getI(k))
                j, v = i, nums[i]
                while nums[j] * v > 0:
                    nums[j], j = 0, getI(j)
                nums[i] = 0
        return False
        
