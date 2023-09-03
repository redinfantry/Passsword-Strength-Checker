# Passsword-Strength-Checker

This is a simple Python program for checking the strength of passwords. It includes features like avoiding consecutive numbers, using special characters, requiring at least one capital letter and one small letter, and having a minimum length of 13 characters. Additionally, it allows you to check if the entered password is in a list of common passwords from a text file.

## Features

- Checks password strength based on the following criteria:
  - Minimum length of 13 characters.
  - At least one uppercase letter.
  - At least one lowercase letter.
  - Special characters (e.g., !@#$%^&*()_+-=[]{};:',.<>?).
  - No consecutive numbers (e.g., "123" is not allowed).

- Utilizes a list of common passwords from a text file to check against common passwords.
- Customized error messages for different password conditions.
- User-friendly and easy to use.

## Dependencies

This program has no external dependencies and uses Python's built-in libraries for its functionality.

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/password-strength-checker.git
