from Sprite import Sprite

class JiggleBot(Sprite):
    
    speed = 5
    diameter = 50
    c = color(200)
    
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        
    def move(self):
        self.y += random(-self.speed, self.speed)
        self.x += random(-self.speed, self.speed)
        self.y = constrain(self.y, 0, height)
        self.x = constrain(self.x, 0, width)
        
    def display(self):
        fill(self.c)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
    def animate(self):
        self.move()
        self.display()
