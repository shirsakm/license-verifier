import csv
import pandas as pd

def add_license(license_id, license_type):
    with open('data/licenses.csv', mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([license_id, license_type])

def delete_license(license_id):
    with open('data/licenses.csv', mode='r') as file:
        reader = csv.reader(file)
        licenses = [row for row in reader if row[0] != license_id]

    with open('data/licenses.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(licenses)

def verify_license(license_id):
    licenses = pd.read_csv('data/licenses.csv', header=None)
    for _, license in licenses.iterrows():
        if license[0] == license_id:
            return {
                'status': 'valid',
                'id': license_id,
                'type': license[1],
            }
    return {
        'status': 'invalid',
        'id': license_id,
    }

def get_licenses():
    with open('data/licenses.csv', mode='r') as file:
        reader = csv.reader(file)
        licenses = [row for row in reader]
        return licenses
