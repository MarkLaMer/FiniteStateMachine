Email Validation Machine  
--------------------------------  

**Overview**
This program provides a function to validate email addresses based on a finite state machine approach. It checks whether an email follows the correct structure, including a valid local part, an @ symbol, and a properly formatted domain.

**Features**
- Ensures the local part contains only letters, dots (.), dashes (-), and underscores (_).
- Verifies that the domain starts with a letter and contains at least one dot (.).
- Prevents invalid cases, such as consecutive dots in the domain or missing local parts.
- Includes a test suite with various email validation scenarios.

**Purpose**  
Validate email addresses using a state machine. Ensures:  
- Local part (before @) allows letters, dots (.), hyphens (-), underscores (_).  
- Domain part (after @) must have at least one dot (e.g., "example.com").  
- Domain cannot start/end with a dot or have consecutive dots (e.g., "domain..com").  
- Only one "@" allowed.  

**States**  
- START: Checks the validity of the first character.  
- LOCAL_PART: The local part of the email before "@".  
- DOMAIN_START: Domain starts with a letter after "@".  
- DOMAIN_LABEL: Validates letters in the domain before a dot.  
- DOMAIN_DOT: Requires a letter after a dot (e.g., ".com").  
- DOMAIN_LABEL_AFTER_DOT: Final valid state (e.g., "com" in "example.com").  

**Usage**  
1. Add test cases to the `test_cases` list in the script.
2. Run the script. Results will print automatically.  
