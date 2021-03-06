import platform
from Bullet import Bullet
from Enemy import Enemy
from Player import Player
from raindrop import Raindrop
from SpriteManager import sprites
from ScreenSaverBot import ScreenSaverBot
from JiggleBot import JiggleBot
import SpriteManager

def setup():
    print "Built with Processing Python version " + platform.python_version()
    
    global player, sprites
    size(500, 500)
    playerTeam = 1
    player = Player(width/2, height/2, playerTeam);
    enemyTeam = 2
    
    SpriteManager.setPlayer(player)
    SpriteManager.spawn(JiggleBot(200, 0, 0))
    SpriteManager.spawn(Enemy(100, 100, enemyTeam))
    SpriteManager.spawn(Raindrop(250, 100, enemyTeam))
    SpriteManager.spawn(Raindrop(20, 100, enemyTeam))
    SpriteManager.spawn(Raindrop(random(0, width), 125, enemyTeam))
    SpriteManager.spawn(ScreenSaverBot(20, 300, enemyTeam))
    SpriteManager.spawn(JiggleBot(height - 25, width/2, enemyTeam))
                           
def draw():
    global player, sprites
    background(255)    
    SpriteManager.animate()
        
def keyPressed():
    SpriteManager.player.keyDown()
        
def keyReleased():
    SpriteManager.player.keyUp()
