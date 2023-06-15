import 'package:flutter/material.dart';
import 'package:resp/responsive/responsive_builder.dart';

import '../common/enums.dart';

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

