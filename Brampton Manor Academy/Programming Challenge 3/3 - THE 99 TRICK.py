# Programming Challenge 3 - THE 99 TRICK

# Calculation
def calculation(answer,friends_number):
  factor = 99 - answer
  total = factor + friends_number
  total = str(total)
  calc_result = friends_number - (int(total[0]) + int(total[1:]))
  return calc_result

# Main program
def run():
  print("We are going to play a game. I want you to pick a number then do a series of calculations. I bet I know what the result of those calculations will be!")
  answer = int(input("*You* This will be the answer. Select a number between 10-49: "))
  friends_number = int(input("*Player*  Pick any number 50-99: "))
  print("\nI said the answer was",answer,"and the calculation result is",calculation(answer,friends_number))

# Run
run()
