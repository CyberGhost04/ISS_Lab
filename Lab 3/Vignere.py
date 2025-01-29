def vigenere_cipher(text, key, mode='encrypt'):
    result = ""
    key_length = len(key)
    key = key.upper()  # Convert key to uppercase for consistency

    for i, char in enumerate(text):
        if char.isalpha():
            # Determine the shift value for the current character
            key_char = key[i % key_length]
            shift = ord(key_char) - ord('A')

            if mode == 'decrypt':
                shift = -shift  # Reverse the shift for decryption

            # Preserve the case of the original character
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            # If it's not a letter, leave it unchanged
            result += char

    return result

# Example usage
plaintext = "Hello, World!"
key = "KEY"

# Encryption
encrypted_text = vigenere_cipher(plaintext, key, mode='encrypt')
print("Encrypted:", encrypted_text)

# Decryption
decrypted_text = vigenere_cipher(encrypted_text, key, mode='decrypt')
print("Decrypted:", decrypted_text)