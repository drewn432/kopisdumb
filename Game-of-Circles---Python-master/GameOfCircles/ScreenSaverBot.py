from Sprite import Sprite

class ScreenSaverBot(Sprite):
    
    xspeed = 10
    yspeed = 5
    diameter = 40
    c = color(200)
    
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        
    def move(self):
        self.y += self.yspeed
        self.x += self.xspeed
        if self.y < 0:
            self.yspeed *= -1
        if self.y > height:
            self.yspeed *= -1
        if self.x > width:
            self.xspeed *= -1
        if self.x < 0:
            self.xspeed *= -1
            
    def display(self):
        fill(self.c)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
    def animate(self):
        self.move()
        self.display()
