from Sprite import Sprite

class Raindrop(Sprite):
    
    speed = 10
    diameter = 25
    c = color(200)
    
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        
    def move(self):
        self.y += self.speed
        if self.y < 0:
            self.speed *= -1
            
        if self.y > height:
            self.y = 0
        
    def display(self):
        fill(self.c)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
    def animate(self):
        self.move()
        self.display()
