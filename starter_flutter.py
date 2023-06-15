import helper_functions as hf
import helper_classes as hc

nameOfProject = hf.getProjectName()
hf.createFlutterProject(nameOfProject)

createStructures = hc.FolderStructues(nameOfProject)

projectType = hf.askForTypeOfProject()

if projectType == 1:
    createStructures.basicRiverpodProject()
else:
    createStructures.responsiveRiverpodProject()

hf.flutterPubGet(nameOfProject)
