import os
import constants as c
import helper_functions as hf


class FolderStructues:
    projectName = ''
    dParent = ''
    dHome = ''
    dFeatures = ''
    dController = ''
    dRepository = ''
    dViews = ''

    dParent = f'.\{projectName}\lib'

    def __init__(self, projectName):
        self.projectName = projectName
        self.dParent = f'.\{projectName}\lib'
        self.dHome = 'home'
        self.dFeatures = 'features'
        self.dController = 'controllers'
        self.dRepository = 'repository'
        self.dViews = 'views'

    def basicRiverpodProject(self):
        self.folderStructureForRiverpod()
        self.filesForRiverpod()

        hf.addFlutterPackage(
            f'{c.Packages().riverpodPackage}', f'.\{self.projectName}')

    def responsiveRiverpodProject(self):
        dEnums = 'enums'
        dResponsive = 'responsive'

        os.mkdir(pEnums)
        os.mkdir(pResponsive)
        os.mkdir(pHome)

    def responsiveAndOrientationRiverPodProject(self):
        pass

    def folderStructureForRiverpod(self):
        pFeatures = f'{self.dParent}\{self.dFeatures}'
        pHome = f'{self.dParent}\{self.dFeatures}\{self.dHome}'
        pController = f'{self.dParent}\{self.dFeatures}\{self.dHome}\{self.dController}'
        pRepository = f'{self.dParent}\{self.dFeatures}\{self.dHome}\{self.dRepository}'
        pView = f'{self.dParent}\{self.dFeatures}\{self.dHome}\{self.dViews}'

        foldersToCreate = [pFeatures, pHome, pController, pRepository, pView]

        hf.createFolders(foldersToCreate)

    def filesForRiverpod(self):
        hConst = c.Contants()

        mainFile = 'main.dart'
        homeViewFile = 'home_view.dart'
        homeControllerFile = 'home_controller.dart'
        homeRepoFile = 'home_repository.dart'

        pMainFile = f'{self.dParent}\{mainFile}'
        pHomeViewFile = f'{self.dParent}\{self.dFeatures}\{self.dHome}\{self.dViews}\{homeViewFile}'
        pHomeControllerFile = f'{self.dParent}\{self.dFeatures}\{self.dHome}\{self.dController}\{homeControllerFile}'
        pHomeRepoFile = f'{self.dParent}\{self.dFeatures}\{self.dHome}\{self.dRepository}\{homeRepoFile}'

        filesToCreate = {
            pMainFile: hConst.hMainContent.replace(
                'projectName', self.projectName),
            pHomeViewFile: hConst.hHomeViewContent,
            pHomeControllerFile: hConst.hControllerContent,
            pHomeRepoFile: hConst.hRepoContent
        }

        hf.createFiles(filesToCreate)
