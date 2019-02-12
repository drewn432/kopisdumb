import platform
from Bullet import Bullet
from Enemy import Enemy
from Player import Player
from SpriteManager import sprites
from raindrop import raindrop
from ScreenSaverBot import ScreenSaverBot
from JiggleBot import JiggleBot

def setup():
    print "Built with Processing Python version " + platform.python_version()
    
    global player, sprites
    size(500, 500)
    playerTeam = 1
    enemyTeam = 2
    player = Player(width/2, height/2, playerTeam)
    
    sprites.append(player)
    sprites.append(Enemy(50, 50, enemyTeam))
    sprites.append(Enemy(150, 150, enemyTeam))
    sprites.append(raindrop(150, 150, enemyTeam))
    sprites.append(raindrop(100, 150, enemyTeam))
    sprites.append(raindrop(50, 150, enemyTeam))
    sprites.append(raindrop(200, 150, enemyTeam))
    sprites.append(raindrop(375, 150, enemyTeam))
    sprites.append(raindrop(300, 150, enemyTeam))
    sprites.append(raindrop(350, 150, enemyTeam))
    sprites.append(raindrop(400, 150, enemyTeam))
    sprites.append(raindrop(450, 150, enemyTeam))
    sprites.append(ScreenSaverBot(450, 150, enemyTeam))
    sprites.append(JiggleBot(450, 150, enemyTeam))
    
                           
def draw():
    global player, sprites
    background(255)    

    for sprite in sprites:
        sprite.animate()
        
    checkCollisions()
    
def checkCollisions():
    global sprites
    for a in sprites:
        for b in sprites:
            if a.team != b.team:
                d = (pow(a.x - b.x, 2) + pow(a.y - b.y, 2))**(0.5)
                r1 = a.diameter / 2
                r2 = b.diameter / 2
                if(r1 + r2 > d):
                    sprites.remove(a)
                    sprites.remove(b)
    
def keyPressed():
    global player
    player.keyDown()    
        
def keyReleased():
    global player
    player.keyUp()
