from pathlib import Path

assets = Path('lib/core/constants/appassets.dart')
text = assets.read_text()
insert = """
  // Canonical references used by existing Driver/shared screens.
  static const String share = 'assets/icons/share.png';
  static const String chatOutl = 'assets/icons/chat_outl.png';
  static const String email = 'assets/icons/email.png';
  static const String callOutl = 'assets/icons/call_outl.png';
  static const String call = 'assets/icons/call.png';
  static const String standard = 'assets/icons/standard.png';
  static const String distance = 'assets/icons/distance.png';
  static const String profile = 'assets/images/profile.png';
  static const String visa = 'assets/images/visa.png';
  static const String download = 'assets/icons/download.png';
  static const String drivingLicence = 'assets/icons/driving_licence.png';
  static const String dbsCertificate = 'assets/icons/dbs_certificate.png';
  static const String privateHireLicence = 'assets/icons/private_hire_licence.png';
  static const String vehicleLicence = 'assets/icons/vehicle_licence.png';
  static const String insurance = 'assets/icons/insurance.png';
  static const String verifyAccount = 'assets/icons/verify_account.png';
"""
if "static const String drivingLicence = 'assets/icons/driving_licence.png';" not in text:
    idx = text.rfind('}')
    text = text[:idx] + insert + text[idx:]
    assets.write_text(text)

colors = Path('lib/core/constants/appcolors.dart')
text = colors.read_text()
if 'static const Color yellow' not in text:
    idx = text.rfind('}')
    text = text[:idx] + "  static const Color yellow = Color(0xFFFAC22F);\n" + text[idx:]
    colors.write_text(text)

Path('test/widget_test.dart').write_text("""import 'package:flutter_test/flutter_test.dart';
import 'package:movera_driver/main.dart';

void main() {
  test('Movera Driver root widget can be constructed', () {
    expect(const MoveraApp(), isA<MoveraApp>());
  });
}
""")

Path(__file__).unlink(missing_ok=True)
