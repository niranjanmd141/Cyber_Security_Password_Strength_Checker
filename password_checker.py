import re

def check_password_strength(password):
    """
    Checks the strength of a given password based on several criteria.
    Returns a string indicating the strength level.
    """
    score = 0
    feedback = []

    # Criteria 1: Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Criteria 2: Uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Password should include uppercase letters.")

    # Criteria 3: Lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password should include lowercase letters.")

    # Criteria 4: Numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Password should include numbers.")

    # Criteria 5: Special characters
    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?`~]", password):
        score += 1
    else:
        feedback.append("Password should include special characters (e.g., !@#$%^&*).")

    # Assess strength based on score
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 1 or score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak" # For passwords failing most or all criteria

    return strength, feedback

def main():
    print("--- Password Strength Checker ---")
    while True:
        password = input("Enter a password to check (or 'quit' to exit): ")
        if password.lower() == 'quit':
            break
        
        strength, feedback = check_password_strength(password)
        print(f"\nPassword: {password}")
        print(f"Strength: {strength}")
        if feedback:
            print("Suggestions to improve:")
            for item in feedback:
                print(f"- {item}")
        print("-" * 30)

if __name__ == "__main__":
    main()