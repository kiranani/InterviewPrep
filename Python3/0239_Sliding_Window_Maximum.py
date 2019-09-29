class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n, h = len(nums), []
        if n == 0:
            return []
        for i in range(k - 1):
            heapq.heappush(h, (-nums[i], i))
        ans = []
        for i in range(k - 1, n):
            heapq.heappush(h, (-nums[i], i))
            #print("Before:", h)
            while h[0][1] < i - k + 1:
                heapq.heappop(h)
            #print(h)
            ans.append(-h[0][0])
        return ans
        
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if not n or k == 1:
            return nums
        
        def update_q(i):
            if q and q[0] == i - k:
                q.popleft()
            while q and nums[q[-1]] < nums[i]:
                q.pop()
        q = collections.deque()
        for i in range(k - 1):
            update_q(i)
            q.append(i)
        ans = [None] * (n - k + 1)
        for i in range(k - 1, n):
            update_q(i)
            q.append(i)
            ans[i - k + 1] = nums[q[0]]
        return ans
        
        
