# This is a responsive Rock, Paper, and Scissors Game!
# Enjoy! :)

print("Welcome to the rock, paper, and scissors game!")
p1 = input("What is the first player name? ")
p2 = input("What is the second player name? ")
print("Welcome " + p1 + " and " + p2 + " !")

choice_1 = input(p1 + " goes first! What do you select? Rock, Paper, or Scissors? ")
choice_2 = input(p1 + " goes first! What do you select? Rock, Paper, or Scissors? ")
rock = 1
scissor = 0
paper = 1

if choice_1.upper() == "rock" & choice_2.upper() == "paper":
    print("hi")
