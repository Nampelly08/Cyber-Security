"""
Caesar Cipher Implementation
Author: Ashritha

Features:
- Encryption and Decryption
- Supports positive and negative shift values
- Preserves uppercase and lowercase letters
- Keeps numbers, spaces, and symbols unchanged
"""

def caesar_cipher(text, shift, mode="encrypt"):
    result = ""

    # Normalize shift value
    shift = shift % 26

    if mode.lower() == "decrypt":
        shift = -shift

    for ch in text:

        if ch.isupper():
            new_char = chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            result += new_char

        elif ch.islower():
            new_char = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
            result += new_char

        else:
            result += ch

    return result


def get_shift():
    while True:
        try:
            return int(input("Enter Shift Key: "))
        except ValueError:
            print("Please enter a valid integer.")


def menu():

    print("=" * 40)
    print("        Caesar Cipher Program")
    print("=" * 40)
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    while True:

        choice = input("\nChoose an option: ")

        if choice == "1":
            text = input("Enter Plain Text : ")
            shift = get_shift()

            encrypted = caesar_cipher(text, shift, "encrypt")

            print("\nEncrypted Text:")
            print(encrypted)

        elif choice == "2":
            text = input("Enter Cipher Text: ")
            shift = get_shift()

            decrypted = caesar_cipher(text, shift, "decrypt")

            print("\nDecrypted Text:")
            print(decrypted)

        elif choice == "3":
            print("\nProgram Closed.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    menu()
