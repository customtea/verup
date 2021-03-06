#!/usr/bin/python
import shutil
import sys
import glob
import os

def version_up(filefullpath: str):
    filedirname = os.path.dirname(filefullpath)
    filepath, extension = os.path.splitext(filefullpath)
    filename = os.path.basename(filepath)
    # get file list
    filelist = glob.glob(f"{filedirname}/*{extension}")
    # filtered filename included
    filelist = list(filter(lambda x:filename in x, filelist))
    # filtered version num (_vXX) included
    filelist = list(filter(lambda x:"_v" in x, filelist))
    if len(filelist) != 0:
        filelist = sorted(filelist, key=lambda x: int(x.split("_")[-1].split(".")[0][1:]), reverse=True)
        vernum = int(filelist[0].split("_")[-1].split(".")[0][1:])
        newvernum = vernum + 1
    else:
        newvernum = 1

    newvernumchar = format(newvernum, "02d")
    newfilename = f"{filedirname}/{filename}_v{newvernumchar}{extension}"
    shutil.copy(filefullpath, newfilename)
    print(f"{filefullpath} is copied {newfilename}")


if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print("Usage: Invalid Argument")
        exit()
    else:
        version_up(sys.argv[1])