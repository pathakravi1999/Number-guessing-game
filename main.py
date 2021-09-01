import random
easy_level_attempt= 10
hard_level_attempt = 5



def compare(number,guess,attempt):
  if guess>number:
    print("Too high")
    return attempt-1
  elif guess<number:
    print("Too low")
    return attempt-1
  elif guess== number:
    print(f"You got it! The answer was {number}")
 

def difficulty():
  choose_difficulty = input("Choose a difficulty type easy or hard ").lower()

  if choose_difficulty == "easy":
    return easy_level_attempt
  elif choose_difficulty == "hard":
    return hard_level_attempt
  
 
def game():
  print("Welcome to the number guessing game")
  print("I'm thinking of a number between 1 to 100")
  number = random.randint(1,100)
  attempt = difficulty()
  
  guess=0
  while guess!=number:
    print(f"You have {attempt} attempts left")

    guess = int(input("Make a guess"))
   
    
    attempt = compare(number,guess,attempt)
    if attempt!=0:
      print("Guess again")
    else:
      print("Goodbye")
      return
game()







    
    
    
    



    
