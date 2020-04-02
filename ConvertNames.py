import os
import sys
import Image
import shutil

SrcPath = 'd:\\Steam\\steamapps\\common\\skyrim\\Data\\textures\\Maps\\Skyrim\\tga\\'
FileCount = 0
MinCellX = -57
MaxCellX = 61
MinCellY = -43
MaxCellY = 50
OutputXOffset = 57
OutputXFactor = 1
OutputYOffset = 50
OutputYFactor = -1
NoExistCount = 0
ZoomLevel = 16
NoExistFile = "nullimage.jpg"

for CellX in range(MinCellX, MaxCellX + 1):
    for CellY in range(MinCellY, MaxCellY + 1):
        SrcFilename = SrcPath + 'Tamriel.%(x)02d.%(y)02d00.tga' % \
                   {'x': CellX, 'y': CellY}
        OutX = CellX * OutputXFactor + OutputXOffset
        OutY = CellY * OutputYFactor + OutputYOffset
        OutputFilename = 'd:\\srmaps1\\zoom%(zoom)d\\skyrim-%(outx)d-%(outy)d-%(zoom)d.tga' % \
                   {'outx': OutX, 'outy': OutY, 'zoom': ZoomLevel}

        if not os.access(SrcFilename, os.F_OK):
            print NoExistCount, ') No Exist', SrcFilename
            NoExistCount = NoExistCount + 1
            SrcFilename = 'd:\\srmaps1-256\\nullimage.jpg'

        print FileCount, ') ', SrcFilename, ' to ', OutputFilename
        shutil.copyfile(SrcFilename, OutputFilename)
        
        FileCount = FileCount + 1

print 'No Exist = ', NoExistCount
        
#FileCount = 100
#for file in os.listdir("f:\\obmaps\\resizejpgs\\"):
#    FileCount = FileCount + 1
#    print FileCount, file
#    if FileCount > 100:
#        break
