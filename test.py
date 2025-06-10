import json, os
from cryptography.fernet import Fernet

def load_or_generate_key():
    if not os.path.exists('key.key'):
        key = Fernet.generate_key()
        with open('key.key', 'wb') as file_key:
            file_key.write(key)
    with open('key.key', 'rb') as file_key:
        return file_key.read()

def load_data():
    try:
        key = load_or_generate_key()
        f = Fernet(key)
        with open('data.enc', 'rb') as data_file:
            encrypted = data_file.read()
        decrypted = f.decrypt(encrypted).decode()
        return json.loads(decrypted)
    except FileNotFoundError:
        return {}
    except Exception as e:
        print('Error Decrypting file:', e)
        return {}

def save_data(data):
    key = load_or_generate_key()
    f = Fernet(key)
    json_data = json.dumps(data).encode() 
    encrypted = f.encrypt(json_data)
    with open('data.enc', 'wb') as data_file:
        data_file.write(encrypted)

def save_password(data):
    site = input('Enter Website: ').strip().lower()
    username = input('Enter username: ')
    password = input('Enter password: ')
    data[site] = {"username": username, "password": password}
    save_data(data)
    print('Password is saved.')

def get_password(data):
    site = input('Enter the Website\'s name to search: ').strip().lower()
    if site in data:
        creds = data[site]
        print(f'Website: {site}')
        print(f'Username: {creds['username']}')
        print(f'Password: {creds['password']}')
    else:
        print('No Passwords found.')

data = load_data()
print('Welcome to Password Manager')
print('Choose the option:- ')
print('1. Save a Password')
print('2. Get saved Passwords')
choice = int(input('Answer in 1/2: ').strip())
if choice == 1: save_password(data)
elif choice == 2: get_password(data)
else:
    print('Wrong Input.')