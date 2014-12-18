import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()

while True:
        pos = mc.player.getPos() #gets the player co-ords
        x = pos.x
        y = pos.y
        z = pos.z

        Block = 0

        mc.setBlock(x,y-1,z,Block) #sets the block beneath the player to the value of 0 (air)
        time.sleep(0.2)

