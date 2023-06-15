class Contants:

    hMainContent = '''import 'package:flutter/material.dart';
import 'package:projectName/features/home/views/home_view.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      title: 'Material App',
      home: HomeView(),
    );
  }
}
'''

    hHomeViewContent = '''import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

class HomeView extends ConsumerWidget {
  const HomeView({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    return Container();
  }
}

'''
    hRepoContent = 'class HomeRepository {}'
    hControllerContent = 'class HomeController {}'

    hResponsiveEnum = '''enum DeviceScreenType {
  mobile,
  tablet,
  desktop,
}
'''
    hResponsiveBuilderContent = '''import 'package:flutter/material.dart';
import 'package:resp/responsive/sizing_information.dart';

class ResponsiveBuilder extends StatelessWidget {
  final Widget Function(
    BuildContext context,
    SizingInformation sizingInformation,
  ) builder;

  const ResponsiveBuilder({super.key, required this.builder});

  @override
  Widget build(BuildContext context) {
    SizingInformation sizingInformation = SizingInformation();

    return builder(context, sizingInformation);
  }
}

'''

    hScreenTypeLayoutContent = '''import 'package:flutter/material.dart';
import 'package:resp/responsive/responsive_builder.dart';

import '../common/enums/enums.dart';

class ScreenTypeLayout extends StatelessWidget {
  final Widget mobile;
  final Widget? tablet;
  final Widget? desktop;

  const ScreenTypeLayout({
    super.key,
    required this.mobile,
    this.tablet,
    this.desktop,
  });

  @override
  Widget build(BuildContext context) {
    return ResponsiveBuilder(
      builder: (context, sizingInformation) {
        if (sizingInformation.deviceScreenType == DeviceScreenType.tablet &&
            tablet != null) {
          return tablet!;
        }
        if (sizingInformation.deviceScreenType == DeviceScreenType.desktop &&
            desktop != null) {
          return desktop!;
        }

        return mobile;
      },
    );
  }
}
'''

    hSizingInfoContent = '''import 'package:flutter/material.dart';

import '../common/enums/enums.dart';

class SizingInformation {
  final DeviceScreenType? deviceScreenType;
  final Size? screenSize;
  final Size? localWidgetSize;

  SizingInformation({
    this.deviceScreenType,
    this.screenSize,
    this.localWidgetSize,
  });

  @override
  String toString() {
    return "DeviceScreenType: $deviceScreenType, ScreenSize: $screenSize, LocalWidgetSize: $localWidgetSize";
  }
}
'''

    hResponsiveHomeContent = '''import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../../responsive/screen_type_layout.dart';
import 'layouts/home_desktop_view.dart';
import 'layouts/home_tab_view.dart';
import 'layouts/home_mobile_view.dart';

class HomeView extends ConsumerWidget {
  const HomeView({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    return const ScreenTypeLayout(
      mobile: HomeMobileView(),
      tablet: HomeTabView(),
      desktop: HomeDesktopView(),
    );
  }
}

'''

    hRespHomeMob = hHomeViewContent.replace('HomeView', 'HomeMobileView')
    hRespHomeTab = hHomeViewContent.replace('HomeView', 'HomeTabView')
    hRespHomeDesk = hHomeViewContent.replace('HomeView', 'HomeDesktopView')


class Packages:
    riverpodPackage = 'flutter_riverpod'
    hooks = 'flutter_hooks'
    hooksRiverpod = 'hooks_riverpod'
