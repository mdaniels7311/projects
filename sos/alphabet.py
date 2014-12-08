import RPi.GPIO as GP,time
GP.setmode(GP.BOARD)
GP.setup(11,GP.OUT)

#defining the function 'dot'
def dot():
    GP.output(11,GP.HIGH)
    time.sleep(0.25)
    GP.output(11,GP.LOW)
    time.sleep(0.5)

#defining the function 'dash'
def dash():
    GP.output(11,GP.HIGH)
    time.sleep(1)
    GP.output(11,GP.LOW)
    time.sleep(0.5)

def morse(name):
    if name == "a":
        print ("a")
        dot()
        dash()
    elif name == "b":
        print ("b")
        dash()
        dot()
        dot()
        dot()
    elif name == "c":
        print ("c")
        dash()
        dot()
        dash()
        dot()
    elif name == "d":
        print ("d")
        dash()
        dot()
        dot()
    elif name == "e":
        print ("e")
        dot()
    elif name == "h":
        print ("h")
        dot()
        dot()
        dot()
        dot()
    elif name == "i":
        print ("i")
        dot()
        dot()
    elif name == "j":
        print ("j")
        dot()
        dash()
        dash()
        dash()
    elif name == "k":
        print ("k")
        dash()
        dot()
        dash()
    elif name == "l":
        print ("l")
        dot()
        dash()
        dot()
        dot()
    elif name == "m":
        print ("m")
        dash()
        dash()
    elif name == "n":
        print ("n")
        dash()
        dot()
    elif name == "o":
        print ("o")
        dash()
        dash()
        dash()
    elif name == "p":
        print ("p")
        dot()
        dash()
        dash()
        dot()
    elif name == "q":
        print ("q")
        dash()
        dash()
        dot()
        dash()
    elif name == "r":
        print ("r")
        dot()
        dash()
        dot()
    elif name == "s":
        print ("s")
        dot()
        dot()
        dot()
    elif name == "t":
        print ("t")
        dash()
    elif name == "u":
        print ("u")
        dot()
        dot()
        dash()
    elif name == "v":
        print ("v")
        dot()
        dot()
        dot()
        dash()
    elif name == "w":
        print ("w")
        dot()
        dash()
        dash()
    elif name == "x":
        print ("x")
        dash()
        dot()
        dot()
        dash()
    elif name == "y":
        print ("y")
        dash()
        dot()
        dash()
        dash()
    elif name == "z":
        print ("z")
        dash()
        dash()
        dot()
        dot()
    elif name == "0":
        print ("0")
        dash()
        dash()
        dash()
        dash()
        dash()
    elif name == "1":
        print ("1")
        dot()
        dash()
        dash()
        dash()
        dash()
    elif name == "2":
        print ("2")
        dot()
        dot()
        dash()
        dash()
        dash()
    elif name == "3":
        print ("3")
        dot()
        dot()
        dot()
        dash()
        dash()
             
             
            

name = input("Please enter a letter or number between 0 to 3: ")
morse(name)
