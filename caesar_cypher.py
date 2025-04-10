# list of characters

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
coded_message = []


# The main function
def caeser_cypher():
    action = input("Type \"encode\" to encrypt or \"decode\" to decrypt: ")
    if action.lower() == "end":
        quit()
    elif action.lower() == "encode" or action.lower() == "decode":
        message = input("Your message here: ")
        shift = int(input('Insert shift number: '))

        if action.lower() == "encode":
            encrypt(message, shift)
        elif action.lower() == "decode":
            decrypt(message, shift)

        display = "".join(coded_message)
        print(display)

        caeser_cypher()
    else:
        caeser_cypher()


def encrypt_shift(char_type, char, shift):
    """
    Takes the character type, the single character and shift number to encode
    """
    # encodes by adding shift number to the character index and taking the modulus off the
    # character type length
    new_char_index = (char_type.index(char) + shift) % len(char_type)

    if new_char_index < len(char_type):
        new_char = char_type[new_char_index]
    else:
        new_char_index -= len(char_type)
        new_char = char_type[new_char_index]
    coded_message.append(new_char)


def decrypt_shift(char_type, char, shift):
    """
    Takes the character type, the single character and shift number to decode
    """
    # encodes by subtracting shift number from the character index and taking the modulus off the
    # character type length
    new_char_index = (char_type.index(char) - shift) % len(char_type)
    if new_char_index >= 0:
        new_char = char_type[new_char_index]
    else:
        new_char_index += len(char_type)
        new_char = char_type[new_char_index]
    coded_message.append(new_char)


def special(char):
    new_char = char
    coded_message.append(new_char)


def encrypt(message, shift):
    """
    Takes the user's message and shift number, breaks them down into characters, check for th
    character type,encode the character based on character type using the encrypt_shift function
    and store them in the coded message
    list.
    """
    global coded_message
    coded_message = []
    message_char = list(message)
    for char in message_char:
        if char in letters:
            encrypt_shift(letters, char, shift)
        elif char in numbers:
            encrypt_shift(numbers, char, shift)
        elif char in symbols:
            encrypt_shift(symbols, char, shift)
        else:
            special(char)


def decrypt(message, shift):
    """
    Same as encrypt function, but we are now decrypting!!!
    """
    global coded_message
    coded_message = []
    message_char = list(message)
    for char in message_char:
        if char in letters:
            decrypt_shift(letters, char, shift)
        elif char in numbers:
            decrypt_shift(numbers, char, shift)
        elif char in symbols:
            decrypt_shift(symbols, char, shift)
        else:
            special(char)


caeser_cypher()
