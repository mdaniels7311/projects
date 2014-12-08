import mcpi.minecraft as minecraft, time, random
mc = minecraft.Minecraft.create()

def house(x,y,z):
	mc.setBlocks(x+1,y,z+1,x-4,y+4,z+5,45)
	time.sleep(2)
	mc.setBlocks(x,y,z+2,x-3,y+4,z+4,0)
		
house(20,0,20)
house(30,0,20)
house(40,0,20)
