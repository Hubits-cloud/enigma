class Plugboard:

    def __init__(self, pairs):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for pair in pairs:
            a = pair[0]
            b = pair[1]
            pos_a = self.left.find(a)
            pos_b = self.left.find(b)
            self.left = self.left[:pos_a] + b + self.left[pos_a + 1:]
            self.left = self.left[:pos_b] + a + self.left[pos_b + 1:]

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal
    
    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal