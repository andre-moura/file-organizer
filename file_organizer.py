import os
import shutil

path = input("")
files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(path)
    extension = extension[1:]

    if os.path.exists(path+' /'+ extension):
        shutil.move(path+' /'+file, path+' /' + extension + ' /' +file)
    else:
        os.makedirs(path+' /'+extension)
        shutil.move(path+' /'+file, path+ ' /' + extension + ' /' + file)