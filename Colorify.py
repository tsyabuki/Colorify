import inputVals as ini
import colorsys as csys
from PIL import Image as img
from PIL import ImageOps as iops

if ini.saturation == 0:
	ini.saturation = 50

lightCol = csys.hls_to_rgb((ini.hue+180)/360, 300, (ini.saturation-50)/100)
darkCol = csys.hls_to_rgb((ini.hue+180)/360, 0, (ini.saturation-50)/100)

# Creates a image object for the source image
imgSource = img.open(ini.inputFileName)
# Grayscales the output image
imgOut = iops.grayscale(imgSource)
# Colorizes the output image based on color values
imgOut = iops.colorize(imgOut, darkCol, lightCol)

# Outputs based on overwrite settings
if ini.overwrite:
    imgOut.save(ini.inputFileName)
else:
    imgOut.save(ini.outputFileName)