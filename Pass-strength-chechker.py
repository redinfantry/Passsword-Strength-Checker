import re

def is_consecutive_numbers(password):
    for i in range(len(password) - 1):
        if password[i].isdigit() and password[i + 1].isdigit():
            return True
    return False

def is_valid_password(password, common_passwords):
    # Check for minimum length
    if len(password) < 13:
        return "Your password violates the password policy."

    # Check for at least one uppercase letter
    has_upper = any(c.isupper() for c in password)

    # Check for at least one lowercase letter
    has_lower = any(c.islower() for c in password)

    # Check for special characters using regex
    has_special = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};:\",.<>?]+', password))

    # Check for consecutive numbers
    has_consecutive_numbers = is_consecutive_numbers(password)

    # Check against common passwords
    if password in common_passwords:
        return "Your entered password is found in a breach password list, kindly change it accordingly."

    if has_upper and has_lower and has_special and not has_consecutive_numbers:
        return "Your Password is strong."

    return "Your password violates the password policy."

def main():
    common_passwords_path = input("Enter the path to the common passwords file: ")
    try:
        with open(common_passwords_path, 'r') as file:
            common_passwords = [line.strip() for line in file]
    except FileNotFoundError:
        common_passwords = []

    password = input("Enter a password: ")

    result_message = is_valid_password(password, common_passwords)
    print(result_message)

if __name__ == "__main__":
    main()
