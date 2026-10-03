#Welcome To Rock Paper Scissors 
x=1
while x==1:
 Player1 = str(input("Player 1, enter your name: " ))
 Player2 = str(input("Player 2, enter your name: " ))
 print("Welcome", Player1, "and", Player2, "to Rock Paper Scissors!")
 c1=str(input(Player1 + ", choose 'rock', 'paper', or 'scissors'\n please type the word exactly: "))
 c2=str(input(Player2 + ", choose rock, paper, or scissors: "))
 if c1==c2:
     print("It's a tie!") 
 elif c1=="rock" and c2=="scissors":
     print(Player1, "wins!")
 elif c1=="scissors" and c2=="paper":
     print(Player1, "wins!")
 elif c1=="paper" and c2=="rock":            
     print(Player1, "wins!")
 elif c2=="rock" and c1=="scissors":
     print(Player2, "wins!")
 elif c2=="scissors" and c1=="paper":
     print(Player2, "wins!") 
 y= str(input("Do you want to play again? (yes/no): "))
 if y=="yes":
     x=1
 else:
     x=0
     print("Thanks for playing!")  
