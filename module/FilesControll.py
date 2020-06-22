#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Charles Path
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK
#List all files in all folders and create a file to the player to read from!

import os
import config as CF
#use CD.iniFolder when none is provided
def getListOfFiles(dirName):
    if dirName == "":
        dirName = CF.initFolder
    #creat a files list and directories
    listOfFiles = os.listdir(dirName)
    allFiles = list()
    #iterate over every entry
    for entry in listOfFiles:
        fullpath = os.path.join(dirName, entry)
        # if it is a directory, then list files
        if os.path.isdir(fullpath):
            #print(fullpath)
            allFiles = allFiles +  getListOfFiles(fullpath)
        else:
            print(fullpath)
            allFiles.append(fullpath)
    return allFiles

def _getListOfFiles(dirName):
  # Get the list of all files in directory tree at given path
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
      
    # Print the files    
    for elem in listOfFiles:
        print(elem)    

def main():
    dirName = CF.initFolder
#    listOfFiles = getListOfFiles(dirName)
    _getListOfFiles(dirName)
    #print(listOfFiles)
    
if __name__ == '__main__':
    main()       
    