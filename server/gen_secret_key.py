import random

def create_secret_key():
    ascii_chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    return ''.join([random.SystemRandom().choice(ascii_chars) for i in range(50)])

if __name__ == '__main__':
    print(create_secret_key())
