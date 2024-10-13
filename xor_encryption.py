def xor_encrypt_decrypt(input_string, key):
    return ''.join(chr(ord(c) ^ key) for c in input_string)

def main():
    print("Welcome to the XOR Encryption/Decryption Tool")
    
    # Input the message to encrypt
    original_text = input("Enter the text to encrypt: ")
    key = int(input("Enter a numeric key for encryption (e.g., 123): "))
    
    # Encrypt the text
    encrypted_text = xor_encrypt_decrypt(original_text, key)
    print("\nEncrypted Text:", encrypted_text)

    # Provide the user with the encrypted text and the key to send to the recipient
    print("\nSend the following encrypted text and key to the recipient:")
    print(f"Encrypted Text: {encrypted_text}")
    print(f"Key: {key}")

    # Ask the recipient for the encrypted text and key to decrypt
    encrypted_input = input("\nEnter the encrypted text to decrypt: ")
    key_input = int(input("Enter the key used for encryption: "))

    # Decrypt the text
    decrypted_text = xor_encrypt_decrypt(encrypted_input, key_input)
    print("\nDecrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()
