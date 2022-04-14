from asyncore import read
import mainScript

def openFunc():
    fileDirectory = mainScript.currentCommand.split()[1]
    f = open(fileDirectory)
    readStuff = f.read()
    f.close
    print(fileDirectory + "'s contents read out as follows:\n" + readStuff)