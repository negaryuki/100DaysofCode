alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("type 'encode' to encrypt, type 'decode' to decrypts:\n")
text = input("Type your message:\n").lower()
shift = int(input("type the shift number\n"))


# don't change the above:

# To DO -1: combine the encrypt and decrypt function into a single function called ceasar().


# def ceasar(ceasar_text, ceasar_shift, ceasar_direction):
#     end_text = ""
#
#     if ceasar_direction == "encode":
#         for letter in ceasar_text:
#             position = alphabet.index(letter)
#             new_position = position + ceasar_shift
#             new_letter = alphabet[new_position]
#             end_text += new_letter
#         print(f'Your encoded text is: {end_text}')
#
#     elif ceasar_direction == "decode":
#         for letter in ceasar_text:
#             position = alphabet.index(letter)
#             new_position = position - ceasar_shift
#             new_letter = alphabet[new_position]
#             end_text += new_letter
#         print(f'Your decoded text is: {end_text}')

# or we could just simplify it as below:

def ceasar(ceasar_text, ceasar_shift, ceasar_direction):
    end_text = ""
    if ceasar_direction == "decode":
        ceasar_shift *= -1

    for letter in ceasar_text:
        position = alphabet.index(letter)
        new_position = position + ceasar_shift
        end_text += alphabet[new_position]
    print(f'Your {ceasar_direction} text is: {end_text}')


ceasar(text, shift, direction)
