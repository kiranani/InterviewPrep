class ExamRoom:

    def __init__(self, N: int):
        self.n = N
        self.students = []
        

    def seat(self) -> int:
        if not self.students:
            self.students.append(0)
            return 0
        else:
            d, s = self.students[0], 0
            for i, stu in enumerate(self.students[1:]):
                cd = (stu - self.students[i]) // 2
                if cd > d:
                    d, s = cd, self.students[i] + cd
            if self.n - 1 - self.students[-1] > d:
                s = self.n - 1
            bisect.insort(self.students, s)
            return s
        

    def leave(self, p: int) -> None:
        self.students.remove(p)
        


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
