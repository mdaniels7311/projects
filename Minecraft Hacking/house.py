import mcpi.minecraft as minecraft, time, random
mc = minecraft.Minecraft.create()


pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

mc.setBlocks(x+1,y,z+1,x-4,y+4,z+5,45)
time.sleep(2)
mc.setBlocks(x+2,y,z+2,x-4,y+4,z+4,0)
