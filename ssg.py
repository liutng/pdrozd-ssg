import sys

from utils.help import *
from utils.input import parseInput
from utils.version import *

try:
    arg = sys.argv[1]
    if arg == "-v" or arg == "--version":
        printVersion()
    elif arg == "-h" or arg == "--help":
        printHelp()
    elif arg == "-i" or arg == "--input":
        try:
            input = sys.argv[2]
            parseInput(input)
        except IndexError:
            raise SystemExit(f"No input was added")    
    else:
        raise Exception()
except IndexError:
    raise SystemExit(f"No arguments were passed")
except Exception:
    raise SystemExit(f"No option for " + arg)