import os
import sys
import Image
import shutil

SrcPath = 'd:\\skyrimmaps\\NoWater\\'
DestPath = 'd:\\skyrimmaps\\nowater-fix\\'
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
        OldX = CellX + OutputXOffset
        OldY = CellY + OutputYOffset
        SrcFilename = SrcPath + 'skyrim-%(x)d-%(y)d-16.jpg' % \
                   {'x': OldX, 'y': OldY}
        
        NewX = OldX
        NewY = 2*OutputYOffset - OldY 
        OutputFilename = DestPath + 'skyrim-%(outx)d-%(outy)d-16.jpg' % \
                   {'outx': NewX, 'outy': NewY }

        if not os.access(SrcFilename, os.F_OK):
            print NoExistCount, ') No Exist', SrcFilename
            NoExistCount = NoExistCount + 1
            SrcFilename = 'd:\\skyrimmaps\\nullimage.jpg'
            
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
