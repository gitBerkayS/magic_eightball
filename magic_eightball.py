import random

user = input("What's your name?\n")
if user == "":
  print("You haven't entered any name. Please re-run the program.")
  exit()
else:
  answer = input("Hello " + user + ", " + "this is the magic 8-ball. Ask away!\n")
  print(user + " " + "asks: " + answer)

random_number = random.randint(1, 9)
#print(random_number)

if random_number == 1:
  eight_ball = "Yes - definitely"
elif random_number == 2:
  eight_ball = "It is decidedly so"
elif random_number == 3:
  eight_ball = "Without a doubt"
elif random_number == 4:
  print("Reply hazy, try again")
elif random_number == 5:
  eight_ball = "Ask again later"
elif random_number == 6:
  peight_ball = "Better not tell you now"
elif random_number == 7:
  eight_ball ="My sources say no"
elif random_number == 8:
  eight_ball = "Outlook not so good"
elif random_number == 9:
  eight_ball = "Very doubtful"
else:
  print("Error")

print("Magic 8-Ball's answer: " + eight_ball)



