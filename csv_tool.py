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
                tempRow[priceHeaderIndex] = unsanitizeString(
                    str(
                        float(
                            sanitizeString(
                                tempRow[priceHeaderIndex]
                            )
                        ) + constant
                    )
                )
            writer.writerow(tempRow)
        outputFile.close()
    inputFile.close()
    return
                
def sanitizeString(value):
    # Replace commas with dots for float conversion.
    if ',' in value:
        value = value.replace(',', '.')
    return value

def unsanitizeString(value):
    # Replace dots with commas back.
    if '.' in value:
        value = value.replace('.', ',')
    return value