alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

def encrypt(original_text, shift_amount):

    # TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
    #  by the shift amount and print the encrypted text.
    encrypted_text = ""

    # for letter in original_text:
    #     letter_index = alphabet.index(letter)
    #
    #     if letter_index + shift_amount > 25:
    #         new_shift_amount = (letter_index + shift_amount) - 26
    #         new_letter = alphabet[new_shift_amount]
    #         encrypted_text += new_letter
    #
    #     else:
    #         new_letter = alphabet[letter_index + shift_amount]
    #         encrypted_text += new_letter

    for letter in original_text:
        letter_index = alphabet.index(letter)
        new_letter = alphabet[(letter_index + shift_amount) % len(alphabet)]
        encrypted_text += new_letter

    print(f"Here is the encoded result: {encrypted_text}")

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?


# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

encrypt(text, shift)
