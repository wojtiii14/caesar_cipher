alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet_capitals = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def encrypt(phrase):

    encrypted_phrase = ''

    for letter in phrase:
        if letter in alphabet:

            x = alphabet.index(letter) + 3

            if x == 26:
                x = 0
            elif x == 27:
                x = 1
            elif x == 28:
                x = 2

            # print(alphabet[x])

            encrypted_phrase = encrypted_phrase + alphabet[x]
        
        elif letter in alphabet_capitals:

            x = alphabet_capitals.index(letter) + 3

            if x == 26:
                x = 0
            elif x == 27:
                x = 1
            elif x == 28:
                x = 2

            # print(alphabet[x])

            encrypted_phrase = encrypted_phrase + alphabet_capitals[x]


        elif letter in numbers:

            number = int(letter) + 3

            if number == 10:
                number = 0
            elif number == 11:
                number = 1
            elif number == 12:
                number = 2

            encrypted_phrase = encrypted_phrase + str(number)

        else:

            encrypted_phrase = encrypted_phrase + letter

    return encrypted_phrase

def decrypt(phrase):

    decrypted_phrase = ''

    for letter in phrase:
        if letter in alphabet:

            x = alphabet.index(letter) - 3

            if x == -3:
                x = 23
            elif x == -2:
                x = 24
            elif x == -1:
                x = 25

            # print(alphabet[x])

            decrypted_phrase = decrypted_phrase + alphabet[x]
        
        elif letter in alphabet_capitals:

            x = alphabet_capitals.index(letter) - 3

            if x == -3:
                x = 23
            elif x == -2:
                x = 24
            elif x == -1:
                x = 25

            # print(alphabet[x])

            decrypted_phrase = decrypted_phrase + alphabet_capitals[x]


        elif letter in numbers:

            number = int(letter) - 3

            if number == -1:
                number = 9
            elif number == -2:
                number = 8
            elif number == -3:
                number = 7

            decrypted_phrase = decrypted_phrase + str(number)

        else:

            decrypted_phrase = decrypted_phrase + letter

    return decrypted_phrase

phrase = input("Type your phrase: ")

x = encrypt(phrase)

print(x)

x = decrypt(x)

print(x)