import random 



class Hunt():

  def welcome(self):
    print("You will be going hunting")
    print("Your goal is to guess the right number")
    print("Each time you guess, you fire a bullet!")
    print("Here we go!")
    input("Hit enter to continue!")

  def hunting(self, wagon):
    targetNumber = random.randint(1,20)
    guess = int(input("Please guess a number between 1 and 20: "))
    while guess != targetNumber:
      if guess > targetNumber:
        print("You missed, shot to high!")
        wagon.bullets -= 1
      elif guess < targetNumber:
        print("You missed, shot to low!")
        wagon.bullets -= 1
      guess = int(input("Please guess a number between 1 and 20: "))
    print("You guessed the number!")
    wagon.bullets -= 1
    if targetNumber > 18:
      print("You killed a bison!")
      print("Food increased by 50!")
      wagon.food += 50 
      input("Hit enter to continue!")
    elif targetNumber >= 15 and targetNumber < 18:
      print("You killed a deer")
      print("Food increased by 25!")
      wagon.food += 25 
      input("Hit enter to continue!")
    elif targetNumber >= 6 and targetNumber < 15:
      print("You killed a rabbit")
      print("Food increased by 15!")
      wagon.food += 15
      input("Hit enter to continue!")
    elif targetNumber >= 0 and targetNumber < 6:
      print("You killed a chipmunk")
      print("Food increased by 3!")
      wagon.food += 3
      input("Hit enter to continue!")


# hunt = Hunt()
# hunt.hunting(wagon)