import pygame, sys

# M.S MWELASE
# I have improved this code using sprites
# seach "pygame sprites" on youtube to learn more..

# CONSTANTS
FPS = 60
TITLE = 'Ping-Pong'
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 150
        
# Paddle class
class Paddle(pygame.sprite.Sprite):
    def __init__(self, group, color, size, pos):
        super().__init__()
        # add sprite group
        group.add(self)
        self.color = color
        self.size = size
        self.image = pygame.surface.Surface(size)
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center = pos)
        self.speed = 7
        self.y_vector = 0
        
    def boders(self):
        if self.rect.bottom >= WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT
        elif self.rect.top <= 0:
            self.rect.top = 0
            
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y_vector = -self.speed
        elif keys[pygame.K_DOWN]:
            self.y_vector = self.speed
            
    def update(self):
        self.boders()
        self.movement()
        self.rect.y += self.y_vector
        
class Opponent(pygame.sprite.Sprite):
    def __init__(self, group, color, size, pos):
        super().__init__()
        # add sprite group
        group.add(self)
        self.color = color
        self.size = size
        self.image = pygame.surface.Surface(size)
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center = pos)
        self.speed = 7
        self.y_vector = self.speed
        
    def borders_and_movement(self):
        if self.rect.bottom >= WINDOW_HEIGHT:
            self.y_vector = -self.speed
        elif self.rect.top <= 0:
            self.y_vector = self.speed
          
    def AI_following_ball(self):
        # print(Pong_Ball.rect.bottom)
        # if ball is on top
        if Pong_Ball.rect.bottom < self.rect.top:
            print(1)
            self.y_vector = -3
        # if ball is on bottom
        elif Pong_Ball.rect.top > self.rect.bottom:
            print(2)
            self.y_vector = 3
            
    
    def update(self):
        # self.borders_and_movement()
        self.AI_following_ball()
        self.rect.y += self.y_vector
        
class PongBall(pygame.sprite.Sprite):
    def __init__(self, group, pos, size, color):
        super().__init__()
        group.add(self)
        self.pos = pos
        self.color = color
        self.pos = pos
        self.pos_x, self.pos_y = self.pos
        self.size = size
        self.image = pygame.surface.Surface(self.size)
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center = pos)
        self.speed = 5
        self.vector_x = self.speed
        self.vector_y = self.speed
        
        
    def movement(self):
        self.rect.x += self.vector_x
        self.rect.y += self.vector_y
        self.pos = (self.pos_x, self.pos_y)
        
    def check_collisions(self):
        if pygame.sprite.spritecollide(self, Player_Paddle_Group, False):
            self.vector_x = -self.speed
        elif pygame.sprite.spritecollide(self, Opponent_Paddle_Group, False):
            self.vector_x = self.speed
            
    def boders(self): 
        if self.rect.left <= 0: # left
            self.vector_x = self.speed
        elif self.rect.right >= WINDOW_WIDTH: # right
            self.vector_x = -self.speed
        elif self.rect.top <= 0: # top
            self.vector_y = self.speed
        elif self.rect.bottom >= WINDOW_HEIGHT: # bottom
            self.vector_y = -self.speed
     
    def update(self):
        self.movement()
        self.check_collisions()
        self.boders()
    
# sprite groups
Player_Paddle_Group = pygame.sprite.Group()
Opponent_Paddle_Group = pygame.sprite.Group()
PongBall_Group = pygame.sprite.Group()

Opponent_Paddle = Opponent(Opponent_Paddle_Group, " white", (20, 150), (30, WINDOW_HEIGHT//2))
Player_Paddle = Paddle(Player_Paddle_Group, "white", (20, 150), (WINDOW_WIDTH-30, WINDOW_HEIGHT//2))
Pong_Ball = PongBall(PongBall_Group, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), (30, 30), "blue")

class Game:
    def __init__(self):
        
        # COLOURS
        self.BLACK = pygame.Color(0, 0, 0)
        self.WHITE = pygame.Color(255, 255, 255)
        self.GREEN = pygame.Color(0, 255, 0)
        
        self.Clock = pygame.time.Clock()
		
		# Display
        self.DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(TITLE)
	    
		# Background
        self.BACKGROUND = pygame.surface.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.BACKGROUND.fill(self.BLACK)
	
        self.RUNNING = True
        
    def _Run(self):
        while self.RUNNING:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.DISPLAY.blit(self.BACKGROUND, (0, 0))
            

			# display sprites
            PongBall_Group.draw(self.DISPLAY)
            PongBall_Group.update()
            Player_Paddle_Group.draw(self.DISPLAY)
            Player_Paddle_Group.update()
            Opponent_Paddle_Group.draw(self.DISPLAY)
            Opponent_Paddle_Group.update()
            
            
            
            pygame.display.update()
            self.Clock.tick(FPS)
			

Pong = Game()

if __name__ == '__main__':
	Pong._Run()
