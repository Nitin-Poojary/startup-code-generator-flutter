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


class Packages:
    riverpodPackage = 'flutter_riverpod'
    hooks = 'flutter_hooks'
    hooksRiverpod = 'hooks_riverpod'
