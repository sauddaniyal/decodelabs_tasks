import string
import secrets


def generate_password(length):
    character_pool = string.ascii_letters + string.digits  # a-z, A-Z, 0-9

    chosen_chars = [secrets.choice(character_pool) for _ in range(length)]
    return "".join(chosen_chars)

def main():
    print("=== Random Password Generator ===")

    while True:
        raw_length = input("Enter desired password length: ").strip()
        try:
            length = int(raw_length)
        except ValueError:
            print("  Invalid input — please enter a whole number.\n")
            continue

        if length < 1:
            print("  Length must be at least 1.\n")
            continue

        break

    password = generate_password(length)
    print(f"\nGenerated Password:\n {password}")

if __name__ == "__main__":
    main()