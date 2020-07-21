#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Charles Path
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK
#List all files in all folders and create a file to the player to read from!

import os
import config as CF
import random
#use CD.iniFolder when none is provided
def getListOfFiles(dirName):
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
            if checkFormat(fullpath):
                print(fullpath)
                allFiles.append(fullpath)
    if CF.random:
        return random.sample(allFiles, len(allFiles))
    return allFiles

def _getListOfFiles(dirName):
  # Get the list of all files in directory tree at given path
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
    CF.totalSongs = listOfFiles.count
    
    # Print the files    
    for elem in listOfFiles:
        print(elem)
    print(CF.totalSongs)
    
def _getListOfFolders(dirName):
    d = dirName
    CF.listDirectories = [os.path.join(d, o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))]#[x[0] for x in os.walk(d)]#[os.path.join(d, o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))]
    CF.listDirectoriesSelect = [dirName for dirName in os.listdir(d) if os.path.isdir(os.path.join(d,dirName))]#[x[1] for x in os.walk(d)]#[dirName for dirName in os.listdir(d) if os.path.isdir(os.path.join(d,dirName))]
    

def checkFormat(entry):
    count = 0
    for af in CF.audioFormats:
        if entry.endswith(af):
            count += 1
    if count > 0:
        return True
    else:
        return False
    
def randomPlayList():
    return random.sample(CF.currentPlayList, len(CF.currentPlayList))
    

def main():
    dirName = CF.initFolder
#    listOfFiles = getListOfFiles(dirName)
    _getListOfFiles(dirName)
    #print(listOfFiles)
    
if __name__ == '__main__':
    main()       
    