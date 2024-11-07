import re

# Function to assess password strength
def assess_password_strength(password, allowed_special_chars):
    score = 0
    suggestions = []
    
    # Check password length
    if len(password) >= 12:
        score += 1
    elif len(password) >= 8:
        score += 0.5
        suggestions.append("Consider increasing the length of your password to at least 12 characters for a stronger password.")
    
    # Check for uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Include at least one uppercase letter.")
    
    # Check for lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Include at least one lowercase letter.")
    
    # Check for digits
    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Include at least one number.")
    
    # Check for special characters
    if re.search(f"[{re.escape(allowed_special_chars)}]", password):
        score += 1
    else:
        suggestions.append(f"Include at least one special character from the allowed set: {allowed_special_chars}")
    
    # Provide feedback based on the score
    if score == 5:
        return "Strong password", suggestions
    elif score == 4:
        return "Moderate password", suggestions
    else:
        return "Weak password", suggestions

# User input for password and allowed special characters
user_password = input("Enter your password: ")
allowed_special_chars = input("Enter allowed special characters (e.g., !@#$%^&*): ")

# Get the password strength assessment
strength, feedback = assess_password_strength(user_password, allowed_special_chars)

# Print the feedback
print(strength)
if feedback:
    for suggestion in feedback:
        print(f"- {suggestion}")

# If password is weak or moderate, ask the user to try again
while strength != "Strong password":
    print("\nPlease enter a stronger password.")
    user_password = input("Enter your new password: ")
    strength, feedback = assess_password_strength(user_password, allowed_special_chars)
    print(strength)
    if feedback:
        for suggestion in feedback:
            print(f"- {suggestion}")
