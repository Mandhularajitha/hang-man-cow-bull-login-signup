import random

def hangman():
    list_of_words=["shiri","raji","rashi","riji","jishi"]
    word=random.choice(list_of_words)
    print(word)
    turns=10
    guessmade=''
    valid_entey=set('abcdefghijklmnopqrstuvwxyz')
    # print(valid_entey)

    while len(word)>0:
        main_word=""
        
        for letter in word:
            if letter in guessmade:
                main_word=main_word+letter
            else:
                main_word=main_word+"_"
        if main_word==word:
            print(main_word)
            print("you won")
            break 

        print("guess the word",main_word)
        guess=input()

        if guess in valid_entey:
            guessmade+=guess
        else:
            print("enter valid character")  
            guess=input()

        if guess not in word:
            turns=turns-1
            if turns==9:
                print("9 turns left")
                print("---------------")
            if turns==8:
                print("8 turns left")
                print("---------------")
                print("       0       ")
            if turns==7:
                print("7 turns left")
                print("---------------")
                print("       0       ")
                print("       |       ")
            if turns==6:
                print("6 turns left")
                print("---------------")
                print("       0       ")
                print("       |       ")
                print("       /       ")
            if turns==5:
                print("5 turns left")
                print("----------------")
                print("       0       ")
                print("       |       ")
                print("      / \      ")
            if turns==4:
                print("4 turns left")
                print("----------------")
                print("      \0      ")
                print("       |       ")
                print("      / \      ")
            if turns==3:
                print("3 turns left")
                print("----------------")
                print("      \0/      ")
                print("       |       ")
                print("      / \      ")
            if turns==2:
                print("2 turns left")
                print("----------------")
                print("      \0/  |    ")
                print("       |       ")
                print("      / \      ")
            if turns==1:
                print("1 turns left hangman on his last breath")
                print("---------------")
                print("      \0/_|    ")
                print("       |       ")
                print("      / \      ")
            if turns==0:
                print("you loose")
                print("man die")
                print("----------------")
                print("       0/_|    ")
                print("       |       ")
                print("      / \      ")
                break                 
name=input("ENTER YOUR NAME ")
print("WELCOME",name)
print("__________________")
print("guess the word in less than 10 attempts")
hangman()
