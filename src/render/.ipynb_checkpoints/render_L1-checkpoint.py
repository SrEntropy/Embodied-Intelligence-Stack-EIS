import pygame

class Display_World:
    def __init__(self, world, agent, cell_size=31):
        self.world = world
        self.agent = agent
        self.cell_size = cell_size

        pygame.init()
        self.screen = pygame.display.set_mode(
            (world.columns * cell_size, world.rows * cell_size)
        )
        pygame.display.set_caption("World Maze")
        self.clock = pygame.time.Clock()

    def start(self):
        running = True
        while running:
            self.clock.tick(60)

            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    running = False 
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_ESCAPE: 
                        running = False 
                    else:
                        self.control_agent(event)

            self.screen.fill((0, 0, 0))

            self.draw_world()
            self.draw_agent()

            pygame.display.flip()
        pygame.quit()

    def draw_world(self):
        for r in range(self.world.rows):
            for c in range(self.world.columns):
                color = (80, 145, 60) if self.world.maze[r][c] == 0 else (61, 37, 35)
                pygame.draw.rect(
                    self.screen,
                    color,
                    (c * self.cell_size, r * self.cell_size, self.cell_size, self.cell_size)
                )    

    def draw_agent(self):
        if self.agent.pos:
            ar, ac = self.agent.pos
            pygame.draw.rect(
                self.screen,
                (255, 0, 0),
                (ac * self.cell_size, ar * self.cell_size, self.cell_size, self.cell_size)
            )
    
    def control_agent(self, event):
        # event.type is already KEYDOWN here 
        if event.key == pygame.K_UP: self.agent.move("N") 
        elif event.key == pygame.K_DOWN: self.agent.move("S") 
        elif event.key == pygame.K_LEFT: self.agent.move("W") 
        elif event.key == pygame.K_RIGHT: self.agent.move("E")
