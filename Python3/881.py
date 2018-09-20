class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        n, people = len(people), sorted(people)
        #print(people)
        left, right, boats = 0, n - 1, 0
        while left <= right:
            boats += 1
            if people[left] + people[right] <= limit:
                #print(left, right)
                left += 1
                right -= 1
            else:
                #print(left, right)
                right -= 1
        return boats
