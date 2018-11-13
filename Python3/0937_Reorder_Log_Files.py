class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digitLogs = []
        wordLogs = []
        for log in logs:
            words = log.strip().split()
            if words[1].isdigit():
                digitLogs.append(log)
            else:
                wordLogs.append((words[1:], log))
        wordLogs.sort(key=lambda x: x[0])
        ans = [x[1] for x in wordLogs]
        ans.extend(digitLogs)
        return ans
        
