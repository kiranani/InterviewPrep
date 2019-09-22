class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        i, n, splits = 0, len(nums), collections.deque()
        while i < n:
            c, num = 0, nums[i]
            while i + c < n and nums[i + c] == num:
                c += 1
            i += c
            while len(splits) - c > 0:
                split = splits.popleft()
                if split[1] < 3:
                    return False
            while splits and num - splits[0][0] > 1:
                if splits.popleft()[1] < 3:
                    return False
            for split in splits:
                split[0], split[1] = num, split[1] + 1
            for _ in range(c - len(splits)):
                splits.append([num, 1])
        return all(x[1] > 2 for x in splits)
        
        
   
