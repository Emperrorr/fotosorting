import os
import time
import datetime
import exifread
import shutil

path= input('укажите папку для сортировки:')
def files(path):
    for file in os.listdir(path):
        if (file.endswith('.jpg') or file.endswith('.JPG') or file.endswith('.CR2') or file.endswith('.cr2')):
            if os.path.isfile(os.path.join(path, file)):
                yield file

##    print(tags['EXIF DateTimeOriginal'])
##    t=tags['EXIF DateTimeOriginal']
#    t=str(t).replace(':','_')[:10]
###    print(t)
#    try:
#        os.mkdir(os.path.join(path, t))
#    except OSError:
#        pass
#    try:
#        shutil.move(os.path.join(path, file), os.path.join(path, t), copy_function=shutil.copy2)
#    except shutil.Error:
#        print (file)
#        pass

for file in files(path):  
##    print(file)
    f=open (os.path.join(path, file), 'rb')
    tags=exifread.process_file(f)
    if 'EXIF DateTimeOriginal' in tags:
        t=tags['EXIF DateTimeOriginal']
    elif 'Image DateTime' in tags:
        t=tags['Image DateTime']
    else:
        t=datetime.datetime.fromtimestamp(os.path.getctime(os.path.join(path, file)))
##    print(tags['EXIF DateTimeOriginal'])
##    t=tags['EXIF DateTimeOriginal']
    t=str(t).replace(':','_')[:10]
    t=str(t).replace('-','_')[:10]
    f.close()
##    print(t)
    try:
        os.mkdir(os.path.join(path, t))
    except OSError:
        pass
    try:
        shutil.move(os.path.join(path, file), os.path.join(path, t), copy_function=shutil.copy2)
    except shutil.Error:
        print (file)
        pass
