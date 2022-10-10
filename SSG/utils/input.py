from ast import parse
from asyncio.windows_events import NULL
from distutils import file_util
import json
from os.path import exists
import os
from pickletools import string1
import shutil
import codecs
import string
from tkinter.tix import Tree
from tokenize import String

def parseInput(arg,lang="en-CA"):
    global newDir #Creates a new Directory for the output
    global newlang
    newDir = os.path.join(os.path.abspath(os.getcwd()), "dist")
    newlang = lang if len(lang) != 0 else "en-CA"

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
            raise SystemExit(f"Input file or directory dosen't exsit (make sure file extension is included)")
    createIndex()

def readConfigFile(arg = ""):
    if len(arg) != 0:
        if(exists(arg)):
            if os.path.isfile(arg):
                jsonFile = open(arg)
                if(jsonFile.readable()):
                    jsonMap =  json.load(jsonFile)
                    if len(jsonMap) == 0:
                        raise SystemExit(f"Config file doesn't contain necessary input and output arguments.")
                    else:
                        input = jsonMap["input"] if jsonMap.__contains__("input") else "";  # Check if argument "input" is included in the config file
                        lang = jsonMap["lang"] if jsonMap.__contains__("lang") else ""; # Check if argument "lang" is included in the config file.
                        if len(input) != 0:
                            parseInput(input,lang)
                        else:
                          raise SystemExit(f"Input file is not included in the config file.")

                else:
                    raise SystemExit(f"Can't read file {arg}, please make sure you have the read permission to the file.")
            
            else:
                raise SystemExit(f"{arg} is a directory, please provide a config file.")
             
        else:
            raise SystemExit(f"Can't find a valid config file in {arg}")
    else:
        raise SystemExit("Config file is not provided, please make sure to pass a valid config file.")

def parseFile(arg):

    file = codecs.open(arg,"r", encoding="utf-8")
    lines = file.read().splitlines()

    fileName = lines[0]
    fullName = os.path.join(newDir, fileName + ".html")

    header = '''<!doctype html>
<html lang=''' + newlang + '''>
<head>
<meta charset="utf-8">
<title>''' + fileName + '''</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
<h1> ''' + fileName + ''' </h1>
<br>
<br>
<p>
'''
    footer = '</p>\n</body>\n</html>'

    if os.path.splitext(arg)[1] == ".txt":
        site = codecs.open(fullName, "w", encoding="utf-8")
        site.write(header)
        for line in lines[1:]: #Loops through the list to fill out the html
                if line != "":
                    site.write(line)
                else:
                    site.write('</p>\n<p>')

        site.write(footer) #Finishes the document with a body
    elif os.path.splitext(arg)[1] == ".md":
        site = codecs.open(fullName, "w",encoding="utf-8")
        site.write(header)
        for line in lines[1:]: #Loops through the list to fill out the html
            if line != "":
                    site.write(parseMarkdown(line))
            else:
                    site.write('</p>\n<p>')

        site.write(footer) #Finishes the document with a body
     


    else:
        print(f"Unable to Proccses " + arg + " because its not a text file")

    
def parseMarkdown(md:str):
    htmlStr = ""
    if md.startswith("# "): #implements heading 1 conversion.
        htmlStr = "<h1>" + md.replace("# ","") + "</h1>"
    elif(len(md.strip()) != 0):
        htmlStr = md

    search = '*'
    # searching for position of *
    index = md.find(search)
    lastIndex = 0
    if index != -1:
        lastIndex = searchStr(search, index, md)
    # Adding Italics in markdown
    if index != -1 and lastIndex != 0:
        md = replace("</i>", lastIndex, md)
        md = replace("<i>", index, md)
        htmlStr = md

    search = '`'
    # searching for position of *
    index = md.find(search)
    lastIndex = 0
    if index != -1:
        lastIndex = searchStr(search, index, md)
    # Adding Italics in markdown
    if index != -1 and lastIndex != 0:
        md = replace("</code>", lastIndex, md)
        md = replace("<code>", index, md)
        htmlStr = md

    htmlStr += " " #adding a space to the end of the line
    return htmlStr

def searchStr(search, index, md:str):
    # searching for position of search variable
    lastIndex = 0
    if index != -1:
        for char_index in range(index, len(md)):
            if md[char_index] == search:
                lastIndex = char_index
    return lastIndex

def replace(replace:str, index, md:str):
    md = md[:index] + replace + md[index+1:] # Have to do the last position first or else it messes with the first indexmd
    return md

def parseDirectory(arg):

    allFiles = os.listdir(arg) #Grabs everything in the directory into a list

    for file in allFiles: #Checks if file is a directory or file if it's a directory call parse directory recursively
        tmp = os.path.join(arg, file)
        if os.path.isfile(tmp):
            parseFile(tmp)
        elif os.path.isdir(tmp):
            parseDirectory(tmp)
        else:
            raise SystemExit(f"Input file or directory dosen't exsit (make sure file extension is included)") 


def createIndex():
    allFiles = os.listdir(newDir)

    if allFiles:
        fullName = os.path.join(newDir, "index.html")

        index = codecs.open(fullName, "w", encoding="utf-8")
        index.write('''<!doctype html>
<html lang='''+ newlang +'''>
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