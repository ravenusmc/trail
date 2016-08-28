#Validations for the main file. 
def mainValid(choice):
  if choice == 1 or choice == 2 or choice == 3:
    return True
  else:
    return False 

def characterValid(choice):
  if choice == 1 or choice == 2 or choice == 3 or choice == 4:
    return True 
  else: 
    return False

def monthValid(choice):
  if choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5:
    return True 
  else: 
    return False 

## Validations for the store file. 
def storemainValid(choice):
  if choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5:
    return True
  else: 
    return False 

def oxenValid(yokeNumber):
  if yokeNumber < 0 or yokeNumber > 5:
    return False
  else:
    return True

def foodValid(foodNumber):
  if foodNumber < 0:
    return False
  else:
    return True

def clothValid(clothNumber):
  if clothNumber < 0:
    return False
  else: 
    return True 

def wheelValid(wheel):
  if wheel < 0:
    return False 
  else: 
    return True 

def axleValid(axle):
  if axle < 0:
    return False
  else: 
    return True

def tongueValid(tongue):
  if tongue < 0:
    return False
  else: 
    return True

## Validations for the trail file.

def trailMenuValid(choice):
  if choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5 or choice == 6:
    return True
  else:
    return False 

def increaseValid(speedUp, yoke):
  if speedUp > yoke:
    return False
  else: 
    return True






























  