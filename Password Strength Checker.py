import re

def check_password_strength(password):
    score = 0
    
    if len(password) >= 8:
        score += 2
    if re.search(r"[A-Z]", password):
        score += 2
    if re.search(r"[a-z]", password):
        score += 2
    if re.search(r"[0-9]", password):
        score += 2
    if re.search(r"[!@#$%^&*]", password):
        score += 2

    if score <= 4:
        return "Weak"
    elif score <= 7:
        return "Medium"
    else:
        return "Strong"

while True:
    password = input("Enter a password (or type 'exit'): ")
    
    if password.lower() == "exit":
        break

    strength = check_password_strength(password)
    print(f"Password Strength: {strength}\n")