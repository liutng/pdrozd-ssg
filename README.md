# pdrozd-ssg

pdrozd-ssg is a static site generator created in python

# Optional features

* Added title parsing

* Added recursive search

* Added automatically generated index file

# Requirements

Python 3

# How to run

  after installing python 3 run the command use the command
* `` py .\ssg.py [options] ``
  
* example `` py .\ssg.py -i .\Sherlock-Holmes-Selected-Stories\ ``

# Commands

The commands of pdrozd-ssg are
* -h or --help this will display to the user the options they have

* -v or --version this will display to the user the current verison of pdrozd-ssg

* -i or --input this with a combanation of .txt or .md file or directory will output your files as a Static Site
  to use put in the format 
 
 ```py ssg.py -i or --input [file.txt\text.ms] or [directory\]``` 

* -l or --lang this at the end of the input command will allow the default language of the HTML files to change
   ```py ssg.py -i or --input [file.txt\text.md] or [directory\] -l or --lang [language]```

 # New feature
 * Added markdown language support for # heading 1
