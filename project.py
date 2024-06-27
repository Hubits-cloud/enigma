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
plug = Plugboard(["AB", "CD", "EF"])

# define Enigma machine. TODO: allow user to input own combination of rotors and reflectors
ENIGMA = Enigma(B,IV,II,I,plug,keyboard)

def main():
    ENIGMA.set_key("CAT")

    ENIGMA.set_rings((5,26,2))

    message = "TESTINGTESTINGTESTINGTESTING"
    cipher_text = ""
    for letter in message:
        cipher_text = cipher_text + ENIGMA.encipher(letter)
    print(cipher_text)
    

if __name__ == "__main__":
    main()