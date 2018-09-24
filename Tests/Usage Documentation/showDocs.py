#!/usr/bin/python

#----------------------------------------------------------------------
# Static Site Generator
# Program: showDocs
# Author: Ricky Dall'Armellina
# Date: 09/24/2018
#
# Description: checks if the first program argument is '-help' or if 
#              it's the first program execution to show the usuage docs
#----------------------------------------------------------------------

DEBUG = True

# Import statements
import sys, os, webbrowser

FIRST_USE_FILE = "firstUse"
USAGE_DOC = "file://" + os.path.abspath("Flock-HowTo.html")

# Custom functions
def LOG(string):
    if DEBUG:
        print(string)

#def showDocs(argValue):

def createFile():
    # creates the first time use file and adds the following contents to it
    f = open(FIRST_USE_FILE, 'w+', 0)
    f.write("The existance of this files tells the program it has been executed before.\n")
    f.write("Deleting this file will result in the program performing a first time execution and show the usage documentation.\n")
    f.write("You can also show the usage documentation by calling the program with the '-help' argument.\n")
    f.write("Thank you for using Flock!")
    f.close()

def openDocs():
    # open usuage documentation with default browser
    LOG("Opening usage documentation with the default web-browser\n")
    #webbrowser.open_new_tab(USAGE_DOC)
    webbrowser.open(USAGE_DOC, new=0, autoraise=True)

#----------------------------------------------------------------------
#----------------------------------------------------------------------

print("\n - Welcome to the Static Site Generator! - \n")
print("Type '-help' when executing the program for usage guide\n")

# check if firstUse file exists
LOG("Checking if first time use file exists: ")
isFirstUse = os.path.isfile(FIRST_USE_FILE)
if not isFirstUse:
    # if not create it
    LOG("File does not exist, creating it...\n")
    createFile()
    # open the documentation
    # [insert code here]
else:
    LOG("File exists\n")

# REFERENCE:
# sys.argv[0] = program name
# sys.argv[1] = first argument
# len(sys.argv) = number of arguments
# str(sys.argv) = all arguments

# check for '-help' argument
# argument list has to be greater than 1 to know there could be a valid arguemnt
if len(sys.argv) > 1:
    # loop through all arguments to catch the possible '-help'
    for arg in sys.argv:
        if arg == "-help":
            LOG("'-help' called!")
            # call show website
            openDocs()
else:
    LOG("No arguments called\n")