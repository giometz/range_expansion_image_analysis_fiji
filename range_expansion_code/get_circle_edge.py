from ij import IJ
import ij.gui
from ij.gui import WaitForUserDialog
from ij.plugin import ChannelSplitter
import os
import sys
import ij
import ij.Macro
from ij.process import ImageProcessor

# Get  the last slice; assume it is always brightfield
image = IJ.getImage()

# May have to change the # of pixels...should be about the width of the edge
IJ.run(image, "Standard Deviation", "block_radius_x=7 block_radius_y=7")
IJ.run(image, 'Threshold...', 'Default Dark')
dial = WaitForUserDialog('Threshold please and remove incorrect areas.')
dial.show()