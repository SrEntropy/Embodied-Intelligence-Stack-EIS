import numpy as np
import random

import random
import numpy as np

class Maze_World:

    def __init__(self, name="Maze", width=21, height=21, seed=43):
        self.name = name
        self.rgn = random.Random(seed)
        self.rows = height
        self.columns = width

        # 1 = wall, 0 = passage
        self.maze = [[1 for _ in range(self.columns)] for _ in range(self.rows)]

    def generate_maze(self, x, y):
        # Mark current cell as passage
        self.maze[y][x] = 0

        # Directions: jump 2 cells
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        self.rgn.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Check bounds and if neighbor is still a wall
            if 0 <= nx < self.columns and 0 <= ny < self.rows and self.maze[ny][nx] == 1:

                # Carve the wall between
                self.maze[y + dy // 2][x + dx // 2] = 0

                # Recurse
                self.generate_maze(nx, ny)
