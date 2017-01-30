# Get the output folder 

command_folder = self.command_to_folder[command]
options = 'save_path=' + command_folder + image_path
IJ.run(command, options)