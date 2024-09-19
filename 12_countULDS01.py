# Count uppercase, lowercase, digits andspecial characters from the given string and arrange:

s1 = "Khushnood1234567723@#$$$$&#$^CATDDU"
U = []  # Uppercase letters
L = []  # Lowercase letters
D = []  # Digits
S = []  # Special characters

for i in s1:
    if ord(i) in range(65, 91):  # Correct ASCII range for uppercase A-Z
        U.append(i)
    elif ord(i) in range(97, 123):  # Correct ASCII range for lowercase a-z
        L.append(i)
    elif ord(i) in range(48, 58):  # Correct ASCII range for digits 0-9
        D.append(i)
    else:
        S.append(i)  # Append special characters

# Combine the lists and convert to a single string


result = ''.join(U + L + D + S)
print("Result:", result)
