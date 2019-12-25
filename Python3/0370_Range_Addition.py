class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        arr = [0] * (length + 1)
        for i, j, s in updates:
            arr[i] += s
            arr[j + 1] -= s
        s = 0
        for i in range(length):
            s += arr[i]
            arr[i] = s
        arr.pop()
        return arr
        
