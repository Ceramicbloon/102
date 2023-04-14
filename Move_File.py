import os
import shutil
src = 'Your src. I prefer not moving every single file from my downloads to another file.'
dst = "Your dst. I prefer not moving every single file from my downloads to another file."
listOfFiles = os.listdir(src)
print(listOfFiles)
for fileName in listOfFiles:
    name, ext = os.path.splitext(fileName)
    print(name, ext)
    if ext == '':
        continue
    if ext in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = src + '/' + fileName
        path2 = dst + '/' + "imageFiles"
        path3 = dst + '/' + "imageFiles" + '/' + fileName
        if os.path.exists(path2):
            print('moving')
            shutil.move(path1, path3)
        else:
            os.mkdir(path2)
            print('moving')
            shutil.move(path1, path3)

    