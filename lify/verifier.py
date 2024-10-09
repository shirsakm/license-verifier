import csv
from cryptography.fernet import Fernet
import pandas as pd

with open('.key', 'rb') as key_file:
        key = key_file.read()

def add_license(license_id, license_type):
    cipher = Fernet(key)

    encrypted_license_id = cipher.encrypt(license_id.encode())

    with open('data/licenses.csv', mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([encrypted_license_id, license_type])

def delete_license(license_id):
    cipher = Fernet(key)
    encrypted_license_id = cipher.encrypt(license_id.encode())

    licenses = pd.read_csv('data/licenses.csv', header=None)
    licenses = licenses.drop(encrypted_license_id, axis='columns')

    licenses.to_csv('data/licenses.csv', index=False)

def verify_license(license_id):
    cipher = Fernet(key)
    
    licenses = pd.read_csv('data/licenses.csv', header=None)
    for license in licenses:
        if license[0] == cipher.encrypt(license_id.encode()):
            return {
                'status': 'valid',
                'id': license_id,
                'type': license[1],
            }
        else:
            return {
                'status': 'invalid',
                'id': license_id,
            }
        