import sys

from utils.help import *
from utils.input import parseInput
from utils.version import *

try:
    for arg in sys.argv:
        if arg == "-h" or arg == "--help":
            printHelp()

    arg = sys.argv[1]  #Grabs the arguments from the command line

    if arg == "-v" or arg == "--version":
        printVersion()
    elif arg == "-i" or arg == "--input":
        try:
            input = sys.argv[2]
            try:
                if sys.argv[3] == "-l" or arg == "--lang":
                    parseInput(input, sys.argv[4])
            except Exception:
                parseInput(input)
        except IndexError:
            raise SystemExit(f"No input was added") #Exits Program if called input without file or directory   
    else:
        raise Exception() #Raises exception if argument passed is not an option
except IndexError:
    raise SystemExit(f"No arguments were passed if unsure about which aurgument are avialable use -h or --help")
except Exception:
    raise SystemExit(f"No option for " + arg)