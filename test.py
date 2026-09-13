
from colorama import init, Fore, Back, Style
import random 

init(autoreset=True)

Suggestions = {'Tumhe dillagi bhul jani padegi', 'hai kaha ka irada'}
print(Fore.GREEN + "\"Welco|\/|e to Prog|`am\"""\n      |  |ood  Chec|<er!")
print(Fore.GREEN + "=============================================")
print("\n                  \
  How are you:")

def Happy():
    print("\n Good! May you stay Happy, stay healthy & Fit", "Onec a Gentleman said: \n \"Happiness is the best makeup.\" — Drew Barrymore")

def Sad():
    print('\n Don\'t worry i am also! Please try to stay Happy & wish for Me Because i\'m also Sad listen NAFK and Enjoy the Sadness.')

print(Style.DIM + Fore.MAGENTA +"\n[1] Happy \n[2] Sad \n[3] Neutral")

def Neutral():
    print("This Update is Undergoing\n", "I have a Game for you","\n")

def guessing():
    number = random.randint(1, 10)
    attempt = 0
    
    while True:
        print(attempt)
        user = int(input("Guess a number 1 to 10: "))
        if user == number:
            
            print ("You win")
            break
        else:
            attempt += 1
            print(Fore.RED + "Try again: \n")
choice = int(input(Style.DIM + Fore.YELLOW + "\nEnter Yours: "))
if choice == 1:
   Happy()

elif choice == 2:
    Sad()
    suggest =  input("Do you want any suggestions?:\n Y/N\n ")
    if suggest == "y":
        print("Try:\n", Suggestions,)

    else:
        print("Try:\n", "[1] Talk Someone")    

elif choice == 3: 
    Neutral()
    play = input("Enter Y/N: ")
    if play == "y":
        # print(attempt)
        guessing()
    elif play == "n":
        print("don\' Worrie We not Forceing")
    else:
        print(Fore.RED + "\n!Invalid choice\n""Maybe try Again") 