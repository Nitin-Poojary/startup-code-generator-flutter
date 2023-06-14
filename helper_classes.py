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
        dHome = 'home'

        dParent = f'.\{projectName}\lib'

        pEnums = os.path.join(dParent, dEnums)
        pResponsive = os.path.join(dParent, dResponsive)
        pHome = os.path.join(dParent, dHome)

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

        os.mkdir(pFeatures)

        if (hf.doesFolderExists(pFeatures)):
            (os.mkdir(pHome))

        if (hf.doesFolderExists(pHome)):
            os.mkdir(pController)
            os.mkdir(pRepository)
            os.mkdir(pView)

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

        hf.createFile(self.projectName, pMainFile, hConst.hMainContent.replace(
            'projectName', self.projectName))
        hf.createFile(self.projectName, pHomeViewFile, hConst.hHomeViewContent)
        hf.createFile(self.projectName, pHomeControllerFile,
                      hConst.hControllerContent)
        hf.createFile(self.projectName, pHomeRepoFile, hConst.hRepoContent)
