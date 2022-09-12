from msilib.schema import Directory
import os
import shutil
import codecs

def parseInput(arg):
    path = os.path.abspath(os.getcwd()) + "\\" + arg

    dist = "dist"
    
    global newDir
    newDir = os.path.join(os.path.abspath(os.getcwd()), dist)

    if os.path.exists(newDir):
        shutil.rmtree(newDir)
    os.mkdir(newDir)

    if os.path.isfile(path):
        parseFile(path)
    elif os.path.isdir(path):
        parseDirectory(path)
    else:
       raise SystemExit(f"File or directory dosen't exsit (make sure file extension is included)") 

def parseFile(arg):
    file = codecs.open(arg, "r", encoding="utf-8")
    lines = file.read().splitlines()

    fileName = lines[0]
    
    fullName = os.path.join(newDir, fileName + ".html")

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
    for line in lines:
        site.write('<p>' + line + '</p>\n')

    site.write('</body>')
    

def parseDirectory(arg):

    allFiles = os.listdir(arg)

    for file in allFiles:
        tmp = os.path.join(arg, file)
        if os.path.isfile(tmp):
            parseFile(tmp)
        elif os.path.isdir(tmp):
            parseDirectory(tmp)
        else:
            raise SystemExit(f"File or directory dosen't exsit (make sure file extension is included)") 