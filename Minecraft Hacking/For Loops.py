import mcpi.minecraft as minecraft, time
mc = minecraft.Minecraft.create()

for location in (2,4,6,8,10):
	mc.setBlock(location,0,0,41)
time.sleep(2)
for height in (-1,15,12,40,65):
	mc.setBlock(10,location,10,41)
time.sleep(2)
for step in (0,1,2,3,4,5,6,7,8,9,10):
	mc.setBlock(20,step,step,22)
time.sleep(2)
