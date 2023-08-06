alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("type 'encode' to encrypt, type 'decode' to decrypts:\n")
text = input("Type your message:\n").lower()
shift = int(input("type the shift number\n"))

# don't change the above:

# To Do-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt (plain_text,shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f'Your encrypted text is: {cipher_text}')

encrypt(text,shift)







# To DO-2: inside 'encrypt' function, shift each letter of the 'text' forward in the alphabet by
# the shift amount and print the encrypted text

#e.g.
#plain_text = "hello"
#shift = 5
#
