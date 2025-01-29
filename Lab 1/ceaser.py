def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

# Example usage
plaintext = "Hello, World!"
shift = 3

encrypted_text = caesar_cipher(plaintext, shift)
print("Encrypted:", encrypted_text)

# To decrypt, use the negative of the shift value
decrypted_text = caesar_cipher(encrypted_text, -shift)
print("Decrypted:", decrypted_text)
