import os
import sys
import Image
import shutil

BasePath = 'd:\\Steam\\steamapps\\common\\skyrim\\Data\\textures\\Maps\\Skyrim\\'
StartX = -57
EndX = 61
StartY = -43
EndY = 50
MissingCount = 0
TotalCount = 0

for X in range(StartX, EndX+1):
    for Y in range(StartY, EndY+1):
        TotalCount += 1
        Filename = BasePath + 'Tamriel.%(x)02d.%(y)02d.dds' % \
                    {'x': X, 'y': Y }
        if not os.path.isfile(Filename):
            print 'Missing File: ', Filename
            MissingCount += 1

print 'Found ', TotalCount, ' files'
print 'Missing ', MissingCount
