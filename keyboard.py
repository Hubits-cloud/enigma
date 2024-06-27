class Keyboard:
    # the user presses a letter and its translated into a signal
    def forward(self, letter):
        # returns the position of the letter in the alphabet
        signal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
        return signal

    # takes a signal and converts it to a letter in the "lampboard"
    def backward(self, signal):
        letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[signal]
        return letter