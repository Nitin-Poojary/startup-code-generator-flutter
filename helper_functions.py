import subprocess
import os
import time


def getProjectName():
    projectName = input('Project name: ')
    return projectName


def createFlutterProject(projectName):
    flutterPath = 'C:\\Users\\sachi\\Downloads\\flutter_windows_3.0.5-stable\\flutter\\bin\\flutter.bat'
    runTerminalCommand(f'{flutterPath} create {projectName}')


def flutterPubGet(projectName):
    flutterPath = 'C:\\Users\\sachi\\Downloads\\flutter_windows_3.0.5-stable\\flutter\\bin\\flutter.bat'
    runTerminalCommand(f'{flutterPath} pub get',
                       directoryName=f'.\{projectName}')


def addFlutterPackage(packageName, directoryName):
    flutterPath = 'C:\\Users\\sachi\\Downloads\\flutter_windows_3.0.5-stable\\flutter\\bin\\flutter.bat'
    runTerminalCommand(f'{flutterPath} pub add {packageName}',
                       directoryName=directoryName)


def runTerminalCommand(command, directoryName=''):
    try:
        if (len(directoryName) > 0):
            process = subprocess.Popen(command, cwd=directoryName)
            process.wait()
        else:
            process = subprocess.Popen(command)
            process.wait()
    except ():
        print('some error occured during while executing some commands')


def createFile(fileName, content):

    with open(fileName, 'w') as f:
        f.write(content)
        print(f"File {fileName} created successfully.")


def createFolders(folders):
    for i in range(len(folders)):
        if i > 0:
            if doesFolderExists(folders[i - 1]):
                os.mkdir(folders[i])
        else:
            os.mkdir(folders[i])


def createFiles(files):
    for filePath in files:
        createFile(filePath, files[filePath])


def doesFolderExists(filePath):
    while not os.path.exists(filePath):
        print(f'Creating {filePath} ...')
        time.sleep(0.1)

    files = filePath.split('\\')
    return True
