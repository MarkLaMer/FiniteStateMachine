def is_valid_email(email):
    current_state = 'local_start'
    domain_has_dot = False

    for char in email:
        if current_state == 'local_start':
            if char.isalpha() or char in ['.', '-', '_']:
                current_state = 'local_part'
            else:
                return False
        elif current_state == 'local_part':
            if char == '@':
                current_state = 'domain_start'
            elif char.isalpha() or char in ['.', '-', '_']:
                pass  # Remain in local_part
            else:
                return False
        elif current_state == 'domain_start':
            if char.isalpha():
                current_state = 'domain_label'
            else:
                return False
        elif current_state == 'domain_label':
            if char == '.':
                current_state = 'domain_dot'
                domain_has_dot = True
            elif char.isalpha():
                pass  # Remain in domain_label
            else:
                return False
        elif current_state == 'domain_dot':
            if char.isalpha():
                current_state = 'domain_label'
            else:
                return False
        else:
            return False

    return current_state == 'domain_label' and domain_has_dot

# Test suite
test_cases = [
    ("user@example.com", True),
    ("user.name@example.com", True),
    ("user-name@example.com", True),
    ("user_name@example.com", True),
    ("user@example", False),          # No dot in domain
    ("user@example..com", False),     # Consecutive dots in domain
    ("user@.example.com", False),     # Domain starts with dot
    ("@example.com", False),          # Missing local part
    ("user@domain.c", True),          # Valid single-letter domain part after dot
    ("user@domain.co.uk", True),      # Multiple dots in domain
]

for email, expected in test_cases:
    result = is_valid_email(email)
    assert result == expected, f"Failed for {email}: expected {expected}, got {result}"

print("All tests passed!")
