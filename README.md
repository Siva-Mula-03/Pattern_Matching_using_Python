# Pattern_Matching_using_Python

Pattern matching with regular expression with python
Write a Python program that accepts a credit card number, PAN number, and a password from
the user and validates it using regular expressions. You may refer to the provided document –
‘Pattern matching with python.pdf’ to understand how to perform pattern matching with regular
expressions. Make sure your program checks for below validations. (Students are advised not
to
experiment and share with their original credit card or PAN numbers)
Validations for credit card number- (Example- 1234-5678-9876-4324)
1. It should begin with a number and end with a number (not with letter/symbol).
2. It should contain ‘ - ’ symbol after each 4 digits.
3. The total length of the entered digits must not exceed 16 digits.
Validations for PAN number- (Example- ABCTY1234D)
1. It should begin with a letter followed by exact 4 subsequent letters.
2. After 5 letters, it should accept 4 numbers.
3. The PAN number must end with the letter.
4. All letters must be in uppercase.
5. The total length of the input (letters/symbols) must not exceed 10 alphanumeric inputs.
Validations for password1. It should begin with single letter followed by exactly three or four uppercase/lowercase
letters.
2. After the letters, it should only accept any one of these special symbols – ‘@’, ‘$’, ‘_’, ‘#’,
‘!’, ‘%’, ‘.’.
3. After the special symbol, it should accept exactly two or three digits.
In the explanation video, you will need to discuss your regular expression logic and demonstrate
your program execution with at least one valid and one invalid input.
