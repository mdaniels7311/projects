#this file contains all the functions for Guess Who. DO NOT DELETE!
import picamera, time, json

#gets picture of user
def getUserImage(name):
    try: #try and except basically tries to do the code un the try indentation and if it fails and comes out with the error shown after the except, it will run the except indentation
        check=False
        while check == False:
            with picamera.PiCamera() as cam:
                cam.resolution = (1024,768)
                cam.start_preview()
                time.sleep(5)
                cam.stop_preview()
                time.sleep(2)
                filename = '{0}.jpeg'.format(name)
                cam.capture(filename)
                
                correct = input("Are you happy with this picture? ")
                if correct.lower()=="yes":
                    check=True
    except picamera.exc.PiCameraMMALError:
        print("Camera not detected. Connect the camera to the slot behind the Ethernet port and restart the Raspberry Pi.")
        filename=""
    except picamera.exc.PiCameraRuntimeError:
        print("bang")
        
    return filename


#gets user details
def getCharProfile():
    name = input("What is your name? ")
    filename = getUserImage(name) #Runs the getUserImage function and saves its data as filename
    check=False
    while check == False:
        hair_colour = input("What is your hair colour? ")
        if hair_colour.lower()=="brown" or hair_colour.lower()=="black" or hair_colour.lower()=="blonde" or hair_colour.lower()=="ginger" or hair_colour.lower()=="." or hair_colour.lower()=="purple" or hair_colour.lower()=="grey":
            check=True
    check=False
    while check == False:
        eye_colour = input("What is your eye colour? ")
        if eye_colour.lower()=="green" or eye_colour.lower()=="blue" or eye_colour.lower()=="brown" or eye_colour.lower()==".":
            check=True
    check=False
    while check == False:
        glasses = input("Are you wearing glasses? ")
        if glasses.lower()=="yes" or glasses.lower()=="no" or glasses.lower()==".":
            check=True
    check=False
    while check == False:
        hat = input("Are you wearing a hat? ")
        if hat.lower()=="yes" or hat.lower()=="no" or hat.lower()==".":
            check=True
    check=False
    while check == False:
        gender = input("What is your gender? ")
        if gender.lower()=="male" or gender.lower()=="female" or gender.lower()==".":
            check=True
    check=False
    while check == False:
        facial_hair = input("Do you have any facial hair? ")
        if facial_hair.lower()=="yes" or facial_hair.lower()=="no" or facial_hair.lower()==".":
            check=True
    check=False
    while check == False:
        facial_features = input("Do you have any facial features, such as freckles? ")
        if facial_features.lower()=="yes" or facial_features.lower()=="no" or facial_features.lower()==".":
            check=True

    return [name, hair_colour, eye_colour, glasses, hat, gender, facial_hair, facial_features]    #return prints the data entered in the variables in the square brackets
    

#loading and storing the data
def loadData():
    print("Loading...")
    try:
        with open ("people.txt",mode='r') as file:
            people = json.load(file)
    except IOError:
        print("Error detected")
        people = []
    return people

        
def store():
    person = getCharProfile()
    people.append(person)
    print(people)
    with open ("people.txt",mode='w') as chars:
        json.dump(people,chars)

print("Running...")

people = loadData()

while len(people)<24: #if the length of the list is shorter than 24, it will keep running store()
    store()


