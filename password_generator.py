import string
import secrets


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for _ in range(length):
        password += secrets.choice(characters)

    return password


def main():
    print("\n===== PASSWORD GENERATOR =====")

    while True:
        try:
            length = int(input("Enter password length (minimum 8): "))

            if length < 8:
                print("Password length must be at least 8.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")


    password = generate_password(length)

    print("\nGenerated Password:")
    print(password)


if __name__ == "__main__":
    main()