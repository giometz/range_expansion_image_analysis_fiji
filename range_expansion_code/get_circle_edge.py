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
IJ.run("Median...", "radius=1");
IJ.run(image, "Sample Variance", "block_radius_x=2 block_radius_y=2")
IJ.run(image, 'Threshold...', 'Default Dark')
dial = WaitForUserDialog('Threshold please and remove incorrect areas.')
dial.show()
# Fill holes
IJ.run("Fill Holes")
# Remove small particles
IJ.run("ParticleRemoverPy ", "enter=.1")
IJ.run("Close-")
IJ.run("Find Edges")