def prepare_text(text):
    # Remove non-alphabetic characters and convert to uppercase
    text = ''.join([char.upper() for char in text if char.isalpha()])
    # Replace 'J' with 'I' (standard Playfair rule)
    text = text.replace("J", "I")
    # Add an 'X' between repeated letters and at the end if the length is odd
    i = 0
    while i < len(text) - 1:
        if text[i] == text[i + 1]:
            text = text[:i + 1] + "X" + text[i + 1:]
        i += 2
    if len(text) % 2 != 0:
        text += "X"
    return text

def create_key_matrix(key):
    # Remove duplicate letters from the key and convert to uppercase
    key = ''.join([char.upper() for char in key if char.isalpha()])
    key = key.replace("J", "I")
    key = ''.join(dict.fromkeys(key))  # Remove duplicates
    # Fill the rest of the matrix with the remaining letters
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in key:
            key += char
    # Create a 5x5 matrix
    matrix = [list(key[i:i + 5]) for i in range(0, 25, 5)]
    return matrix

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def playfair_cipher(text, key, mode='encrypt'):
    # Prepare the text and create the key matrix
    text = prepare_text(text)
    matrix = create_key_matrix(key)
    result = ""

    # Process the text in digraphs (pairs of two letters)
    for i in range(0, len(text), 2):
        char1, char2 = text[i], text[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        # Same row: shift right (encrypt) or left (decrypt)
        if row1 == row2:
            result += matrix[row1][(col1 + (1 if mode == 'encrypt' else -1)) % 5]
            result += matrix[row2][(col2 + (1 if mode == 'encrypt' else -1)) % 5]
        # Same column: shift down (encrypt) or up (decrypt)
        elif col1 == col2:
            result += matrix[(row1 + (1 if mode == 'encrypt' else -1)) % 5][col1]
            result += matrix[(row2 + (1 if mode == 'encrypt' else -1)) % 5][col2]
        # Rectangle: swap columns
        else:
            result += matrix[row1][col2]
            result += matrix[row2][col1]

    # Restore the original case of the text
    final_result = []
    index = 0
    for char in text:
        if char.isalpha():
            if text[index].isupper():
                final_result.append(result[index].upper())
            else:
                final_result.append(result[index].lower())
            index += 1
        else:
            final_result.append(char)
    return ''.join(final_result)

# Example usage
plaintext = "Hello, World!"
key = "PLAYFAIR"

# Encryption
encrypted_text = playfair_cipher(plaintext, key, mode='encrypt')
print("Encrypted:", encrypted_text)

# Decryption
decrypted_text = playfair_cipher(encrypted_text, key, mode='decrypt')
print("Decrypted:", decrypted_text)