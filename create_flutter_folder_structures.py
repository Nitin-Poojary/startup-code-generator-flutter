import helper_functions as hf
import helper_classes as hc

nameOfProject = hf.getProjectName()
hf.createFlutterProject(nameOfProject)

createStructures = hc.FolderStructues(nameOfProject)
createStructures.basicRiverpodProject()

hf.flutterPubGet(nameOfProject)
