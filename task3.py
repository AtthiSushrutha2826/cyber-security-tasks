import re

def check_password_strength(password):
    # Initialize strength levels and feedback
    strength = 0
    feedback = []

    # Check length of the password
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    # Check for numbers
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one number.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character.")

    # Determine password strength
    if strength == 5:
        return "Strong password!", []
    elif 3 <= strength < 5:
        return "Moderate password. Consider improving it:", feedback
    else:
        return "Weak password. Needs significant improvement:", feedback

# Main program
if __name__ == "__main__":
    print("Welcome to the Password Complexity Checker!")
    password = input("Enter a password to check its strength: ")
    result, feedback = check_password_strength(password)
    print("\n" + result)
    for item in feedback:
        print("- " + item)
