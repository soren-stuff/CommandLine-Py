import mainScript

def openFunc():
    fileDirectory = mainScript.currentCommand.split()[1]
    f = open(fileDirectory)
    