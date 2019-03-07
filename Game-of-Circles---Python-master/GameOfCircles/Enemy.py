from Sprite import Sprite
from Bullet import Bullet
from Player import Player

import SpriteManager

class Enemy(Sprite):
    
    speed = 10
    diameter = 50
    c = color(200)
    mark = 0
    wait = 1000
    go = True


    def move(self):
        self.y -= self.speed
        if self.y < 0 or self.y > width:
            self.speed *= -1
            
        vector = self.aim(SpriteManager.getPlayer())
        self.fire(vector)
            
    def aim(self, target):
        d = ((self.x - target.x)**2 + (self.y - target.y)**2)**.5
        xComp = target.x - self.x
        yComp = target.y - self.y
        xVec = xComp/2 * .1
        yVec = yComp/2 * .1
        return PVector(xVec, yVec)
    
    def fire(self, vector):
        if(millis() - self.mark > self.wait):
            self.go = not self.go
            self.mark = millis()
            
        if(self.go):
            self.go = False
            SpriteManager.spawn(Bullet(self.x, self.y, vector, self.team))
