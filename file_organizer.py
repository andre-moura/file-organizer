import os
import shutil
import platform

def organize(self):
    path = self.path.get()
    if path != '':
        files = os.listdir(path)
        slash = '\\'

        if platform.system().lower() == 'windows':
            slash =  '/' 
            
        for file in files:
            filename, extension = os.path.splitext(file)
            extension = extension[1:]

            if os.path.exists(path + slash + extension):
                shutil.move(path + slash + file, path + slash + extension + slash + file)
            else:
                os.makedirs(path + slash + extension)
                shutil.move(path + slash + file, path + slash +  extension + slash +  file)