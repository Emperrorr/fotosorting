import os
import time
import datetime
import exifread
import shutil

path_in= input('укажите папку для сортировки:')
path_out= input('укажите папку для вывода:')
ext=('jpg', 'JPG', 'CR2', 'cr2', 'avi', 'mpg', 'mp4', 'mov')

cat=os.walk(path_in, topdown=True, onerror=None, followlinks=False)

for path, folder, files in cat:
    for file in files:
        if os.path.isfile(os.path.join(path, file)):
            if (file.endswith(ext)):
                f=open (os.path.join(path, file), 'rb')
                tags=exifread.process_file(f)
                print (file)
                if 'EXIF DateTimeOriginal' in tags:
                    t=tags['EXIF DateTimeOriginal']
                elif 'Image DateTime' in tags:
                    t=tags['Image DateTime']
                else:
                    t=datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(path, file)))
            t=str(t).replace(':','_')[:10]
            t=str(t).replace('-','_')[:10]
            f.close()       
#            print (t)
            try:
                os.mkdir(os.path.join(path_out, t))
            except OSError:
                pass
            try:
                shutil.move(os.path.join(path, file), os.path.join(path_out, t), copy_function=shutil.copy2)
            except shutil.Error:
                print (file+ ' COPY Error!!!')
                pass

#
#def files(path):
#    for file in os.listdir(path):
#        if (file.endswith('.jpg') or file.endswith('.JPG') or file.endswith('.CR2') or file.endswith('.cr2') or file.endswith('.mp4')):
#            if os.path.isfile(os.path.join(path, file)):
#                yield file
#
#for file in files(path):  
#    f=open (os.path.join(path, file), 'rb')
#    tags=exifread.process_file(f)
#    if 'EXIF DateTimeOriginal' in tags:
#        t=tags['EXIF DateTimeOriginal']
#    elif 'Image DateTime' in tags:
#        t=tags['Image DateTime']
#    else:
#        t=datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(path, file)))
#
#    t=str(t).replace(':','_')[:10]
#    t=str(t).replace('-','_')[:10]
#    f.close()
#    
#    try:
#        os.mkdir(os.path.join(path_out, t))
#    except OSError:
#        pass
#    try:
#        shutil.move(os.path.join(path, file), os.path.join(path_out, t), copy_function=shutil.copy2)
#    except shutil.Error:
#        print (file)
#        pass
