import random
import sys
import time


def DisplayCurrentState():
    for i in currentState:
        print(i + '', end='')

    print('\n')


def UpdateState(userLetter):
    for i in range(len(currentState)):
        if wordlist[i] == userLetter:
            currentState[i] = userLetter


def GameOver():
    global wordGuessed

    if wordlist == currentState:
        wordGuessed = True
        DisplayCurrentState()
        print('\n')
        print('Congrats You Win')
        print('Thanks for playing')
        sys.exit()
    # elif wordlist == currentState:
    # wordGuessed = False


def DisplayHangman(count):
    if count == 1:
        print(
            "        _________ \n"
            "       |      ()    \n"
            "       |          \n"
            "       |          \n"
            "       |          \n"
            "       |          \n"
            "       |          \n"
            "       |  \n"
            "    ___|___ \n"
        )
        print("Wrong input " + str(limit - count) + " attempts remaining ")

    elif count == 2:
        print(
            "        _________ \n"
            "       |      ()    \n"
            "       |      \/   \n"
            "       |      ||   \n"
            "       |          \n"
            "       |          \n"
            "       |          \n"
            "       |  \n"
            "    ___|___ \n"
        )
        print("Wrong input " + str(limit - count) + " attempts remaining ")

    elif count == 3:
        print(
            "        _________ \n"
            "       |      ()    \n"
            "       |      \/   \n"
            "       |      ||   \n"
            "       |     ----    \n"
            "       |          \n"
            "       |          \n"
            "       |  \n"
            "    ___|___ \n"
        )
        print("Wrong input " + str(limit - count) + " attempts remaining ")

    elif count == 4:
        print("Wrong input " + str(limit - count) + " attempts remaining ")
        print("Sorry You Lost !")
        DisplayCurrentState()
        print('\n')
        print('The word was ' + str(word))
        print('Thanks for playing')
        sys.exit()


with open("words") as f:
    listOfwords = f.read().splitlines()

count = 0

random_num = random.randint(0, len(listOfwords) - 1)
word = listOfwords[random_num]
wordlist = list(word)

currentState = ['_'] * len(wordlist)

wordGuessed = False

name = input("what is your name : ")
print("\n")
time.sleep(2)
print("Welcome " + name + " Enjoy ")
time.sleep(2)
print("\n")
print("You have 3 attempts to Guess the Correct Word")

while not wordGuessed:
    limit = 4
    DisplayCurrentState()
    userLetter = input('Guess a Letter : ')
    print()

    if userLetter in wordlist:
        if userLetter in currentState:
            print('You already guessed this later')
        else:
            UpdateState(userLetter)

        GameOver()

    else:
        count += 1
        if count == 1:
            DisplayHangman(count)
            print("\n")
            print('Try again')

        elif count == 2:
            DisplayHangman(count)
            print("\n")
            print('Try again')

        elif count == 3:
            DisplayHangman(count)
            print("\n")
            print('Try again')

            print("\n")
            print('One Final Attempt')

        elif (count == 4):
            DisplayHangman(count)
