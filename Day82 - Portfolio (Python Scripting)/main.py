# TASK: take any String input and convert it into Morse Code

# MORSE CODE: Morse code is a method used in telecommunication to encode text characters as sequences of two different signal durations, called dots and dashes or dits and dahs. It was originally developed for use in telegraphy between electrical telegraphs. Each character is represented by a unique sequence of dots and dashes. For example, the letter “A” is represented as “.-” and the letter “B” is represented as “-...”.


# Step 1: create a dictionary where keys are alphabetic characters and values are the coresponding morse codes

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '\'': '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}


# Step 2: prompt the user for an Input strng which we will conveert to a morse code later on

user_input = input("Please enter a String/Word:")

# Step 3: Convert the input string to uppercase

user_input_upper = user_input.upper()

# Step 4: Iterate inside the input string and replace each character with the coresponding Morse code. 
# Eventually save the characters inside a variable

morse_code = ""
for char in user_input_upper:
  if char in morse_code_dict:
    morse_code += morse_code_dict[char]
  else:
    raise MorseCodeNotFoundError(f"Character '{char}' not found in Morse code dictionary.")
    

print("Your String has been converted to Morse code:", morse_code)
