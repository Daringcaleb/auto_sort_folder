import os
import shutil
import subprocess

AUDIO= ['.mp3', '.wav', '.acc', '.raw']      
IMAGES= ['.jpeg', '.jpg', '.png', '.PNG']     
DOC= ['.doc', '.docx', '.xls', '.xlsx']
PDF = ['.pdf']
VIDEO= ['.mp4', '.avi', '.mkv', '.mov']    
CODES= ['.py', '.js', '.css', '.java', '.dart', '.yaml']
ZIP = ['.zip', '.7z', '.rar']
SETUP = ['.exe', '.dmg']


print ('SORT Folder')
print ('..........You are HERE: {}'.format(os.getcwd()))

files = os.listdir()

Folder = ['Audio', 'Images', 'Doc', 'PDFs', 'Videos', 'Codes', 'Zip_Files', 'Softwares','Folders', 'Others']
if not os.path.isdir('./Audio'):
    for d in Folder:
        os.mkdir('./{}'.format(d))
    print('Audio Folder Created')

    for f in files:
        name, extention = os.path.splitext(f)
        extension = name[name.rfind("."):]

        if extention in IMAGES:
            shutil.move(f, './Images/{}'.format(f))
        elif extention in DOC:
            shutil.move(f, './Doc/{}'.format(f))
        elif extention in PDF:
            shutil.move(f, './PDFs/{}'.format(f))
        elif extention in VIDEO:
            shutil.move(f, './Videos/{}'.format(f))
        elif extention in CODES:
            shutil.move(f, './Codes/{}'.format(f))
        elif extention in ZIP:
            shutil.move(f, './Zip_Files/{}'.format(f))
        elif extention in SETUP:
            shutil.move(f, './Softwares/{}'.format(f))
        else:
            if os.path.isdir(name):
                if name not in Folder:
                    shutil.move(f, './Folders/{}'.format(f))
            else:
                if f != 'sort.py':
                    shutil.move(f, './Others/{}'.format(f))
print ('...........................................Sort Complete..............................................')