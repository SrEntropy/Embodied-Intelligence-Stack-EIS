class Agent:
    def __init__(self, env, pos = (1,1),):
        self.pos = pos
        self.env = env
        self.actions = {"N":(-1, 0), "S":(1, 0), "W":(0, -1),"E":(0, 1)}

    def move(self, action):
        dr, dc = self.actions[action] 
        
        new_r = self.pos[0] + dr 
        new_c = self.pos[1] + dc
        
        # 1. Check bounds 
        if not (0 <= new_r < self.env.rows and 0 <= new_c < self.env.columns): 
            print("Blocked: out of bounds") 
            return 
        # 2. Check if next cell is a wall 
        if self.env.maze[new_r][new_c] == 1: 
            print("Blocked: wall") 
            return
        # 3. Move 
        self.pos = [new_r, new_c] 
        print(f"Moved {action} to {self.pos}")