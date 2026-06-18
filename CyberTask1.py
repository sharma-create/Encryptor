def encrypt(message, shift):
    encrypted = ""

    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted += new_char
        else:
            encrypted += char

    return encrypted


def decrypt(message, shift):
    decrypted = ""

    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base - shift) % 26 + base)
            decrypted += new_char
        else:
            decrypted += char

    return decrypted


print("===== Caesar Cipher =====")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter your choice (1/2): ")

message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

if choice == "1":
    result = encrypt(message, shift)
    print("Encrypted Message:", result)

elif choice == "2":
    result = decrypt(message, shift)
    print("Decrypted Message:", result)

else:
    print("Invalid choice! Please enter 1 or 2.")