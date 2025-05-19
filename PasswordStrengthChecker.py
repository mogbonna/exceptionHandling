class PasswordTooShortError(Exception): pass
class MissingUppercaseError(Exception): pass
class MissingLowercaseError(Exception): pass
class MissingDigitError(Exception): pass
class MissingSpecialCharError(Exception): pass

def check_password_strength(password):
    if len(password) < 8:
        raise PasswordTooShortError("Password must be at least 8 characters.")
    if not any(c.isupper() for c in password):
        raise MissingUppercaseError("Password must include an uppercase letter.")
    if not any(c.islower() for c in password):
        raise MissingLowercaseError("Password must include a lowercase letter.")
    if not any(c.isdigit() for c in password):
        raise MissingDigitError("Password must include a digit.")
    if not any(c in "!@#$%^&*()_+-=" for c in password):
        raise MissingSpecialCharError("Password must include a special character.")
    return True

try:
    pwd = input("Enter a password to check: ")
    if check_password_strength(pwd):
        print("Password is strong!")

except (PasswordTooShortError,
        MissingUppercaseError,
        MissingLowercaseError,
        MissingDigitError,
        MissingSpecialCharError) as e:
    print("Weak password:", e)

except KeyboardInterrupt:
    print("\nPassword check cancelled by user.")

finally:
    print("Password check complete.")
