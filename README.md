# Project Enigma

    #### Video Demo:  https://youtu.be/QGdJcZaiVYc

    ### Description:
    For my project i decided to recreate the enigma ciphering system. I decided to do this after watching The Imitation Game with my class. 
    The machine is made of a keyboard, a plugboard, three rotors, and reflector. I will go over all of these pieces separately later.
    First of all the path of the signal, and in that sense the order each leter get enciphered. When a letter is typed it first goes to the plugboard, after that it goes through all three rotors, it then gets reflected back by the reflector, back through the rotors, through the plugboard and out to the lampboard. Don't worry, we'll get to what each of the things do.

    ### Design Choices:
    You may notice that when counting to 26 for the letters, instead of going from 0-25 i go from 1-26. That is was to avoid confusion when going back and forth between wikipedia, and my code.
    When it comes to the rotor and reflector setting, i decided to go with their historical values, taken from wikipedia.

    ### Plugboard:
    The plugboard takes two different letters and switch their values, for example if you typed 'AG' then when ever the plugboard would recieve A it would come out as a G and vise verca. The plugboard can take as many values as you want as long as each letter only appears once. So for example you can't say 'AG' and 'AD'.

    ### Rotors:
    You can choose between 5 different rotors, each rotor has 2 alphabets, the right and left. The right alphabet is a normal alphabet, from a to z, but the left one is different for each rotor. So if 'a' is input then on one rotor it might come out as a 'C' while on another rotor it might come out as a 'T'. And to make it even more secure, after a signal has been passed through the rotor, the left alphabet turns one space on the right most rotor. So even if you type the same letter twice, it'll come out as different letters both times.

    ### Reflector:
    You can choose between 3 different reflectors. The reflectors work the same way as the rotors, except they dont rotate.

    ### Lampboard:
    The lampboard one the real enigma machine is what showed the enciphered letter, here it only returns the signal of the enciphered letter.
