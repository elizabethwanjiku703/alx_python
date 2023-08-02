# 6. Password Validation Function
def validate_password(password):
    if len(password) < 8:
        return False

# We check uppercase, lowercase, and digits of the password
    is_uppercase = False
    is_lowercase = False
    has_digit = False
    for char in password:
        if char.isupper():
            is_uppercase = True
        elif char.islower():
            is_lowercase = True
        elif char.isdigit():
            has_digit = True

    if not (is_uppercase and is_lowercase and has_digit):
        return False

# We check spacing
    if ' ' in password:
        return False
    return True
