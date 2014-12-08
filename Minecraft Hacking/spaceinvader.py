import mcpi.minecraft as minecraft, time
mc = minecraft.Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

block = 1
lava = 11
water = 9

while True:
	mc.setBlocks(x+3,y,z+3,x+15,y,z+12,block)
	mc.setBlocks(x+4,y,z+5,x+4,y,z+7,lava)
	mc.setBlocks(x+5,y,z+7,x+5,y,z+8,lava)
	mc.setBlocks(x+6,y,z+5,x+6,y,z+9,lava)
	mc.setBlocks(x+7,y,z+4,x+8,y,z+4,lava)
	mc.setBlocks(x+10,y,z+4,x+11,y,z+4,lava)
	mc.setBlocks(x+7,y,z+6,x+7,y,z+7,lava)
	mc.setBlocks(x+7,y,z+9,x+7,y,z+10,lava)
	mc.setBlock(x+6,y,z+11,lava)
	mc.setBlock(x+12,y,z+11,lava)
	mc.setBlocks(x+8,y,z+6,x+10,y,z+9,lava)
	mc.setBlocks(x+11,y,z+6,x+11,y,z+7,lava)
	mc.setBlocks(x+11,y,z+9,x+11,y,z+10,lava)
	mc.setBlocks(x+12,y,z+5,x+12,y,z+9,lava)
	mc.setBlocks(x+13,y,z+7,x+13,y,z+8,lava)
	mc.setBlocks(x+14,y,z+5,x+14,y,z+7,lava)
	mc.setBlocks(x+3,y-1,z+3,x+15,y-1,z+12,block)

	time.sleep(3)

	mc.setBlocks(x+4,y,z+5,x+4,y,z+7,water)
	mc.setBlocks(x+5,y,z+7,x+5,y,z+8,water)
	mc.setBlocks(x+6,y,z+5,x+6,y,z+9,water)
	mc.setBlocks(x+7,y,z+4,x+8,y,z+4,water)
	mc.setBlocks(x+10,y,z+4,x+11,y,z+4,water)
	mc.setBlocks(x+7,y,z+6,x+7,y,z+7,water)
	mc.setBlocks(x+7,y,z+9,x+7,y,z+10,water)
	mc.setBlock(x+6,y,z+11,water)
	mc.setBlock(x+12,y,z+11,water)
	mc.setBlocks(x+8,y,z+6,x+10,y,z+9,water)
	mc.setBlocks(x+11,y,z+6,x+11,y,z+7,water)
	mc.setBlocks(x+11,y,z+9,x+11,y,z+10,water)
	mc.setBlocks(x+12,y,z+5,x+12,y,z+9,water)
	mc.setBlocks(x+13,y,z+7,x+13,y,z+8,water)
	mc.setBlocks(x+14,y,z+5,x+14,y,z+7,water)

	time.sleep(3)
