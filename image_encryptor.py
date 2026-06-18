from PIL import Image


def encrypt_image(image_path, key):
    try:
        # Remove accidental quotes and spaces
        image_path = image_path.strip().replace('"', '')

        # Convert image to RGB
        img = Image.open(image_path).convert("RGB")

        pixels = img.load()
        width, height = img.size

        for x in range(width):
            for y in range(height):

                r, g, b = pixels[x, y]

                pixels[x, y] = (
                    (r + key) % 256,
                    (g + key) % 256,
                    (b + key) % 256
                )

        output_file = "encrypted_image.png"
        img.save(output_file)

        print("\n✅ Image Encrypted Successfully!")
        print(f"Saved as: {output_file}")

    except Exception as e:
        print("\n❌ Error:", e)


def decrypt_image(image_path, key):
    try:
        # Remove accidental quotes and spaces
        image_path = image_path.strip().replace('"', '')

        # Convert image to RGB
        img = Image.open(image_path).convert("RGB")

        pixels = img.load()
        width, height = img.size

        for x in range(width):
            for y in range(height):

                r, g, b = pixels[x, y]

                pixels[x, y] = (
                    (r - key) % 256,
                    (g - key) % 256,
                    (b - key) % 256
                )

        output_file = "decrypted_image.png"
        img.save(output_file)

        print("\n✅ Image Decrypted Successfully!")
        print(f"Saved as: {output_file}")

    except Exception as e:
        print("\n❌ Error:", e)


def main():

    print("=" * 50)
    print("      IMAGE ENCRYPTION TOOL")
    print("=" * 50)

    while True:

        print("\n1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":

            image_path = input("Enter image path: ")
            key = int(input("Enter secret key (0-255): "))

            encrypt_image(image_path, key)

        elif choice == "2":

            image_path = input("Enter encrypted image path: ")
            key = int(input("Enter the same secret key: "))

            decrypt_image(image_path, key)

        elif choice == "3":

            print("\nThank you for using the program.")
            break

        else:

            print("\n❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()