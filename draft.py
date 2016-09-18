
def main():
  print("1. Test")
  print("2. Second Test")
  choice = int(input("Testing: "))
  while not valid(choice):
    print("Incorrect Selection!")
    choice = int(input("Testing: "))
  if choice == 1:
    print("Yay!")
  elif choice == 2:
    print("Nay!")

def valid(choice):
  if choice == 1 or choice == 2:
    return True 
  else:
    return False

main()
