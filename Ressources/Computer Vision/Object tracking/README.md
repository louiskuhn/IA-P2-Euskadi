# Attention pour goturn, il faut préalablement récupérer le modèle

Les 2 fichiers suivants doivent être dans le répertoire courant :
1. `goturn.caffemodel`
2. `goturn.prototxt`
Je peux pas les mettre sur le repo puisque trop lourd...

Voilà la démarche pour les récupérer. En english siouplé

## Download model files
`goturn.caffemodel` and `goturn.prototxt` file can be downloaded from [opencv_extra](https://github.com/opencv/opencv_extra/tree/c4219d5eb3105ed8e634278fad312a1a8d2c182d/testdata/tracking).
To use the `goturn.caffemodel` file, first follow the instructions given below to unzip the split files.

### Instructions to unzip `goturn.caffemodel` split zip files

#### Windows

1) Click “Start” if you have Windows XP or later versions and choose “Programs,” “Accessories” and “Windows Explorer.” The Windows Explorer window appears.
 
2) Navigate to the folder containing the zip files by double-clicking drives and folders to open them.
 
3) Choose “File” from the Windows Explorer window and select “New” and “Folder” to create a new folder. You can optionally rename this folder by right-clicking it and choosing “Rename.”
 
4) Drag the split zip archives into this new folder. Open the folder to reveal its contents. All the 4 pieces of the complete zip must be in the folder or you cannot extract them.

5) Right-click the first zip file and choose “Open With” and then “Compress (zipped) Folder.” The original file appears in a new window.
Click “Extract All Files” in the Folder Tasks pane on the right side of the window. A wizard is displayed. Specify a location for the extracted archive, which by default is the current folder. Then go through the wizard to complete extraction.
 
6) The file will be extracted to specified location.

7) Copy/cut the unzipped `goturn.caffemodel` file to the directory containing the codes.

#### Linux

1) Use `terminal` to navigate to the folder containing the split zip files.

2) Use `cat` command to merge the split files:

`cat goturn.caffemodel.zip* > goturn.caffemodel.zip`

3) Unzip the zip file:

`unzip goturn.caffemodel.zip`

4) Move the unzipped `goturn.caffemodel` to the directory containing the codes.


