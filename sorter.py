import os
# import time
import datetime
import exifread
import shutil

a=int()
b=int()
path_in= input('укажите папку для сортировки:')
path_out= input('укажите папку для вывода:')
ext=('jpg', 'jpeg', 'JPEG', 'JPG', 'CR2', 'cr2', 'avi', 'mpg', 'mp4', 'mov')

cat=os.walk(path_in, topdown=True, onerror=None, followlinks=False)

for path, folder, files in cat:
    for file in files:
        if os.path.isfile(os.path.join(path, file)):
            if (file.endswith(ext)):
                f=open (os.path.join(path, file), 'rb')
                tags=exifread.process_file(f)
#                 print (file)
                if 'EXIF DateTimeOriginal' in tags:
                    t=tags['EXIF DateTimeOriginal']
                elif 'Image DateTime' in tags:
                    t=tags['Image DateTime']
                else:
                    t=datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(path, file)))
            else:
                a+=1
                print (file+ ' is skipped')
                continue
            t=str(t).replace(':','-')[:10]
            t=str(t).replace('_','-')[:10]
            f.close()       
            try:
                os.mkdir(os.path.join(path_out, t))
            except OSError:
                pass
            try:
                shutil.move(os.path.join(path, file), os.path.join(path_out, t), copy_function=shutil.copy2)
                print (file+ ' is moved to '+path_out+'\\'+t)
                b+=1
            except shutil.Error:
                a+=1
                print (file+ ' COPY Error!!!')
                pass
print (b,' file(s) moved')
print (a,' file(s) skipped')
