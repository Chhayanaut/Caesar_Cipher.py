alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import art
print(art.logo)

def cipher( plain_text, shift_amount, direction_text):
    emty_text = ""
    if direction_text == "decode":
        shift_amount *= -1

    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position+shift_amount
            emty_text += alphabet[new_position]
        else:
            emty_text += letter

    print(f'The {direction_text}d text is {emty_text}')

again_cipher = False
while not again_cipher:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 45
    cipher(plain_text=text, shift_amount=shift, direction_text=direction)
    result = input(print("Do you want to try more? No or Yes"))
    if result == "No":
        again_cipher = True
        print("See you later!")

