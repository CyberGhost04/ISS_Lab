def rail_fence_encrypt(plaintext):

    row1 = plaintext[::2]  # Characters at even indices
    row2 = plaintext[1::2]  # Characters at odd indices

    ciphertext = row1 + row2
    return ciphertext

def rail_fence_decrypt(ciphertext):
    # Determine the length of each row
    length = len(ciphertext)
    half_length = (length + 1) // 2

    row1 = ciphertext[:half_length]
    row2 = ciphertext[half_length:]

    plaintext = []
    for i in range(half_length):
        plaintext.append(row1[i])
        if i < len(row2):
            plaintext.append(row2[i])
    return ''.join(plaintext)

# Example usage
plaintext = "HELLO WORLD"
ciphertext = rail_fence_encrypt(plaintext)
print("Encrypted:", ciphertext)

decrypted_text = rail_fence_decrypt(ciphertext)
print("Decrypted:", decrypted_text)