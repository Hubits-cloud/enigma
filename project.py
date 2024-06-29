# TODO everything works, now make input and output

from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflect
from enigma import Enigma

# historicly accurate enigma components taken from wikipedia: https://en.wikipedia.org/wiki/Enigma_rotor_details


#plugboard settings. TODO: give user acces to change plugboard settings
#plug = Plugboard(["AB", "CD", "EF"])

# define Enigma machine. TODO: allow user to input own combination of rotors and reflectors
#ENIGMA = Enigma(B,IV,II,I,plug,keyboard)

def main():

    message = input("Type message to encipher: ").strip().upper()
    ciphered_message = ""

    keyboard = Keyboard()
    plug = Plugboard(get_plugboard())
    reflector = get_reflector()
    left_rotor = get_rotor_left()
    middle_rotor = get_rotor_middle()
    right_rotor = get_rotor_right()
    key = get_key()
    rings = get_rings()

    ENIGMA = Enigma(reflector, left_rotor, middle_rotor, right_rotor, plug, keyboard)
    ENIGMA.set_key(key)
    ENIGMA.set_rings(rings)

    for letter in message:
        ciphered_message = ciphered_message + ENIGMA.encipher(letter)
    print(ciphered_message)
    # ENIGMA = Enigma(B,IV,II,I,plug,keyboard)
    #ENIGMA.set_key("CAT")

    #ENIGMA.set_rings((5,26,2))

    #message = "TESTINGTESTINGTESTINGTESTING"
    #cipher_text = ""
    #for letter in message:
        #cipher_text = cipher_text + ENIGMA.encipher(letter)
    #print(cipher_text)

def get_plugboard():
    while True:
        plug_txt = input("Please type plugboard connection with a space in between. E.g: AB CD EF: ").upper().strip()
        plug = plug_txt.split()
        length = len(plug_txt.replace(" ",""))
        if len(plug) != length / 2:
            print("ERR only input two chars per pair")
            continue

        letters = [x for x in plug_txt]
        letters = [x.strip(' ') for x in letters]
        letters[:] = [x for x in letters if x]
        for x in letters:

            if letters.count(x) != 1:
                print ("ERR only use one instance per char")
                continue

            elif isfloat(x):
                print("ERR only input chars")
                continue

            else:
                return plug
    
        
def get_reflector():
    A = Reflect("EJMZALYXVBWFCRQUONTSPIKHGD")
    B = Reflect("YRUHQSLDPXNGOKMIEBFZCWVJAT")
    C = Reflect("FVPJIAOYEDRZXWGCTKUQSBNMHL")

    while True:
        usr_input = input("Please chose between reflector A, B, & C: ").upper().strip()
        if usr_input != "A" and usr_input != "B" and usr_input !="C":
            print("ERR please chose between A, B, & C")
            continue

        elif usr_input == "A":
            return A
        
        elif usr_input == "B":
            return B
        
        elif usr_input == "C":
            return C
        
        else:
            print("ERR unknown error")
            continue


def get_rotor_left():
    I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
    II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
    III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
    IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
    V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

    while True:
        usr_input = input("Please chose between rotor I, II, III, IV, & V for the left rotor: ").upper().strip()

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
            print("ERR please chose between I, II, III, IV, & V")
            continue
        
        else:
            print("ERR unknown error")
            continue

def get_rotor_middle():
    I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
    II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
    III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
    IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
    V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

    while True:
        usr_input = input("Please chose between rotor I, II, III, IV, & V for the middle rotor: ").upper().strip()

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
            print("ERR please chose between I, II, III, IV, & V")
            continue
        
        else:
            print("ERR unknown error")
            continue

def get_rotor_right():
    I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
    II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
    III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
    IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
    V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

    while True:
        usr_input = input("Please chose between rotor I, II, III, IV, & V for the right rotor: ").upper().strip()

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
            print("ERR please chose between I, II, III, IV, & V")
            continue
        
        else:
            print("ERR unknown error")
            continue

def get_key():
    while True:
        usr_input = input("Please type a 3 char keyword, you may use any letter of the english alphabet: ").upper().strip()
        usr_input = usr_input.replace(" ", "")
        if len(usr_input) != 3:
            print("ERR key must be three chars long")
            continue

        for letter in usr_input:
            if letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                print("ERR char is not a letter in the english alphabet")
                continue

        key_word = usr_input
        return key_word

def get_rings():
    while True:
        usr_input = input("Please input three ints between 1 & 26: ").strip()
        
        try:
            a, b, c = usr_input.split()
        except ValueError:
            print ("Please type three different ints")
            continue

        if len(a) + len(b) + len(c) > 6:
            print("ERR please choose between 1 and 26")
            continue

        if a.isnumeric() == False or b.isnumeric() == False or c.isnumeric() == False:
            print("ERR non int input")
            continue

        try:
            a = int(a)
            b = int(b)
            c = int(c)
        except:
            print("ERR non int input")
            continue

        if a > 26 or b > 26 or c > 26:
            print("ERR please choose between 1 and 26")
            continue

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