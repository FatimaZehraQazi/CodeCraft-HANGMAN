import random #importing random function to be able to randomize which fruit the player has to guess
def getrandomword(): #function to get random word
    fruit_list = [
    'blueberry', 'blackberry', 'apple', 'banana', 'orange', 'grapefruit', 'strawberry', 'pineapple', 'peach', 'mango',
    'watermelon', 'sugarmelon','coconut','kiwi','cherry','avacado','grapes','pomogranate','raspberry','gooseberry','lychee','jackfruit','guava',
    'fig','durian','Rambutan','Persimmon','Quince','Canary melon','Pomelo','Soursop','Feijoa','Ackee','Carambola','Custard apple',
    'Chempedak','Jocote','Kabosu','Atemoya','Lucuma'] #making a fruit list for the choices pf the hangman game
    word = random.choice(fruit_list) #assigning the random choice to the variable word
    return word.upper() #returning the word in upper case letters for example ; BANANA

def play(word): #Word is the parameter that is used from the previous function and play is the name of the function for the hangman code
    hangman = "_" * len(word) # to output the number of blank spaces that represent the word
    guessed = False # if the word is guessed, the flag will be turned to true and the round will end
    guessed_letters = [] #initialize an empty list that will add the numbers that have already been guessed
    tries =  0 #number of tries that are used until the player losesbanana
    print(visual(tries)) # To print the visual art for the number of tries
    print(hangman) #to print the ____________
    print("the word has", len(hangman),"letters")

    while not guessed and tries < 9: #run a loop until either the player guesses the word or runs out og tries
        guess = input("Make your sacred guess :")#to take the guess from the player and convert it to upper case
        while guess.isalpha() == False:
            guess = input("Make your sacred guess:")
        guess = (guess.upper())


        if len(guess) == 1 and guess.isalpha(): #to check if the word is an alphabet
            print("The already used letters are :", guessed_letters)
            if guess in guessed_letters: #if the alphabet is already used before
                print(guess," is already taken. Try again.") # outputs the alphabet guessed
            elif guess not in word: # if alphabt us not in the word
                print("You are leading towards losing the battle.", guess, "is not in the word")
                tries = tries + 1 # decrement the num of triesz
                print("You have",9 - tries,"chances left")
                guessed_letters.append(guess) #append the list for the already guessed lketters
            else:
                print(guess, "is in the word. Congrats! You are one step closer to victory.") # alphaber is in the woird
                guessed_letters.append(guess) #append the list

                new_hangman = "" #create a new string (emoty) for the update of the hangman
                for i in range(len(word)): #run a loop till the length of the word
                    if word[i] == guess: #if the position (i) of the word matches the lettere guessed
                        new_hangman += guess # it will update the letter at that positioin
                    else:
                        new_hangman += hangman[i] #else it will upodate ____
                hangman = new_hangman #word completed will be updated to new hangman
                if "_" not in hangman: # if ___ are not present anymore, ie all letters have been guesed,
                    guessed = True #flag will turn true
        print(visual(tries)) #print the art
        print(hangman) #print the hangman ________
        if tries == 9:
            print(visual(9))
            print("Oops! You lost (oT-T)尸.....")
            print("Better luck next time! The word was", word)



def visual(tries):
    art = [""" 
                   --------
                   |      |
                   |   
                   |   
                   |    
                   |      
                   |
                   -
                                """,
       """
                   --------
                   |      |
                   |      O
                   |     
                   |     
                   |     
                   |
                   -
                                       """,
       """
                   --------
                   |      |
                   |      O
                   |      |
                   |      
                   |      
                   |
                   -
                                """,
       """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   |
                   -
                                """,
       """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |    
                   |
                   -
                                """,
       """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   |
                   -
                                """,
       """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |       \ 
                   |
                   -
                                """,
       """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \ 
                   |
                   -
                                """,
       """
                   --------
                   |      |
                   |
                   |      O
                   |     \|/
                   |      |
                   |     / \ 
                   -
                                """,
       """
                   --------
                   |      |
                   |      O
                   |
                   |     \|/
                   |      |
                   |     / \ 
                   -
                                """
       ]
    return art[tries]


def main():
    print("Hi! Welcome to the GameHub!")
    name = input("May I know your name? : ")
    print("Hi",name,". Today we are playing Hangman~")
    print("Rules are simple! :")
    print("1. The category is limited to fruits only (^ _ ^)/")
    print("2. You can only input one alphabet at a time.)")
    while input("Do you wish to start? (Y/N):").upper() == "Y":
        print("Alright! Brace yourself!")
        print("Ready?")
        print("Go!")
        print("\n")
        print("Enjoy !")
        word = getrandomword()
        play(word)
        while input("Do you wish to play again? (Y/N)").upper() == "Y":
            word = getrandomword()
            play(word)
main()