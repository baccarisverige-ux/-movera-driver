import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:get/get.dart';
import 'package:movera_driver/constants/appcolors.dart';
import 'package:movera_driver/presentation/common/splash/splash.dart';

void main() {
  runApp(const MoveraDriverApp());
}

class MoveraDriverApp extends StatelessWidget {
  const MoveraDriverApp({super.key});

  @override
  Widget build(BuildContext context) {
    return ScreenUtilInit(
      designSize: const Size(375, 812),
      minTextAdapt: true,
      splitScreenMode: true,
      ensureScreenSize: true,
      builder: (_, child) {
        return GetMaterialApp(
          title: 'Movera Driver',
          debugShowCheckedModeBanner: false,
          theme: ThemeData.light(
            useMaterial3: true,
          ).copyWith(scaffoldBackgroundColor: AppColor.bg),
          home: Splash(),
        );
      },
    );
  }
}
