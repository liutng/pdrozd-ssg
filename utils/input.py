import os
import shutil
import codecs

def parseInput(arg):
    global newDir #Creates a new Directory for the output
    newDir = os.path.join(os.path.abspath(os.getcwd()), "dist")

    if os.path.exists(newDir): #Checks if dist is already a directory if it is it is removed 
            shutil.rmtree(newDir)
    os.mkdir(newDir)

    if os.path.isfile(arg): #added this incase passed argument is absolute path
        parseFile(arg)
    elif os.path.isdir(arg): #added this incase passed argument is absolute path
        parseDirectory(arg)
    else: #If passed argument is not absolute create an absolute path for it
        path = os.path.abspath(os.getcwd()) + "\\" + arg #Creates a path for the file or directory

        if os.path.isfile(path): #Checks if file or directory
            parseFile(path)
        elif os.path.isdir(path):
            parseDirectory(path)
        else:
            raise SystemExit(f"File or directory dosen't exsit (make sure file extension is included)")
    createIndex()

def parseFile(arg):
    if os.path.splitext(arg)[1] != ".txt":
        print(f"Unable to Proccses " + arg + " because its not a text file")
    else:
        file = codecs.open(arg, "r", encoding="utf-8")
        lines = file.read().splitlines() #Creates a String list of lines 

        fileName = lines[0] #Creates a name for the file with the first line
        
        fullName = os.path.join(newDir, fileName + ".html") #Creates a path for the new file so it is created in dist

        site = codecs.open(fullName, "w", encoding="utf-8")
        site.write('''<!doctype html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <title>''' + fileName + '''</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
    <h1> ''' + fileName + ''' </h1>
    <br>
    <br>
    ''')
        for line in lines: #Loops through the list to fill out the html
            site.write('<p>' + line + '</p>\n')

        site.write('</body>\n</html>') #Finishes the document with a body
    

def parseDirectory(arg):

    allFiles = os.listdir(arg) #Grabs everything in the directory into a list

    for file in allFiles: #Checks if file is a directory or file if it's a directory call parse directory recursively
        tmp = os.path.join(arg, file)
        if os.path.isfile(tmp):
            parseFile(tmp)
        elif os.path.isdir(tmp):
            parseDirectory(tmp)
        else:
            raise SystemExit(f"File or directory dosen't exsit (make sure file extension is included)") 


def createIndex():
    allFiles = os.listdir(newDir)

    if allFiles:
        fullName = os.path.join(newDir, "index.html")

        index = codecs.open(fullName, "w", encoding="utf-8")
        index.write('''<!doctype html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <title> Index </title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
    <h1> Index </h1>
    <br>
    <br>
    <ol>
    ''')
        for file in allFiles: #Loops through the list to fill out the html
            index.write('<li><a href="'+ file +'">' + file + '</a></li>\n')

        index.write('''</ol>
    </body>
    </html>''') #Finishes the document with a body
    else:
        raise SystemExit()