import os
import sys
import Image
import shutil

def makeInFilename(outx, outy, zoom):
        return 'd:\\srmaps1\\' + 'zoom%(zoom)d\\skyrim-%(outx)d-%(outy)d-%(zoom)d.tga' % \
                    {'outx': outx, 'outy': outy, 'zoom': zoom }

def makeOutFilename(outx, outy, zoom):
        return FilePath + 'zoom%(zoom)d\\skyrim-%(outx)d-%(outy)d-%(zoom)d.jpg' % \
                    {'outx': outx, 'outy': outy, 'zoom': zoom }    

FilePath = 'd:\\srmaps1-256\\'
NullFile = 'd:\\srmaps1-256\\nullimage.jpg'
ImageSize = 256
StartZoom = 16
StartX = 0
StartY = 0
NumX = 119
NumY = 94
CurrentZoom = StartZoom

for XIndex in range(StartX, NumX+1):
        for YIndex in range(StartY, NumY+1):
            Filename = makeInFilename(XIndex, YIndex, StartZoom)

            try:
                ImageTmp = Image.open(Filename)
            except IOError:
                ImageTmp = Image.open(NullFile)

            OutFile = makeOutFilename(XIndex, YIndex, StartZoom)
            ImageTmp.save(OutFile)
            print CurrentZoom, XIndex, YIndex
