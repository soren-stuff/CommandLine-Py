import pathlib
import commandList

RunCommandLine = True

while RunCommandLine == True:
    currentCommand = input(str(pathlib.Path(__file__).parent.resolve()) + ">")
    commandUsed = currentCommand.split()[0]
    match commandUsed:
        case "open":
            commandList.openFunc()
        case _:
            print("test")
        
#    if commandUsed == "open":
 #       fileDirectory = currentCommand.split()[1]
  #      f = open(fileDirectory)
   # else:
    #    print("Command not recognized. Check your spelling, or check that it is a real command")