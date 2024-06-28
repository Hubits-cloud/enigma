# TODO everything works, now make input and output

from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflect
from enigma import Enigma

# historicly accurate enigma components taken from wikipedia: https://en.wikipedia.org/wiki/Enigma_rotor_details
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
A = Reflect("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflect("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflect("FVPJIAOYEDRZXWGCTKUQSBNMHL")

keyboard = Keyboard()

#plugboard settings. TODO: give user acces to change plugboard settings
#plug = Plugboard(["AB", "CD", "EF"])

# define Enigma machine. TODO: allow user to input own combination of rotors and reflectors
#ENIGMA = Enigma(B,IV,II,I,plug,keyboard)

def main():
    
    plug = get_reflector()
    print (plug)
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
    while True:
        usr_input = input("Please chose between rotor I, II, III, IV, & V: ").upper().strip()
        if usr_input != "I" and usr_input != "II" and usr_input !="III" and usr_input !="IV" and usr_input !="V":
            print("ERR please chose between I, II, III, IV, & V")
            continue

        elif usr_input == "I":
            return I
        
        elif usr_input == "II":
            return II
        
        elif usr_input == "III":
            return III
        
        elif usr_input == "IV":
            return IV
        
        elif usr_input == "V":
            return V
        
        else:
            print("ERR unknown error")
            continue

def get_rotor_middle():
    while True:
        usr_input = input("Please chose between rotor I, II, III, IV, & V: ").upper().strip()
        if usr_input != "I" and usr_input != "II" and usr_input !="III" and usr_input !="IV" and usr_input !="V":
            print("ERR please chose between I, II, III, IV, & V")
            continue

        elif usr_input == "I":
            return I
        
        elif usr_input == "II":
            return II
        
        elif usr_input == "III":
            return III
        
        elif usr_input == "IV":
            return IV
        
        elif usr_input == "V":
            return V
        
        else:
            print("ERR unknown error")
            continue

def get_rotor_right():
    while True:
        usr_input = input("Please chose between rotor I, II, III, IV, & V: ").upper().strip()
        if usr_input != "I" and usr_input != "II" and usr_input !="III" and usr_input !="IV" and usr_input !="V":
            print("ERR please chose between I, II, III, IV, & V")
            continue

        elif usr_input == "I":
            return I
        
        elif usr_input == "II":
            return II
        
        elif usr_input == "III":
            return III
        
        elif usr_input == "IV":
            return IV
        
        elif usr_input == "V":
            return V
        
        else:
            print("ERR unknown error")
            continue

def get_key():
    while True:
        usr_input = input("Please type a 3 char keyword, you may use any letter of the english alphabet: ").upper().strip()
        for letter in usr_input:
            if letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                print("ERR char is not a letter in the english alphabet")
                continue  
        key_word = usr_input
        return key_word

def get_rings():
    ...
    
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    main()