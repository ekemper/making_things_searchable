# !/usr/bin/python
import os
import ocr
from printer import pr

def gatherFilePaths():
    rawFilePaths = []   
    for root, dirs, files in os.walk("./rawDocuments", topdown=False):
        for name in files:
            rawFilePaths.append(os.path.join(root, name))

    return rawFilePaths


def isImage(filePath):
    name, ext = os.path.splitext(filePath)
    possibleImageExtensions = ['.jpg', '.jpeg', '.png']
    for e in possibleImageExtensions:
        if e == ext:
            return True

    return False 

def generateDocument(filePath):
    text = ''

    if isImage(filePath):
        text = ocr.getText(filePath)

    return {
        'rawFilePath': filePath,
        'text': text
    }

def generateDocuments(rawFilePaths):
    newDocuments = []

    for filePath in rawFilePaths:
        newDocuments.append(generateDocument(filePath))

    return newDocuments
    
    
def main():
    filePaths = gatherFilePaths()
    newDocs = generateDocuments(filePaths)
    pr({'newDocs': newDocs})

if __name__ == '__main__':
    main()
