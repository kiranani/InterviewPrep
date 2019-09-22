class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.food = food
        self.fi = 0
        self.q = collections.deque([(0, 0)])
        self.d = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
        self.m, self.n = height, width
        

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        x, y = self.q[-1][0] + self.d[direction][0], self.q[-1][1] + self.d[direction][1]
        if x < 0 or x >= self.m or y < 0 or y >= self.n:
            return -1
        elif self.fi < len(self.food) and [x, y] == self.food[self.fi]:
            self.fi += 1
        else:
            self.q.popleft()
        if (x, y) in self.q:
            return -1
        self.q.append((x, y))
        return len(self.q) - 1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
