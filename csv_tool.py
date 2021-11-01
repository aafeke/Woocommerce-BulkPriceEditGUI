import csv
import shutil
import os

global priceHeaderIndex

def verifyFile(filePath):
    global priceHeaderIndex
    # Check if file is a proper Woocommerce product csv file
    # with the 'price' column

    with open(filePath, encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)
        if any('Price' in s for s in headers) or any('fiyatı' in s for s in headers):
            for string in headers:
                if('Price' in string or 'fiyatı' in string): break
            
            priceHeaderIndex = headers.index(string)
            file.close()
            return True
    return False

def prepare(filePath):
    try: os.mkdir('.temp')
    except: pass

    shutil.copy(filePath, '.temp\\input.csv')
    shutil.copy(filePath, '.temp\\output.csv')
    shutil.copy(filePath, '.temp\\backup.csv')
    return

def modify(constant):

    inputFile = open('.temp\\input.csv', 'r', encoding='utf-8')
    reader = csv.reader(inputFile)

    with open('.temp\\output.csv', 'w', newline='', encoding='utf-8') as outputFile:
        writer = csv.writer(outputFile)

        # Write the first row a.k.a. headers.
        writer.writerow(next(reader))

        for row in reader:
            tempRow = row 
            if(tempRow[priceHeaderIndex] != ''):
                tempRow[priceHeaderIndex] = modifyValue(tempRow[priceHeaderIndex], constant)
            writer.writerow(tempRow)
        
        outputFile.close()
    inputFile.close()
    return

def modifyValue(source: str, value: str) -> str:
    temp = sanitizeString(source)
    temp = float(temp)

    if '%' in value:
        value = value.replace('%', '')
        temp = temp + temp * float(value) / 100

    else:
        temp = round( temp + float(value), 1 )

    temp = str(temp)
    return unsanitizeString(temp)

def sanitizeString(value: str) -> str:
    # Replace commas with dots for float conversion.
    return value.replace(',', '.')

def unsanitizeString(value: str) -> str:
    # Replace dots with commas back.
    return value.replace('.', ',')