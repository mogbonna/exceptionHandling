import getpass
import os

class UsernameAlreadyExists(Exception): pass
class InvalidUsernameOrPassword(Exception): pass

class PasswordTooShortError(Exception): pass
class MissingUppercaseError(Exception): pass
class MissingLowercaseError(Exception): pass
class MissingDigitError(Exception): pass
class MissingSpecialCharError(Exception): pass

def check_password_strength(password):
    if len(password) < 8:
        raise PasswordTooShortError("Password must be at least 8 characters.")
    if not any(c.isupper() for c in password):
        raise MissingUppercaseError("Include at least one UPPERCASE letter.")
    if not any(c.islower() for c in password):
        raise MissingLowercaseError("Include at least one lowercase letter.")
    if not any(c.isdigit() for c in password):
        raise MissingDigitError("Include at least one digit.")
    if not any(c in "!@#$%^&*()-_=+[]{}" for c in password):
        raise MissingSpecialCharError("Include at least one special character (!@#...).")
    return True

def load_users(filename="users.txt"):
    users = {}
    if os.path.exists(filename):
        with open(filename, "r") as f:
            for line in f:
                if ":" in line:
                    username, password = line.strip().split(":", 1)
                    users[username] = password
    return users

def save_user(username, password, filename="users.txt"):
    with open(filename, "a") as f:
        f.write(f"{username}:{password}\n")

users = load_users()

def register(username, password):
    if username in users:
        raise UsernameAlreadyExists("Username already taken.")
    
    check_password_strength(password)
    
    users[username] = password
    save_user(username, password)
    print("Registration successful.")

def login(username, password):
    if username not in users or users[username] != password:
        raise InvalidUsernameOrPassword("Invalid login credentials.")
    print("Login successful. Welcome,", username)

while True:
    try:
        print("\n=== User System ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            uname = input("Enter username: ")
            pwd = getpass.getpass("Enter password (input hidden): ")
            register(uname, pwd)

        elif choice == '2':
            uname = input("Enter username: ")
            pwd = getpass.getpass("Enter password (input hidden): ")
            login(uname, pwd)

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Choose 1–3.")

    except (UsernameAlreadyExists,
            PasswordTooShortError,
            MissingUppercaseError,
            MissingLowercaseError,
            MissingDigitError,
            MissingSpecialCharError) as e:
        print("Registration failed:", e)

    except InvalidUsernameOrPassword as ie:
        print("Login failed:", ie)

    except KeyboardInterrupt:
        print("\nProgram cancelled.")
        break

    finally:
        print("Action completed.\n")
