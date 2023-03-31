def is_password_valid(password):
    if len(password) >= 6 and password.isdigit():
        print('Password is valid')
    else:
        print('Password in not valid')

