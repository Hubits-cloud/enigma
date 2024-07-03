import sys

from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflect
from enigma import Enigma

# historicly accurate enigma components taken from wikipedia: https://en.wikipedia.org/wiki/Enigma_rotor_details


def main():

    # get the user input
    message = input("Type message to encipher: ").strip().upper()
    plug_input = input("Please type plugboard connection with a space in between. E.g: AB CD EF: ").upper().strip()
    reflector_input = input("Please chose between reflector A, B, & C: ").upper().strip()
    rotorL_input = input("Please chose between rotor I, II, III, IV, & V for the left rotor: ").upper().strip()
    rotorM_input = input("Please chose between rotor I, II, III, IV, & V for the middle rotor: ").upper().strip()
    rotorR_input = input("Please chose between rotor I, II, III, IV, & V for the right rotor: ").upper().strip()
    key_input = input("Please type a 3 char keyword, you may use any letter of the english alphabet: ").upper().strip()
    ring_input = input("Please input three ints between 1 & 26: ").strip()

    # prepare an empty var for the ciphered message
    ciphered_message = ""

    #prepares the functions and classes
    keyboard = Keyboard()
    plug = Plugboard(get_plugboard(plug_input))
    reflector = get_reflector(reflector_input)
    left_rotor = get_rotor_left(rotorL_input)
    middle_rotor = get_rotor_middle(rotorM_input)
    right_rotor = get_rotor_right(rotorR_input)
    key = get_key(key_input)
    rings = get_rings(ring_input)

    # prepares the cipher with the given parameters
    ENIGMA = Enigma(reflector, left_rotor, middle_rotor, right_rotor, plug, keyboard)
    # prepares the keys and rings for the cipher
    ENIGMA.set_key(key)
    ENIGMA.set_rings(rings)

    # goes through each letter in the message and enciphers them
    for letter in message:
        ciphered_message = ciphered_message + ENIGMA.encipher(letter)
    print(ciphered_message)

def get_plugboard(s):
    while True:
        # get the input
        plug_txt = s
        plug = plug_txt.split()
        # gets the length of the input after removing spaces
        length = len(plug_txt.replace(" ",""))

        # checks if the length of plug is half the length of length, because plug is only supposed to be 2 chars
        if len(plug) != length / 2:
            sys.exit("ERR only input two chars per pair")
            

        # splits the plug into single chars and removes spaces
        letters = [x for x in plug_txt]
        letters = [x.strip(' ') for x in letters]
        letters[:] = [x for x in letters if x]
        for x in letters:

            if letters.count(x) != 1:
                sys.exit ("ERR only use one instance per char")
                

            elif isfloat(x):
                sys.exit("ERR only input chars")
                

            else:
                return plug
    
        
def get_reflector(s):
    # historicly accurate enigma components taken from wikipedia: https://en.wikipedia.org/wiki/Enigma_rotor_details
    A = Reflect("EJMZALYXVBWFCRQUONTSPIKHGD")
    B = Reflect("YRUHQSLDPXNGOKMIEBFZCWVJAT")
    C = Reflect("FVPJIAOYEDRZXWGCTKUQSBNMHL")

    while True:
        # gets the user input
        usr_input = s

        # ensures that either A, B, or C was inputtet
        if usr_input != "A" and usr_input != "B" and usr_input !="C":
            sys.exit("ERR please chose between A, B, & C")
            

        elif usr_input == "A":
            return A
        
        elif usr_input == "B":
            return B
        
        elif usr_input == "C":
            return C
        
        else:
            sys.exit("ERR unknown error")
            


def get_rotor_left(s):
    # historicly accurate enigma components taken from wikipedia: https://en.wikipedia.org/wiki/Enigma_rotor_details
    I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
    II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
    III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
    IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
    V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

    while True:
        # get the input of the user
        usr_input = s

        if usr_input == "I" or usr_input == "1" or usr_input == "ONE":
            return I
        
        elif usr_input == "II" or usr_input == "2" or usr_input == "TWO":
            return II
        
        elif usr_input == "III" or usr_input == "3" or usr_input == "THREE":
            return III
        
        elif usr_input == "IV" or usr_input == "4" or usr_input == "FOUR":
            return IV
        
        elif usr_input == "V" or usr_input == "5" or usr_input == "FIVE":
            return V
        
        elif usr_input != "I" and usr_input != "II" and usr_input !="III" and usr_input !="IV" and usr_input !="V":
            sys.exit("ERR please chose between I, II, III, IV, & V")
            
        
        else:
            sys.exit("ERR unknown error")
            

def get_rotor_middle(s):
    # historicly accurate enigma components taken from wikipedia: https://en.wikipedia.org/wiki/Enigma_rotor_details
    I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
    II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
    III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
    IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
    V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

    while True:
        # get the input of the user
        usr_input = s

        if usr_input == "I" or usr_input == "1" or usr_input == "ONE":
            return I
        
        elif usr_input == "II" or usr_input == "2" or usr_input == "TWO":
            return II
        
        elif usr_input == "III" or usr_input == "3" or usr_input == "THREE":
            return III
        
        elif usr_input == "IV" or usr_input == "4" or usr_input == "FOUR":
            return IV
        
        elif usr_input == "V" or usr_input == "5" or usr_input == "FIVE":
            return V
        
        elif usr_input != "I" and usr_input != "II" and usr_input !="III" and usr_input !="IV" and usr_input !="V":
            sys.exit("ERR please chose between I, II, III, IV, & V")
            
        
        else:
            sys.exit("ERR unknown error")
            

def get_rotor_right(s):
    # historicly accurate enigma components taken from wikipedia: https://en.wikipedia.org/wiki/Enigma_rotor_details
    I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
    II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
    III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
    IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
    V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

    while True:
        # get the input of the user
        usr_input = s

        if usr_input == "I" or usr_input == "1" or usr_input == "ONE":
            return I
        
        elif usr_input == "II" or usr_input == "2" or usr_input == "TWO":
            return II
        
        elif usr_input == "III" or usr_input == "3" or usr_input == "THREE":
            return III
        
        elif usr_input == "IV" or usr_input == "4" or usr_input == "FOUR":
            return IV
        
        elif usr_input == "V" or usr_input == "5" or usr_input == "FIVE":
            return V
        
        elif usr_input != "I" and usr_input != "II" and usr_input !="III" and usr_input !="IV" and usr_input !="V":
            sys.exit("ERR please chose between I, II, III, IV, & V")
            
        
        else:
            sys.exit("ERR unknown error")
            

def get_key(s):
    while True:
        usr_input = s
        usr_input = usr_input.replace(" ", "")
        if len(usr_input) != 3:
            sys.exit("ERR key must be three chars long")
            

        for letter in usr_input:
            if letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                sys.exit("ERR char is not a letter in the english alphabet")
                

        key_word = usr_input
        return key_word

def get_rings(s):
    while True:
        usr_input = s
        
        try:
            a, b, c = usr_input.split()
        except ValueError:
            sys.exit ("Please type three different ints")
            

        if len(a) + len(b) + len(c) > 6:
            sys.exit("ERR please choose between 1 and 26")
            

        if a.isnumeric() == False or b.isnumeric() == False or c.isnumeric() == False:
            sys.exit("ERR non int input")
            

        try:
            a = int(a)
            b = int(b)
            c = int(c)
        except:
            sys.exit("ERR non int input")
            

        if a > 26 or b > 26 or c > 26:
            sys.exit("ERR please choose between 1 and 26")
            

        ring_tuple = (a, b, c)
        return ring_tuple

    
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    main()