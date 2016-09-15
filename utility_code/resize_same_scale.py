import ij
from ij import IJ
from ij.io import DirectoryChooser

type_to_save_as = '.tif'

inputFolder = DirectoryChooser('Set input directory.').getDirectory()
outputFolder = DirectoryChooser('Set output directory.').getDirectory()

import glob as glob
import os

image_list = [os.path.basename(x) for x in glob.glob(inputFolder + '*.tif')]

# We *shrink* smaller images.
max_scaled_width = 0

for image_name in image_list:
	cur_image = ij.ImagePlus(inputFolder + image_name)

	cal = cur_image.getCalibration()
	scale = cal.pixelWidth
	width = cur_image.width

	scaled_width = scale*width

	if scaled_width > max_scaled_width:
		max_scaled_width = scaled_width

print 'Maximum scaled width is:' , max_scaled_width

# Now that we have the maximum width, shrink each image appropriately.
import os

for image_name in image_list:
	cur_image = ij.ImagePlus(inputFolder + image_name)

	cal = cur_image.getCalibration()
	scale = cal.pixelWidth
	width = cur_image.width

	scaled_width = scale*width

	shrink_scale = scaled_width/max_scaled_width

	scaling_piece = 'x=' + str(shrink_scale) + ' y=' + str(shrink_scale)

	IJ.run(cur_image, "Scale...", scaling_piece + " interpolation=Bicubic create average");

	cur_image = IJ.getImage()

	new_type = image_name.replace('.tif', type_to_save_as)
	
	IJ.save(cur_image, outputFolder + new_type)
	cur_image.close()

print 'Done!