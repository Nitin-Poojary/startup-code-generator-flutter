import subprocess
import os
import time


def getProjectName():
    projectName = input('Project name: ')
    return projectName


def getFlutterPath():
    try:
        with open('.\\flutterpath.txt', 'r') as f:
            flutterPath = f.read()
            return flutterPath
    except FileNotFoundError:
        flutterPath = input(
            'Enter path to you flutter batch file flutter.bat in bin folder of your flutter:\n')

        with open('.\\flutterpath.txt', 'w') as f:
            f.write(flutterPath)

        return flutterPath


def askForTypeOfProject():
    print('Select the type of project:')
    typeOfProject = int(input(
        '1. Basic Riverpod structure project\n2. Responsive riverpod structure project\n'))

    while typeOfProject not in range(1, 3):
        typeOfProject = askForTypeOfProject()

    return typeOfProject


def askForFeaturesInProject():
    featuresString = input(
        'This project will be using feature first approach.\nEnter the features you want in your app:\nExample: auth, chat, call, products, home or type skip to skip this step\n')

    if featuresString.lower() == 'skip':
        return []
    else:
        featuresList = featuresString.split(',')
        features = []

        for feature in featuresList:
            features.append(feature.strip())

        if 'home' in features:
            features.remove('home')
        return features


def createFlutterProject(projectName):
    flutterPath = getFlutterPath()
    runTerminalCommand(f'{flutterPath} create {projectName}')


def flutterPubGet(projectName):
    flutterPath = getFlutterPath()
    runTerminalCommand(f'{flutterPath} pub get',
                       directoryName=f'.\{projectName}')


def addFlutterPackage(packageName, directoryName):
    flutterPath = getFlutterPath()
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


def createFile(filePath, content):

    with open(filePath, 'w') as f:
        f.write(content)
        print(f"File {filePath} created successfully.")


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
