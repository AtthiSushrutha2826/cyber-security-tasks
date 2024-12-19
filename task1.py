def caesar_cipher(text, shift, mode):
    result = ""
    shift = shift % 26  # Ensure the shift is within the range of 0-25
    
    if mode == "decrypt":
        shift = -shift  # Reverse the shift for decryption

    for char in text:
        if char.isalpha():  # Check if the character is a letter
            base = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around using modulo
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Non-alphabetic characters remain unchanged
    
    return result

def main():
    print("Caesar Cipher Program")
    while True:
        print("\n1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            text = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted = caesar_cipher(text, shift, "encrypt")
            print(f"Encrypted message: {encrypted}")

        elif choice == '2':
            text = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted = caesar_cipher(text, shift, "decrypt")
            print(f"Decrypted message: {decrypted}")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
