import 'package:flutter_test/flutter_test.dart';
import 'package:movera_driver/main.dart';

void main() {
  test('Movera Driver root widget can be constructed', () {
    expect(const MoveraApp(), isA<MoveraApp>());
  });
}
