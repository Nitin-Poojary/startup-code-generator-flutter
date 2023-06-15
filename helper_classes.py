import constants as c
import helper_functions as hf


class hFolderStructure:
    projectName = ''
    dParent = ''
    dHome = ''
    dFeatures = ''
    dController = ''
    dRepository = ''
    dViews = ''
    dEnum = ''
    dResponsive = ''
    dCommon = ''
    dUtils = ''
    dLayouts = ''
    dOrientation = ''

    dParent = f'.\{projectName}\lib'

    def __init__(self, projectName):
        self.projectName = projectName
        self.dParent = f'.\{projectName}\lib'
        self.dHome = 'home'
        self.dFeatures = 'features'
        self.dController = 'controllers'
        self.dRepository = 'repository'
        self.dViews = 'views'
        self.dEnums = 'enums'
        self.dResponsive = 'responsive'
        self.dCommon = 'common'
        self.dUtils = 'utils'
        self.dLayouts = 'layouts'
        self.dOrientation = 'orientation'

    def folderStructureForRiverpod(self):
        pFeatures = f'{self.dParent}\{self.dFeatures}'
        pHome = f'{pFeatures}\{self.dHome}'
        pController = f'{pHome}\{self.dController}'
        pRepository = f'{pHome}\{self.dRepository}'
        pView = f'{pHome}\{self.dViews}'

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

    def folderStructureForResponsive(self):

        pResponsive = f'{self.dParent}\{self.dResponsive}'
        pCommon = f'{self.dParent}\{self.dCommon}'
        pEnums = f'{pCommon}\{self.dEnums}'
        pUtils = f'{pCommon}\{self.dUtils}'
        pLayouts = f'{self.dParent}\{self.dFeatures}\{self.dHome}\{self.dViews}\{self.dLayouts}'

        folderToCreate = [pResponsive, pCommon, pEnums, pUtils, pLayouts]

        hf.createFolders(folderToCreate)

    def filesForResponsive(self):
        hConst = c.Contants()

        mainFile = 'main.dart'
        homeViewFile = 'home_view.dart'
        enumFile = 'enums.dart'
        responsiveBuilder = 'responsive_builder.dart'
        sizingInformation = 'sizing_information.dart'
        screenTypeLayout = 'screen_type_layout.dart'
        homeMobViewFile = 'home_mobile_view.dart'
        homeTabViewFile = 'home_tab_view.dart'
        homeDeskViewFile = 'home_desktop_view.dart'

        pMainFile = f'{self.dParent}\{mainFile}'
        pHomeViewFile = f'{self.dParent}\{self.dFeatures}\{self.dHome}\{self.dViews}\{homeViewFile}'
        pEnumFile = f'{self.dParent}\{self.dCommon}\{self.dEnum}\{enumFile}'
        pResponsiveBuilder = f'{self.dParent}\{self.dResponsive}\{responsiveBuilder}'
        pSizingInformation = f'{self.dParent}\{self.dResponsive}\{sizingInformation}'
        pScreenTypeLayout = f'{self.dParent}\{self.dResponsive}\{screenTypeLayout}'
        pHomeMobViewFile = f'{self.dParent}\{self.dFeatures}\{self.dHome}\{self.dViews}\{self.dLayouts}\{homeMobViewFile}'
        pHomeTabViewFile = f'{self.dParent}\{self.dFeatures}\{self.dHome}\{self.dViews}\{self.dLayouts}\{homeTabViewFile}'
        pHomeDesktopViewFile = f'{self.dParent}\{self.dFeatures}\{self.dHome}\{self.dViews}\{self.dLayouts}\{homeDeskViewFile}'

        filesToCreate = {
            pMainFile: hConst.hMainContent.replace(
                'projectName', self.projectName),
            pHomeViewFile: hConst.hResponsiveHomeContent,
            pEnumFile: hConst.hResponsiveEnum,
            pResponsiveBuilder: hConst.hResponsiveBuilderContent,
            pSizingInformation: hConst.hSizingInfoContent,
            pScreenTypeLayout: hConst.hScreenTypeLayoutContent,
            pHomeMobViewFile: hConst.hRespHomeMob,
            pHomeTabViewFile: hConst.hRespHomeTab,
            pHomeDesktopViewFile: hConst.hRespHomeDesk,
        }

        hf.createFiles(filesToCreate)


class FolderStructues(hFolderStructure):
    projectName = ''

    def __init__(self, projectName):
        self.projectName = projectName
        super().__init__(projectName)

    def basicRiverpodProject(self):
        super().folderStructureForRiverpod()
        super().filesForRiverpod()

        hf.addFlutterPackage(
            f'{c.Packages().riverpodPackage}', f'.\{self.projectName}')

    def responsiveRiverpodProject(self):
        super().folderStructureForRiverpod()
        super().folderStructureForResponsive()
        super().filesForRiverpod()
        super().filesForResponsive()

        hf.addFlutterPackage(
            f'{c.Packages().riverpodPackage}', f'.\{self.projectName}')

    def responsiveAndOrientationRiverPodProject(self):
        pass
