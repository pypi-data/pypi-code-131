#!/usr/bin/python3
import RPi.GPIO as GPIO
import sys
from time import sleep

# Python program to implement Morse Code Translator
# Modifed to interface with the RPi.GPIO API
# source: https://www.geeksforgeeks.org/morse-code-translator-python/

channel = 12

'''
VARIABLE KEY
'cipher' -> 'stores the morse translated form of the english string'
'decipher' -> 'stores the english translated form of the morse string'
'citext' -> 'stores morse code of a single character'
'i' -> 'keeps count of the spaces between morse characters'
'message' -> 'stores the string to be encoded or decoded'
'''

# Dictionary representing the morse code chart
MORSE_CODE_DICT = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ',': '--..--',
    '.': '.-.-.-',
    '?': '..--..',
    '/': '-..-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-',
}


# Function to encrypt the string according to the morse code chart
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':

            # Looks up the dictionary and adds the correspponding morse code
            # along with a space to separate morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different character and 2 indicates different words
            cipher += ' '

    return cipher


# Function to decrypt the string from morse to english
def decrypt(message):

    # extra space added at the end to access the last morse code
    message += ' '

    decipher = ''
    citext = ''
    for letter in message:

        # checks for space
        if (letter != ' '):
            # counter to keep track of space
            i = 0
            # storing morse code of a single character
            citext += letter
        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1
            # if i = 2 that indicates a new word
            if i == 2:
                # adding space to separate words
                decipher += ' '
            else:
                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''

    return decipher


def long_pulse():
    GPIO.output(channel, GPIO.HIGH)
    sleep(.4)
    GPIO.output(channel, GPIO.LOW)


def short_pulse():
    GPIO.output(channel, GPIO.HIGH)
    sleep(.2)
    GPIO.output(channel, GPIO.LOW)


def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(channel, GPIO.OUT)

    if len(sys.argv) > 1:
        msg = sys.argv[1]
    else:
        msg = "hello world"
    result = encrypt(msg.upper())

    for i in result:
        if i == "-":
            long_pulse()
        elif i == ".":
            short_pulse()
        else:
            sleep(.5)
        sleep(.1)
    GPIO.cleanup()


# Executes the main function
if __name__ == '__main__':
    main()
