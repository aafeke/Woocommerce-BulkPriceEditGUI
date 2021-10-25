import csv
import shutil
import os

def verifyFile(filePath):
    # Check if file is a proper Woocommerce product csv file
    # with the 'price' column

    with open(filePath, encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)
    return any('Price' in s for s in headers) or any('fiyatı' in s for s in headers)

def prepare(filePath):
    try: os.mkdir('.temp')
    except: pass

    shutil.copy(filePath, '.temp\\output.csv')
    shutil.copy(filePath, '.temp\\backup.csv')
    return

def modify():
    return
