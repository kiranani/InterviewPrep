class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def operate(opStack, numStack):
            n2, n1, op = numStack.pop(), numStack.pop(), opStack.pop()
            if op == "+":
                numStack.append(n1 + n2)
            elif op == "-":
                numStack.append(n1 - n2)
        i, n, opers = 0, len(s), set(["+", "-", "*", "/"])
        opStack, numStack = [], []
        while i < n:
            if s[i] in opers:
                if len(opStack) > 0:
                    if s[i] in ["+", "-"]:
                        if opStack[-1] in ["+", "-"]:
                            operate(opStack, numStack)
                opStack.append(s[i])
            elif s[i].isdigit():
                j = i + 1
                while j < n and s[j].isdigit():
                    j += 1
                n2 = int(s[i:j])
                if not opStack:
                    numStack.append(n2)
                elif opStack[-1] == "*":
                    opStack.pop()
                    numStack.append(numStack.pop() * n2)
                elif opStack[-1] == "/":
                    opStack.pop()
                    numStack.append(numStack.pop() // n2)
                else:
                    numStack.append(n2)
                i = j - 1
            i += 1

        print(opStack, numStack)
        while opStack:
            operate(opStack, numStack)
        return numStack[0]
