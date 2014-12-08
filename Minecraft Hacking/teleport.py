### Basic Teleporter in MC Pi

import time, mcpi.minecraft as mc #imports time and mcpi module
game = mc.Minecraft.create() #connects to a minecraft game and calls it game

time.sleep(5.5)
game.postToChat("Hello! Welcome to Minecraft!")
time.sleep(3)
game.postToChat("Enjoy! :D")
time.sleep(5)

game.postToChat("And magic!")
game.player.setPos(69,69,69)
time.sleep(1)
game.postToChat("You have been teleported!")
time.sleep(2)
game.postToChat("Lets teleport you again...")
time.sleep(2)
game.player.setPos(-31,0,111)
game.postToChat("Kazaam!")
time.sleep(3)
game.postToChat("Lets do this one more time!")
time.sleep(1.5)
game.player.setPos(-140,22,112)
game.postToChat("I'm a wizard Harry...")
time.sleep(5)
game.player.setPos(77,10,133)

