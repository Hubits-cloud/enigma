from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflect


I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

A = Reflect("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflect("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflect("FVPJIAOYEDRZXWGCTKUQSBNMHL")

keyboard = Keyboard()
plug = Plugboard(["AR", "GK", "OX"])

def main():
    letter = "A"
    signal = keyboard.forward(letter)
    signal = plug.forward(signal)
    signal = III.forward(signal)
    signal = II.forward(signal)
    signal = I.forward(signal)
    signal = A.reflect(signal)
    signal = I.backward(signal)
    signal = II.backward(signal)
    signal = III.backward(signal)
    signal = plug.backward(signal)
    letter = keyboard.backward(signal)
    print(letter)
    

if __name__ == "__main__":
    main()