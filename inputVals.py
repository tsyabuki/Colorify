# Reads in input values from the ini file and stores them within callable variables
inputFileName = ''  # Input file name
outputFileName = ''  # New file name
overwrite = False  # Overwrites the file if the new file has an identical name as the input
hue = 0  # Hue value
saturation = 0  # Saturation value

inputList = [0,0,0,0,0]  # This list directly stores each line of the ini file in the list
try:
    with open('input.ini', 'r') as iniOpen: # Opens the input ini file if it exists
        for i in range(len(inputList)): # Cycles through each known ini property
            inputList[i] = iniOpen.readline() # Places each line of the ini file within the list
            if inputList[i][-1] == '\n': # If the added value contains an end line character, it is manually removed
                inputList[i] = inputList[i][0:-1]
except FileNotFoundError: # If the ini file is not found, a blank ini file is created
    iniNew = open('input.ini', 'w')
    iniNew.write("inputfilename=''\noutputfilename=''\noverwrite=False\nhue=0\nsaturation=0")
    iniNew.close()

inputFileName = inputList[0][15:-1]
outputFileName = inputList[1][16:-1]
# Ensures the output file is either a JPG file or a PNG file
if outputFileName[-4:len(outputFileName)] != '.png' and outputFileName[-4:len(outputFileName)] != '.jpg':
    exit('Please output to .png or .jpg')
overwrite = inputList[2][10:len(inputList[2])]
# Parses the ini True and False values
if overwrite.lower() == 'true':
    overwrite = True
else:
    overwrite = False
# Ensures hue is an integer
try:
    hue = int(inputList[3][4:len(inputList[3])])
except ValueError:
    exit('The hue value must be an integer')
# Ensures saturation is an integer
try:
    saturation = int(inputList[4][11:len(inputList[4])])
except ValueError:
    exit('The saturation value must be an integer')
