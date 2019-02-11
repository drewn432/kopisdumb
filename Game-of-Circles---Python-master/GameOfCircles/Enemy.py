class Enemy:
    
    speed = 8
    diameter = 50
    c = color(0,0,255)
    
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        
    def move(self):
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1
        
    def display(self):
        fill(self.c)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
    def animate(self):
        self.move()
        self.display()
