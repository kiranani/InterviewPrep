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
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n, q = len(nums), collections.deque()
        if n == 0:
            return []
        for i in range(k - 1):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)

        ans = []
        for i in range(k - 1, n):
            if q and q[0] < i - k + 1:
                q.popleft()
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
            ans.append(nums[q[0]])
        return ans
        
