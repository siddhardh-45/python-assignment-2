# Student Registration Validator

Validates student registration inputs: Student ID, Email, Password, and Referral Code.  

**Rules:**  
- Student ID: `CSE-XXX` (digits)  
- Email: contains `@` and `.`, ends with `.edu`  
- Password: ≥8 chars, starts with uppercase, contains a digit  
- Referral Code: `REF` + 2 digits + `@`  

**Output:**  
- `APPROVED` if all valid  
- `REJECTED` if any invalid  
