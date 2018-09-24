# !/usr/bin/python
import os
import ocr

def gatherFilePaths():
    rawFilePaths = []   
    for root, dirs, files in os.walk("./rawDocuments", topdown=False):
        for name in files:
            rawFilePaths.append(os.path.join(root, name))

    return rawFilePaths


def isImage(filePath):
    name, ext = os.path.splitext(filePath)
    possibleImageExtensions = ['jpg', 'jpeg', '.png']
    if ext in possibleImageExtensions:
        return True

    return False 

def generateDocument(filePath):
    newDoc = {}
    
    if isImage(filePath):
        imageText = ocr.getText(filePath)

    newDoc = {
        'rawFilePath': filePath,
        'text': imageText
    }




def generateDocuments(rawFilePaths):
    newDocuments = []

    for filePath in rawFilePaths:
        newDocuments.append(generateDocument(filePath))

    return newDocuments
    
    
    
