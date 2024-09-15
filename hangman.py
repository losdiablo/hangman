import random
import string
import artAndWords # type: ignore
# chars=string.ascii_lowercase
# print(chars)
# numOfLetters=random.randint(5,20)
# print(numOfLetters)
# for letter in range(numOfLetters):
#     wordToGuess+=random.choice(chars)
def displayMan(wrongGuesses):
    print("***************")    
    for line in artAndWords.hangmanArt[wrongGuesses]:
        print(line)
    print("***************")    
def displayHint(hint):   
    print(" ".join(hint))
def displayAnswer(wordToGuess):  
    print(" ".join(wordToGuess))
def main():
    wordToGuess=random.choice(artAndWords.words)
    print(wordToGuess)
    hint=["_"] * len(wordToGuess)
    print(hint)
    wrongGuesses=0
    wrongLetters=set()
    guessedLetters=set()
    isRunning=True
    while isRunning:
        displayMan(wrongGuesses)
        displayHint(hint)
        # displayAnswer(wordToGuess)
        guess=input("enter the letter: ").lower()
        if len(guess) is not 1 or not guess.isalpha():
            print("invalid input !")
            continue
        if guess in guessedLetters:
            print(f"{guess} is already used")
            continue
        if guess in wordToGuess:
            for i in range(len(wordToGuess)):
                if wordToGuess[i]==guess:
                    hint[i]=guess
                    guessedLetters.add(guess)
        else:
            wrongGuesses+=1
        if "_"  not in hint:
            displayMan(wrongGuesses)
            displayAnswer(wordToGuess)
            print(" YOU WIN !")
            isRunning=False
        elif wrongGuesses >= len(artAndWords.hangmanArt)-1:
            displayMan(wrongGuesses)
            displayAnswer(wordToGuess)
            print(" YOU LOSE !")
            isRunning=False


if __name__=="__main__":
    main()
# print(hangmanArt[6])


