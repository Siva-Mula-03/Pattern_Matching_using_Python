import re

def validate_credit_card_number():
    cc_num = input("Enter your credit card number: ")
    cc_num_regex = re.compile(r'^\d{4}-\d{4}-\d{4}-\d{4}$')
    if cc_num_regex.search(cc_num):
        print("Valid credit card number")
        print()
    else:
        print("Invalid credit card number")
        print()

def validate_pan_number():
    pan_num = input("Enter your PAN number: ")
    pan_num_regex = re.compile(r'^[A-Z][A-Z]{4}[0-9]{4}[A-Z]$')
    if pan_num_regex.search(pan_num):
        print("Valid PAN number")
        print()
    else:
        print("Invalid PAN number")
        print()

def validate_password():
    password = input("Enter your password: ")
    password_regex = re.compile(
        r'^[a-zA-Z]([a-z]{3,4}|[A-Z]{3,4})[@\$#\!%_\.]{1}[0-9]{2,3}$')
    if password_regex.search(password):
        print("Valid password")
        print()
    else:
        print("Invalid password")
        print()

def main():
    print("1. Validate credit card number")
    print("2. Validate PAN number")
    print("3. Validate password")
    choice = input("Enter your choice: ")

    if choice == '1':
        validate_credit_card_number()
    elif choice == '2':
        validate_pan_number()
    elif choice == '3':
        validate_password()
    else:
        print("Invalid choice")

if __name__ == '__main__':
    main()
