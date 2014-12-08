#<-- This is a hastag #Swag
import mcpi.minecraft as minecraft, time, random
mc = minecraft.Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

def m(x,y,z):
    mc.setBlocks(x,y,z,x,y+6,z,42)
    mc.setBlocks(x+4,y,z,x+4,y+6,z,42)
    mc.setBlocks(x+2,y+3,z,x+2,y+4,z,42)
    mc.setBlock(x+1,y+5,z,42)
    mc.setBlock(x+3,y+5,z,42)

m(0,0,0)
