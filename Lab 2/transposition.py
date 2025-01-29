def transposition_cipher(text, key):
    # Calculate the number of rows needed
    rows = (len(text) // key) + (1 if len(text) % key != 0 else 0)
    
    # Create a grid (list of lists) to hold the text
    grid = [['' for _ in range(key)] for _ in range(rows)]
    
    # Fill the grid row-wise
    index = 0
    for row in range(rows):
        for col in range(key):
            if index < len(text):
                grid[row][col] = text[index]
                index += 1
    
    # Read the grid column-wise to create the ciphertext
    ciphertext = ''
    for col in range(key):
        for row in range(rows):
            ciphertext += grid[row][col]
    
    return ciphertext

# Example usage
plaintext = "Hello, World!"
key = 4
encrypted_text = transposition_cipher(plaintext, key)
print("Encrypted:", encrypted_text)