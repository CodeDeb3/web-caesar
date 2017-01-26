def alphabet_position(letter):
    #return value of letter

    lowlist= "abcdefghijklmnopqrstuvwxyz"

    if letter.lower() in lowlist:
        return lowlist.index(letter.lower())

def rotate_character(char,rot):
    #rotate character by finding position from above function

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    if char.isalpha() and char.islower():
        rot = (alphabet_position(char) + int(rot))%26  #mod 26 so it wraps around
        Newchar = alphabet[rot]
        return Newchar

    elif char.isalpha() and char.isupper():
        rot = (alphabet_position(char.lower()) + int(rot))%26
        Newchar = alphabet[rot].upper()
        return Newchar

    else:
        return char

def encrypt(message, rot):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = ''
    for char in text:
        cipher = cipher + rotate_character(char,rot)
    return cipher
