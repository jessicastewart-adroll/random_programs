'''
http://arunrocks.com/mars-rover-in-python-and-haskell/
'''

class Plateau(object):
    def __init__(self, bounds):
        self.bounds = bounds
        self.rovers = []

    def add_rover(self, position):
        self.rovers.append(MarsRover(position))

    def move_rover(self, instructions):
        return self.rovers.pop().process_instructions(instructions)

class MarsRover(object):
    DIRECTION_CARDINAL = "NESW"
    DIRECTION_MOVEMENT = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def __init__(self, position):
        x, y, direction = position.split()
        self.x = int(x)
        self.y = int(y)
        self.direction = MarsRover.DIRECTION_CARDINAL.find(direction)

    def process_instructions(self, instructions):
        for instr in instructions:
            if instr == "M":
                self.move()
            else:
                self.change_direction(instr)

        return self.x, self.y, MarsRover.DIRECTION_CARDINAL[self.direction]

    def change_direction(self, direction_change):
        if self.direction == 0 and direction_change == "L":
            self.direction = 3
        elif self.direction == 3 and direction_change == "R":
            self.direction = 0
        elif direction_change == "L":
            self.direction -= 1
        else:
            self.direction += 1

    def move(self):
        x, y = MarsRover.DIRECTION_MOVEMENT[self.direction]
        self.x += x
        self.y += y

# p = Plateau([5, 5])
# p.add_rover("1 2 N")
# p.move_rover("LMLMLMLMM")
# p.add_rover("3 3 E")
# p.move_rover("MMRMMRMRRM")

# Test Input:
# 5 5
# 1 2 N
# LMLMLMLMM
# 3 3 E
# MMRMMRMRRM
# Expected Output:
# 1 3 N
# 5 1 E
