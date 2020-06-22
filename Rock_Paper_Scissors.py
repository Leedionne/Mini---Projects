Rock_Paper_Scissors
a = "rock"
b = "paper"
c = "scissor"
words = [a, b, c]
computer_win = 0
user_win =0
i = 0
while i < 5:
computer = choice([a, b, c])
user = input(“tell Ur choice:”)
if user not in words:
print(“Spelling Mistake!”)
break
elif user == computer:
print(“Both have chosen the same. Let’s, play again”)
elif ((computer == a and user == c) or
(computer == b and user == a) or
(computer == c and user == b)):
print(“Computer Wins!”)
computer_win += 1
else:
print(“User Wins!”)
user_win +=1
print(f"Computer choose: {computer}")
i += 1
print(f"Computer Won= { computer_win} and User won= {user_win}")