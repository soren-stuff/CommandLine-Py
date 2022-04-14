import pathlib
import commandList

RunCommandLine = True

while RunCommandLine == True:
    currentCommand = input(str(pathlib.Path(__file__).parent.resolve()) + ">")
    commandUsed = currentCommand.split()[0]
    match commandUsed:
        case "read":
            commandList.readFunc()
        case _:
            print("Command not recognized '" + commandUsed + "' - Did you misspell a command, or does the command not exist?")