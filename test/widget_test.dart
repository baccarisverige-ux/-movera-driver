import 'package:flutter_test/flutter_test.dart';
import 'package:riding_app/main.dart';

void main() {
  testWidgets('driver app boots', (WidgetTester tester) async {
    await tester.pumpWidget(const MoveraDriverApp());
    await tester.pump();
    expect(find.byType(MoveraDriverApp), findsOneWidget);
  });
}
