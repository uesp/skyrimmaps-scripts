import os
import sys
import Image
import shutil

def makeFilename(outx, outy, zoom):
        return FilePath + 'zoom%(zoom)d\\skyrim-%(outx)d-%(outy)d-%(zoom)d.jpg' % \
                    {'outx': outx, 'outy': outy, 'zoom': zoom }

FilePath = 'd:\\srmaps1-256\\'
NullFile = 'd:\\srmaps1-256\\nullimage.jpg'
ImageSize = 256
StartZoom = 16
EndZoom = 8
StartX = 0 * 1
StartY = 0 * 1
NumX = 128 * 2
NumY = 128 * 2
CurrentZoom = StartZoom

for CurrentZoom in range(StartZoom, EndZoom, -1):
    StartY = int(StartY / 2)
    StartX = int(StartX / 2)
    NumX = int(NumX / 2)
    NumY = int(NumY / 2)
    for XIndex in range(StartX, StartX+NumX, 2):
        for YIndex in range(StartY, StartY+NumY, 2):
            FileNW = makeFilename(XIndex, YIndex, CurrentZoom)
            FileNE = makeFilename(XIndex+1, YIndex, CurrentZoom)
            FileSW = makeFilename(XIndex, YIndex+1, CurrentZoom)
            FileSE = makeFilename(XIndex+1, YIndex+1, CurrentZoom)
    
            try:
                ImageNW = Image.open(FileNW)
            except IOError:
                ImageNW = Image.open(NullFile)
                
            try:            
                ImageNE = Image.open(FileNE)
            except IOError:
                ImageNE = Image.open(NullFile)
    
            try:            
                ImageSW = Image.open(FileSW)
            except IOError:
                ImageSW = Image.open(NullFile)
    
            try:            
                ImageSE = Image.open(FileSE)
            except IOError:
                ImageSE = Image.open(NullFile)        
    
            NewImage = Image.new("RGB", (ImageSize, ImageSize) )
            NewImage.paste(ImageNW.resize((ImageSize/2,ImageSize/2), Image.ANTIALIAS), (0,0))
            NewImage.paste(ImageNE.resize((ImageSize/2,ImageSize/2), Image.ANTIALIAS), (ImageSize/2,0))
            NewImage.paste(ImageSW.resize((ImageSize/2,ImageSize/2), Image.ANTIALIAS), (0,ImageSize/2))
            NewImage.paste(ImageSE.resize((ImageSize/2,ImageSize/2), Image.ANTIALIAS), (ImageSize/2,ImageSize/2))
                    
            OutputFile = makeFilename(XIndex/2, YIndex/2, CurrentZoom - 1)
            NewImage.save(OutputFile)
            
            print CurrentZoom, XIndex, YIndex
    
    
#OutputFilename = makeFilename(1, 2, 3)
#print OutputFilename
