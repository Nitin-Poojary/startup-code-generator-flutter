import 'package:flutter/material.dart';
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

