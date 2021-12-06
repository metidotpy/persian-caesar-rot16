from persian_alphabet import PERSIAN_ALPHABET, PERSIAN_NUMBERS

class Encrypt:
    def caesar(self, text):
        caesar_encrypted = ''
        for char in text:
            if char == 'ن':
                encrypted_char = 'ا'
            elif char == 'و':
                encrypted_char = 'ب'
            elif char == 'ه':
                encrypted_char = 'پ'
            elif char == 'ی':
                encrypted_char = 'ت'
            elif char in PERSIAN_ALPHABET:
                encrypted_char = PERSIAN_ALPHABET[PERSIAN_ALPHABET.index(char) + 4]
            elif char in PERSIAN_NUMBERS:
                encrypted_char = PERSIAN_NUMBERS[char]
            else:
                encrypted_char = char
            caesar_encrypted += encrypted_char
        return caesar_encrypted
    def rot16(self, text):
        rot16_encrypted = ''
        for char in text:
            if char in PERSIAN_ALPHABET[0:16]:
                encrypted_char = PERSIAN_ALPHABET[PERSIAN_ALPHABET.index(char) + 16]
            elif char in PERSIAN_ALPHABET[16:31]:
                encrypted_char = PERSIAN_ALPHABET[PERSIAN_ALPHABET.index(char) - 16]
            elif char in PERSIAN_NUMBERS:
                encrypted_char = PERSIAN_NUMBERS[char]
            else:
                encrypted_char = char
            rot16_encrypted += encrypted_char
        return rot16_encrypted


class Decrypt:
    def caesar(self, text):
        caesar_decrypted = ''
        for char in text:
            if char == 'ا':
                decrypted_char = 'ن'
            elif char == 'ب':
                decrypted_char = 'و'
            elif char == 'پ':
                decrypted_char = 'ه'
            elif char == 'ت':
                decrypted_char = 'ی'
            elif char in PERSIAN_ALPHABET:
                decrypted_char = PERSIAN_ALPHABET[PERSIAN_ALPHABET.index(char) - 4]
            elif char in PERSIAN_NUMBERS:
                decrypted_char = PERSIAN_NUMBERS[char]
            else:
                decrypted_char = char
            caesar_decrypted += decrypted_char
        return caesar_decrypted
    
    def rot16(self, text):
        rot16_decrypted = ''
        for char in text:
            if char in PERSIAN_ALPHABET[0:16]:
                decrypted_char = PERSIAN_ALPHABET[PERSIAN_ALPHABET.index(char) + 16]
            elif char in PERSIAN_ALPHABET[16:31]:
                decrypted_char = PERSIAN_ALPHABET[PERSIAN_ALPHABET.index(char) - 16]
            elif char in PERSIAN_NUMBERS:
                decrypted_char = PERSIAN_NUMBERS[char]
            else:
                decrypted_char = char
            rot16_decrypted += decrypted_char
        return rot16_decrypted