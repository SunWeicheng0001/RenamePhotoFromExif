import exifread
import os
import re
# open image file for reading (binary mode)
for root, _, _ in os.walk('E:\Pictures\照片',topdown=False):
    os.chdir(root)
    for filename in os.listdir("."):
        if os.path.isfile(filename):
            r = re.compile('.*\\-.*\\-.* .*\\..*\\..*\\..*')
            if r.match(filename):
                continue
            file = open(filename,"rb")
            extension = os.path.splitext(file.name)[1][1:].strip().lower()
            tags = exifread.process_file(file)
            try:
                date = str(tags['EXIF DateTimeOriginal'])
            except KeyError:
                file.close()
                continue
            date = date.replace(":","-",2)
            date = date.replace(":",".")
            file.close()
            if os.path.isfile(date+"."+extension):
                continue
            print("rename " + file.name +" to "+date+"."+extension)
            os.rename(file.name,date+"."+extension)