def substitution_cipher(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            # Determine the case of the character
            start = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around using modulo 26
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            # If it's not a letter, leave it unchanged
            result += char
    
    return result

# Example usage
plaintext = "Hello, World!"
shift = 3
encrypted_text = substitution_cipher(plaintext, shift)
print("Encrypted:", encrypted_text)

decrypted_text = substitution_cipher(encrypted_text, -shift)
print("Decrypted:", decrypted_text)