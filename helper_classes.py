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

    def folderStructureForRiverpod(self, features):
        pFeatures = f'{self.dParent}\{self.dFeatures}'
        pHome = f'{pFeatures}\{self.dHome}'
        pController = f'{pHome}\{self.dController}'
        pRepository = f'{pHome}\{self.dRepository}'
        pView = f'{pHome}\{self.dViews}'

        foldersToCreate = [pFeatures]

        if (len(features) > 0):
            for feature in features:
                pFeature = f'{pFeatures}\{feature}'
                controller = f'{pFeature}\{self.dController}'
                repository = f'{pFeature}\{self.dRepository}'
                view = f'{pFeature}\{self.dViews}'

                foldersToCreate.extend(
                    [pFeature, controller, repository, view])

        foldersToCreate.extend(
            [pHome, pController, pRepository, pView])

        hf.createFolders(foldersToCreate)

    def filesForRiverpod(self, features):
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

        if (len(features)) > 0:
            for feature in features:
                pFeatureView = f'{self.dParent}\{self.dFeatures}\{feature}\{self.dViews}\{feature}_view.dart'
                pFeatureController = f'{self.dParent}\{self.dFeatures}\{feature}\{self.dController}\{feature}_controller.dart'
                pFeatureRepository = f'{self.dParent}\{self.dFeatures}\{feature}\{self.dRepository}\{feature}_repository.dart'

                pFeatureViewContent = hConst.hHomeViewContent.replace(
                    'HomeView', f'{feature.capitalize()}View')
                pFeatureControllerContent = hConst.hControllerContent.replace(
                    'HomeController', f'{feature.capitalize()}Controller')
                pFeatureRepositoryContent = hConst.hRepoContent.replace(
                    'HomeRepository', f'{feature.capitalize()}Repository')

                featureUpdate = {pFeatureView: pFeatureViewContent, pFeatureController:
                                 pFeatureControllerContent, pFeatureRepository: pFeatureRepositoryContent}

                filesToCreate.update(featureUpdate)

        hf.createFiles(filesToCreate)

    def folderStructureForResponsive(self, features):

        pResponsive = f'{self.dParent}\{self.dResponsive}'
        pCommon = f'{self.dParent}\{self.dCommon}'
        pEnums = f'{pCommon}\{self.dEnums}'
        pUtils = f'{pCommon}\{self.dUtils}'
        pLayouts = f'{self.dParent}\{self.dFeatures}\{self.dHome}\{self.dViews}\{self.dLayouts}'

        foldersToCreate = [pResponsive, pCommon, pEnums, pUtils, pLayouts]

        if (len(features) > 0):
            for feature in features:
                pFeatureLayout = f'{self.dParent}\{self.dFeatures}\{feature}\{self.dViews}\{self.dLayouts}'

                foldersToCreate.append(pFeatureLayout)

        hf.createFolders(foldersToCreate)

    def filesForResponsive(self, features):
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
        pEnumFile = f'{self.dParent}\{self.dCommon}\{self.dEnums}\{enumFile}'
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
            pResponsiveBuilder: hConst.hResponsiveBuilderContent.replace('package:resp', f'package:{self.projectName}'),
            pSizingInformation: hConst.hSizingInfoContent,
            pScreenTypeLayout: hConst.hScreenTypeLayoutContent.replace('package:resp', f'package:{self.projectName}'),
            pHomeMobViewFile: hConst.hRespHomeMob,
            pHomeTabViewFile: hConst.hRespHomeTab,
            pHomeDesktopViewFile: hConst.hRespHomeDesk,
        }

        if (len(features) > 0):
            for feature in features:
                pFeatureMobViewFile = f'{self.dParent}\{self.dFeatures}\{feature}\{self.dViews}\{self.dLayouts}\{feature}_mobile_view.dart'
                pFeatureTabViewFile = f'{self.dParent}\{self.dFeatures}\{feature}\{self.dViews}\{self.dLayouts}\{feature}_tab_view.dart'
                pFeatureDesktopViewFile = f'{self.dParent}\{self.dFeatures}\{feature}\{self.dViews}\{self.dLayouts}\{feature}_desktop_view.dart'
                pFeatureViewFile = f'{self.dParent}\{self.dFeatures}\{feature}\{self.dViews}\{feature}_view.dart'

                mobViewContent = hConst.hRespHomeMob.replace(
                    'Home', feature.capitalize())

                tabViewContent = hConst.hRespHomeTab.replace(
                    'Home', feature.capitalize())

                desktopViewContent = hConst.hRespHomeDesk.replace(
                    'Home', feature.capitalize())

                viewContent = hConst.hResponsiveHomeContent.replace('home', feature).replace(
                    'Home', feature.capitalize())

                featureUpdate = {pFeatureMobViewFile: mobViewContent,
                                 pFeatureTabViewFile: tabViewContent, pFeatureDesktopViewFile: desktopViewContent, pFeatureViewFile: viewContent}

                filesToCreate.update(featureUpdate)

        hf.createFiles(filesToCreate)


class FolderStructues(hFolderStructure):
    projectName = ''

    def __init__(self, projectName):
        self.projectName = projectName
        super().__init__(projectName)

    def basicRiverpodProject(self):
        features = hf.askForFeaturesInProject()
        super().folderStructureForRiverpod(features)
        super().filesForRiverpod(features)

        hf.addFlutterPackage(
            f'{c.Packages().riverpodPackage}', f'.\{self.projectName}')

    def responsiveRiverpodProject(self):
        features = hf.askForFeaturesInProject()
        super().folderStructureForRiverpod(features)
        super().folderStructureForResponsive(features)
        super().filesForRiverpod(features)
        super().filesForResponsive(features)

        hf.addFlutterPackage(
            f'{c.Packages().riverpodPackage}', f'.\{self.projectName}')

    def responsiveAndOrientationRiverPodProject(self):
        pass
