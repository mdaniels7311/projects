import mcpi.minecraft as minecraft, time
mc = minecraft.Minecraft.create()

#move player to origin
mc.player.setPos(0.4,6,0.4)

b = 7
r = 14
o = 1
g = 5

while True:
	time.sleep(2)

	mc.setBlock(0,0,0,35,b)
	mc.setBlock(0,1,0,35,b)
	mc.setBlock(0,2,0,35,b)
	mc.setBlock(0,3,0,35,b)
	mc.setBlock(0,4,0,35,b)
	mc.setBlock(0,5,0,35,r)

	time.sleep(3)

	mc.setBlock(0,0,0,35,b)
	mc.setBlock(0,1,0,35,b)
	mc.setBlock(0,2,0,35,b)
	mc.setBlock(0,3,0,35,b)
	mc.setBlock(0,4,0,35,o)
	mc.setBlock(0,5,0,35,r)

	time.sleep(5)

	mc.setBlock(0,0,0,35,b)
	mc.setBlock(0,1,0,35,b)
	mc.setBlock(0,2,0,35,b)
	mc.setBlock(0,3,0,35,g)
	mc.setBlock(0,4,0,35,b)
	mc.setBlock(0,5,0,35,b)

	time.sleep(8)

	mc.setBlock(0,0,0,35,b)
	mc.setBlock(0,1,0,35,b)
	mc.setBlock(0,2,0,35,b)
	mc.setBlock(0,3,0,35,b)
	mc.setBlock(0,4,0,35,o)
	mc.setBlock(0,5,0,35,b)

	time.sleep(2)

	mc.setBlock(0,0,0,35,b)
	mc.setBlock(0,1,0,35,b)
	mc.setBlock(0,2,0,35,b)
	mc.setBlock(0,3,0,35,b)
	mc.setBlock(0,4,0,35,b)
	mc.setBlock(0,5,0,35,r)

	time.sleep(5)


