import sys
import os
import re

# -------------------------
# Custom Exceptions
# -------------------------
class UserAlreadyExistsError(Exception): pass
class UserNotFoundError(Exception): pass
class InvalidPasswordError(Exception): pass
class WeakPasswordError(Exception): pass

# -------------------------
# Password Strength Checker
# -------------------------
def is_strong_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r"[A-Z]", password):
        return False, "Password must include at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return False, "Password must include at least one lowercase letter."
    if not re.search(r"\d", password):
        return False, "Password must include at least one digit."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must include at least one special character."
    return True, ""

# -------------------------
# Password Input with '*' Masking
# -------------------------
def input_password(prompt='Password: '):
    print(prompt, end='', flush=True)
    password = ''
    
    try:
        # For Windows
        import msvcrt
        while True:
            ch = msvcrt.getch()
            if ch in {b'\r', b'\n'}:
                print()
                break
            elif ch == b'\x08':  # Backspace
                if len(password) > 0:
                    password = password[:-1]
                    sys.stdout.write('\b \b')
            elif ch == b'\x03':  # Ctrl+C
                raise KeyboardInterrupt
            else:
                try:
                    char = ch.decode()
                    password += char
                    sys.stdout.write('*')
                except:
                    continue
    except ImportError:
        # For Linux/macOS
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            while True:
                ch = sys.stdin.read(1)
                if ch in {'\r', '\n'}:
                    print()
                    break
                elif ch == '\x7f':  # Backspace
                    if len(password) > 0:
                        password = password[:-1]
                        sys.stdout.write('\b \b')
                elif ch == '\x03':  # Ctrl+C
                    raise KeyboardInterrupt
                else:
                    password += ch
                    sys.stdout.write('*')
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return password

# -------------------------
# User Data Functions
# -------------------------
def load_users():
    users = {}
    if os.path.exists("users.txt"):
        with open("users.txt", "r") as f:
            for line in f:
                if ":" in line:
                    username, password = line.strip().split(":")
                    users[username] = password
    return users

def save_user(username, password):
    with open("users.txt", "a") as f:
        f.write(f"{username}:{password}\n")

# -------------------------
# Registration
# -------------------------
def register():
    users = load_users()
    username = input("Choose a username: ")
    if username in users:
        raise UserAlreadyExistsError("Username already exists.")

    while True:
        password = input_password("Choose a strong password: ")
        valid, message = is_strong_password(password)
        if valid:
            break
        else:
            print("❌ Weak password:", message)

    save_user(username, password)
    print("✅ Registration successful!")

# -------------------------
# Login
# -------------------------
def login():
    users = load_users()
    username = input("Enter username: ")
    if username not in users:
        raise UserNotFoundError("User not found.")
    password = input_password("Enter password: ")
    if users[username] != password:
        raise InvalidPasswordError("Incorrect password.")
    print(f"✅ Welcome, {username}!")

# -------------------------
# Main Menu
# -------------------------
while True:
    try:
        print("\n🔐 Login & Registration System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        option = input("Choose an option: ")

        if option == '1':
            register()
        elif option == '2':
            login()
        elif option == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

    except (UserAlreadyExistsError, UserNotFoundError, InvalidPasswordError, WeakPasswordError) as e:
        print("❌", e)

    except KeyboardInterrupt:
        print("\nProgram interrupted.")
        break

    finally:
        print("Action completed.\n")
