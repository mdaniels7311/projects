import time, mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

while True:
    time.sleep(3)
    mc.postToChat("Teleportation in 3...")
    time.sleep(1)
    mc.postToChat("2...")
    time.sleep(1)
    mc.postToChat("1...")
    time.sleep(1)
    mc.postToChat("Teleporting to 69, 69, 69...")
    mc.player.setPos(69, 69, 69)
    time.sleep(2)
    mc.postToChat("Teleporting testing complete! Test 2 initiating...")
    time.sleep(5)
    mc.player.setPos(100,100,100)
    mc.postToChat("Loop starting...")
    time.sleep(5)
