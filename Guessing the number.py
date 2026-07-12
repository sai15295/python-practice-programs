secret_number = 83
guess_number = int(input("Guess the number: "))
if secret_number == guess_number:
  print("Your guess is correct")
  print("You won the reward")
else:
  print("Your guess is wrong")
  print("No reward")
