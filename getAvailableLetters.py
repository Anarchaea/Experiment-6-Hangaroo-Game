def getAvailableLetters(lettersGuessed):
    alp='abcdefghijklmnopqrstuvwxyz'
    string=""
    for x in alp:
        if x in lettersGuessed:
            alp.replace(x," ")
        else:
            string+=x
    return string
            