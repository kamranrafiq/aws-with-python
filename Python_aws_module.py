def igpay(a_word):
    vowels = "aeiou"
    
    if a_word[0] in vowels:
        return a_word + "way"
    else:
        return a_word[1:] + a_word[0] + "ay"
        
