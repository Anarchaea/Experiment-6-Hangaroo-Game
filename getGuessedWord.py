def getGuessedWord(secretWord,lettersGuessed):
    word=""
    for x in secretWord:
        if x not in lettersGuessed:
            word+=" _ "
        else:
            word+=x
    return word