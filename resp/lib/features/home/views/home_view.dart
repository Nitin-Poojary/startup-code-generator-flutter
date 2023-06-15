import 'package:flutter/material.dart';
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

