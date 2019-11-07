class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dig, let = [], []
        for line in logs:
            tokens = line.split(maxsplit=1)
            if tokens[1][0].isalpha():
                let.append([tokens, line])
            else:
                dig.append(line)
        let.sort(key=lambda x: (x[0][1], x[0][0]))
        return [x[1] for x in let] + dig
        
