import mcpi.minecraft as minecraft, time, random
mc = minecraft.Minecraft.create()

mc.setBlocks(-30,-5,-30,30,30,30,0) #clear area

#places colourful wool blocks
for b in range(14,0,-1):
	mc.postToChat(-1)
	mc.setBlock(-3,b,0,35,b)
	time.sleep(2)
