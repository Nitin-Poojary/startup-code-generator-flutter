import 'package:flutter/material.dart';

import '../common/enums.dart';

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

