class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        inds, a = [None] * 26, ord("a")
        for i, l in enumerate(S):
            ind = ord(l) - a
            if inds[ind]:
                inds[ind][1] = i
            else:
                inds[ind] = [i, i]
        points = []
        for ind in inds:
            if ind:
                points.append((ind[0], 0))
                points.append((ind[1], 1))
        points.sort(key=lambda x: (x[0], x[1]))
        ans = []
        stack = [points[0][0]]
        for point in points[1:]:
            if point[1]:
                prev = stack.pop()
                if not stack:
                    ans.append(point[0] - prev + 1)
            else:
                stack.append(point[0])
        return ans
        
