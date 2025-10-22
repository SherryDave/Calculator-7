import re

def check_password_strength(password):
    """
    Checks if the password meets all the strength criteria.
    
    Parameters:
    password (str): The password to be checked.
    
    Returns:
    bool: True if the password is strong, False otherwise.
    """
    errors = []
    
    # Check for length
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")
    
    # Check for uppercase letter
    if not re.search("[A-Z]", password):
        errors.append("Password must contain at least one uppercase letter.")
    
    # Check for number
    if not re.search("[0-9]", password):
        errors.append("Password must contain at least one number.")
    
    # Check for special character
    if not re.search("[^A-Za-z0-9]", password):
        errors.append("Password must contain at least one special character (e.g., @, #, $).")
    
    if errors:
        print("Weak password. Here's what you need to improve:")
        for error in errors:
            print(f"- {error}")
        return False
    else:
        return True

def hint_for_password():
    print("\nHint for creating a strong password:")
    print("- Use a combination of uppercase and lowercase letters.")
    print("- Include at least one number.")
    print("- Add a special character like @, #, or $.")
    print("- Make sure it's at least 8 characters long.")
    print("- Avoid using easily guessable information like your name or birthdate.")

def main():
    print("Welcome to the Password Strength Checker!")
    print("You have up to three attempts to enter a strong password.")
    
    hint_for_password()
    
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        password = input("\nEnter your password: ")
        
        if check_password_strength(password):
            print("Password is strong.")
            print("Password accepted.")
            break
        else:
            print("Try again!")
            attempts += 1
            if attempts < max_attempts:
                print("Remember to fix the issues mentioned earlier.")
    else:
        print("Too many failed attempts. Try again later.")

if __name__ == "__main__":
    main()
