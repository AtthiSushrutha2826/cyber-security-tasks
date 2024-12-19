from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    try:
        # Open the image
        img = Image.open(input_path)
        img_array = np.array(img)

        # Encrypt by applying a simple mathematical operation
        encrypted_array = (img_array + key) % 256  # Ensure values stay in range (0-255)

        # Convert back to image and save
        encrypted_img = Image.fromarray(np.uint8(encrypted_array))
        encrypted_img.save(output_path)
        print(f"Image encrypted and saved as {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def decrypt_image(input_path, output_path, key):
    try:
        # Open the image
        img = Image.open(input_path)
        img_array = np.array(img)

        # Decrypt by reversing the mathematical operation
        decrypted_array = (img_array - key) % 256  # Ensure values stay in range (0-255)

        # Convert back to image and save
        decrypted_img = Image.fromarray(np.uint8(decrypted_array))
        decrypted_img.save(output_path)
        print(f"Image decrypted and saved as {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Image Encryption Tool")
    while True:
        print("\n1. Encrypt an image")
        print("2. Decrypt an image")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            input_path = input("Enter the path of the image to encrypt: ")
            output_path = input("Enter the path to save the encrypted image: ")
            key = int(input("Enter the encryption key (integer): "))
            encrypt_image(input_path, output_path, key)

        elif choice == '2':
            input_path = input("Enter the path of the encrypted image: ")
            output_path = input("Enter the path to save the decrypted image: ")
            key = int(input("Enter the decryption key (integer): "))
            decrypt_image(input_path, output_path, key)

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
