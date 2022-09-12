import sys

from utils.help import *
from utils.input import parseInput
from utils.version import *

try:
    arg = sys.argv[1]  #Grabs the arguments from the command line
    if arg == "-v" or arg == "--version":
        printVersion()
    elif arg == "-h" or arg == "--help":
        printHelp()
    elif arg == "-i" or arg == "--input":
        try:
            input = sys.argv[2]
            parseInput(input)
        except IndexError:
            raise SystemExit(f"No input was added") #Exits Program if called input without file or directory   
    else:
        raise Exception() #Raises exception if argument passed is not an option
except IndexError:
    raise SystemExit(f"No arguments were passed if unsure about which aurgument are avialable use -h or --help")
except Exception:
    raise SystemExit(f"No option for " + arg)