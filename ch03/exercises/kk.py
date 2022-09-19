import random
rand = random.randint(0,10)
print(rand)
win_condition = 0
number_of_guesses = 0
while win_condition == 0 and number_of_guesses < 3:    
  user_input = input("Pick a number between 0 and 10: ")
  if int(user_input) == rand:
    win_condition = 1
    print("Correct!")
  elif int(user_input) > rand: 
    print("Too High")
    
  elif int(user_input) < rand:
    print("Too Low")
  number_of_guesses += 1
if win_condition == 1:
  print("You Win")
elif number_of_guesses >= 3:
  print("You're trash try again next time")
 


